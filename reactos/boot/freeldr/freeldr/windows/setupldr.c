/*
 *  FreeLoader
 *
 *  Copyright (C) 2009       Aleksey Bragin  <aleksey@reactos.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, write to the Free Software Foundation, Inc.,
 *  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

#include <freeldr.h>

#include <ndk/ldrtypes.h>
#include <arc/setupblk.h>

#include <debug.h>

// TODO: Move to .h
VOID AllocateAndInitLPB(PLOADER_PARAMETER_BLOCK *OutLoaderBlock);
BOOLEAN WinLdrLoadBootDrivers(PLOADER_PARAMETER_BLOCK LoaderBlock, LPSTR BootPath);
void WinLdrSetupForNt(PLOADER_PARAMETER_BLOCK LoaderBlock,
                      PVOID *GdtIdt,
                      ULONG *PcrBasePage,
                      ULONG *TssBasePage);
VOID
WinLdrInitializePhase1(PLOADER_PARAMETER_BLOCK LoaderBlock,
                       PCHAR Options,
                       PCHAR SystemPath,
                       PCHAR BootPath,
                       USHORT VersionToBoot);
BOOLEAN
WinLdrLoadNLSData(IN OUT PLOADER_PARAMETER_BLOCK LoaderBlock,
                  IN LPCSTR DirectoryPath,
                  IN LPCSTR AnsiFileName,
                  IN LPCSTR OemFileName,
                  IN LPCSTR LanguageFileName);
BOOLEAN
WinLdrAddDriverToList(LIST_ENTRY *BootDriverListHead,
                      LPWSTR RegistryPath,
                      LPWSTR ImagePath,
                      LPWSTR ServiceName);


//FIXME: Do a better way to retrieve Arc disk information
extern ULONG reactos_disk_count;
extern ARC_DISK_SIGNATURE reactos_arc_disk_info[];
extern char reactos_arc_strings[32][256];

extern BOOLEAN UseRealHeap;
extern ULONG LoaderPagesSpanned;


VOID
SetupLdrLoadNlsData(PLOADER_PARAMETER_BLOCK LoaderBlock, HINF InfHandle, LPCSTR SearchPath)
{
    INFCONTEXT InfContext;
    BOOLEAN Status;
    LPCSTR AnsiName, OemName, LangName;

    /* Get ANSI codepage file */
    if (!InfFindFirstLine(InfHandle, "NLS", "AnsiCodepage", &InfContext))
    {
        printf("Failed to find 'NLS/AnsiCodepage'\n");
        return;
    }
    if (!InfGetDataField(&InfContext, 1, &AnsiName))
    {
        printf("Failed to get load options\n");
        return;
    }

    /* Get OEM codepage file */
    if (!InfFindFirstLine(InfHandle, "NLS", "OemCodepage", &InfContext))
    {
        printf("Failed to find 'NLS/AnsiCodepage'\n");
        return;
    }
    if (!InfGetDataField(&InfContext, 1, &OemName))
    {
        printf("Failed to get load options\n");
        return;
    }

    if (!InfFindFirstLine(InfHandle, "NLS", "UnicodeCasetable", &InfContext))
    {
        printf("Failed to find 'NLS/AnsiCodepage'\n");
        return;
    }
    if (!InfGetDataField(&InfContext, 1, &LangName))
    {
        printf("Failed to get load options\n");
        return;
    }

    Status = WinLdrLoadNLSData(LoaderBlock, SearchPath, AnsiName, OemName, LangName);
    DPRINTM(DPRINT_WINDOWS, "NLS data loaded with status %d\n", Status);
}

VOID
SetupLdrScanBootDrivers(PLOADER_PARAMETER_BLOCK LoaderBlock, HINF InfHandle, LPCSTR SearchPath)
{
    INFCONTEXT InfContext, dirContext;
    BOOLEAN Status;
    LPCSTR Media, DriverName, dirIndex, ImagePath;
    WCHAR ServiceName[256];
    WCHAR ImagePathW[256];

    /* Open inf section */
    if (!InfFindFirstLine(InfHandle, "SourceDisksFiles", NULL, &InfContext))
        return;

    /* Load all listed boot drivers */
    do
    {
        if (InfGetDataField(&InfContext, 7, &Media) &&
            InfGetDataField(&InfContext, 0, &DriverName) &&
            InfGetDataField(&InfContext, 13, &dirIndex))
        {
            if ((strcmp(Media, "x") == 0) &&
                InfFindFirstLine(InfHandle, "Directories", dirIndex, &dirContext) &&
                InfGetDataField(&dirContext, 1, &ImagePath))
            {
                /* Convert name to widechar */
                swprintf(ServiceName, L"%S", DriverName);

                /* Prepare image path */
                swprintf(ImagePathW, L"%S", ImagePath);
                wcscat(ImagePathW, L"\\");
                wcscat(ImagePathW, ServiceName);

                /* Remove .sys extension */
                ServiceName[wcslen(ServiceName) - 4] = 0;

                /* Add it to the list */
                Status = WinLdrAddDriverToList(&LoaderBlock->BootDriverListHead,
                    L"\\Registry\\Machine\\System\\CurrentControlSet\\Services\\",
                    ImagePathW,
                    ServiceName);

                if (!Status)
                {
                    DPRINTM(DPRINT_WINDOWS, "could not add boot driver %s, %s\n", SearchPath, DriverName);
                    return;
                }
            }
        }
    } while (InfFindNextLine(&InfContext, &InfContext));
}

VOID LoadReactOSSetup2(VOID)
{
    CHAR  SystemPath[512], SearchPath[512];
    CHAR  FileName[512];
    CHAR  BootPath[512];
    LPCSTR LoadOptions, BootOptions;
    BOOLEAN BootFromFloppy;
#if DBG
    LPCSTR DbgOptions;
#endif
    PVOID NtosBase = NULL, HalBase = NULL, KdComBase = NULL;
    BOOLEAN Status;
    ULONG i, ErrorLine;
    HINF InfHandle;
    INFCONTEXT InfContext;
    PLOADER_PARAMETER_BLOCK LoaderBlock, LoaderBlockVA;
    PSETUP_LOADER_BLOCK SetupBlock;
    KERNEL_ENTRY_POINT KiSystemStartup;
    PLDR_DATA_TABLE_ENTRY KernelDTE, HalDTE, KdComDTE = NULL;
    // Mm-related things
    PVOID GdtIdt;
    ULONG PcrBasePage=0;
    ULONG TssBasePage=0;
    LPCSTR SourcePath;
    LPCSTR SourcePaths[] =
    {
        "", /* Only for floppy boot */
#if defined(_M_IX86)
        "\\I386",
#elif defined(_M_MPPC)
        "\\PPC",
#elif defined(_M_MRX000)
        "\\MIPS",
#endif
        "\\reactos",
        NULL
    };

    /* Get boot path */
    MachDiskGetBootPath(SystemPath, sizeof(SystemPath));

    /* And check if we booted from floppy */
    BootFromFloppy = strstr(SystemPath, "fdisk") != NULL;

    /* Open 'txtsetup.sif' from any of source paths */
    for (i = BootFromFloppy ? 0 : 1; ; i++)
    {
        SourcePath = SourcePaths[i];
        if (!SourcePath)
        {
            printf("Failed to open 'txtsetup.sif'\n");
            return;
        }
        sprintf(FileName, "%s\\txtsetup.sif", SourcePath);
        if (InfOpenFile (&InfHandle, FileName, &ErrorLine))
        {
            sprintf(BootPath, "%s%s\\", SystemPath, SourcePath);
            break;
        }
    }

    /* Get Load options - debug and non-debug */
    if (!InfFindFirstLine(InfHandle,
                          "SetupData",
                          "OsLoadOptions",
                          &InfContext))
    {
        printf("Failed to find 'SetupData/OsLoadOptions'\n");
        return;
    }

    if (!InfGetDataField (&InfContext, 1, &LoadOptions))
    {
        printf("Failed to get load options\n");
        return;
    }

    BootOptions = LoadOptions;

#if DBG
    /* Get debug load options and use them */
    if (InfFindFirstLine(InfHandle,
                         "SetupData",
                         "DbgOsLoadOptions",
                         &InfContext))
    {
        if (!InfGetDataField(&InfContext, 1, &DbgOptions))
            DbgOptions = "";
        else
            BootOptions = DbgOptions;
    }
#endif

    DPRINTM(DPRINT_WINDOWS,"BootOptions: '%s'\n", BootOptions);

    SetupUiInitialize();
    UiDrawStatusText("");
    UiDrawStatusText("Detecting Hardware...");

    /* Let user know we started loading */
    UiDrawStatusText("Loading...");

    /* Construct the system path */
    sprintf(SystemPath, "%s\\", SourcePath);

    DPRINTM(DPRINT_WINDOWS,"BootPath: '%s', SystemPath: '%s'\n", BootPath, SystemPath);

    /* Allocate and minimalistic-initialize LPB */
    AllocateAndInitLPB(&LoaderBlock);

    /* Allocate and initialize setup loader block */
    SetupBlock = MmHeapAlloc(sizeof(SETUP_LOADER_BLOCK));
    RtlZeroMemory(SetupBlock, sizeof(SETUP_LOADER_BLOCK));
    LoaderBlock->SetupLdrBlock = SetupBlock;

    /* Set textmode setup flag */
    SetupBlock->Flags = SETUPLDR_TEXT_MODE;

    /* Detect hardware */
    UseRealHeap = TRUE;
    LoaderBlock->ConfigurationRoot = MachHwDetect();

	strcpy(FileName, "\\ArcName\\");

    /* Load kernel */
    strcpy(FileName+strlen("\\ArcName\\"), BootPath);
    strcat(FileName, "SYSTEM32\\NTOSKRNL.EXE");
    Status = WinLdrLoadImage(FileName+strlen("\\ArcName\\"), LoaderSystemCode, &NtosBase);
    DPRINTM(DPRINT_WINDOWS, "Ntos loaded with status %d at %p\n", Status, NtosBase);
    Status = WinLdrAllocateDataTableEntry(LoaderBlock, "ntoskrnl.exe",
        FileName, NtosBase, &KernelDTE);
    DPRINTM(DPRINT_WINDOWS, "Ntos Data Table Entry allocated with status %d at %p\n", Status, KernelDTE);

    /* Load HAL */
    strcpy(FileName+strlen("\\ArcName\\"), BootPath);
    strcat(FileName, "SYSTEM32\\HAL.DLL");
    Status = WinLdrLoadImage(FileName+strlen("\\ArcName\\"), LoaderHalCode, &HalBase);
    DPRINTM(DPRINT_WINDOWS, "HAL loaded with status %d at %p\n", Status, HalBase);
    Status = WinLdrAllocateDataTableEntry(LoaderBlock, "hal.dll",
        FileName, HalBase, &HalDTE);
    DPRINTM(DPRINT_WINDOWS, "HAL Data Table Entry allocated with status %d at %p\n", Status, HalDTE);

    /* Load kernel-debugger support dll */
    strcpy(FileName+strlen("\\ArcName\\"), BootPath);
    strcat(FileName, "SYSTEM32\\KDCOM.DLL");
    Status = WinLdrLoadImage(FileName+strlen("\\ArcName\\"), LoaderBootDriver, &KdComBase);
    DPRINTM(DPRINT_WINDOWS, "KdCom loaded with status %d at %p\n", Status, KdComBase);
    Status = WinLdrAllocateDataTableEntry(LoaderBlock, "kdcom.dll",
        FileName, KdComBase, &KdComDTE);
    DPRINTM(DPRINT_WINDOWS, "KdCom Data Table Entry allocated with status %d at %p\n", Status, HalDTE);

    /* Load all referenced DLLs for kernel, HAL and kdcom.dll */
    strcpy(SearchPath, BootPath);
    strcat(SearchPath, "system32\\");
    Status = WinLdrScanImportDescriptorTable(LoaderBlock, SearchPath, KernelDTE);
    Status &= WinLdrScanImportDescriptorTable(LoaderBlock, SearchPath, HalDTE);
    if (KdComDTE)
        Status &= WinLdrScanImportDescriptorTable(LoaderBlock, SearchPath, KdComDTE);

    if (!Status)
    {
        UiMessageBox("Error loading imported dll.");
        return;
    }

    /* Load NLS data, they are in system32 */
    SetupLdrLoadNlsData(LoaderBlock, InfHandle, SearchPath);

    /* Get a list of boot drivers */
    SetupLdrScanBootDrivers(LoaderBlock, InfHandle, BootPath);

    /* Load boot drivers */
    Status = WinLdrLoadBootDrivers(LoaderBlock, BootPath);
    DPRINTM(DPRINT_WINDOWS, "Boot drivers loaded with status %d\n", Status);

    /* Alloc PCR, TSS, do magic things with the GDT/IDT */
    WinLdrSetupForNt(LoaderBlock, &GdtIdt, &PcrBasePage, &TssBasePage);

    /* Initialize Phase 1 - no drivers loading anymore */
    WinLdrInitializePhase1(LoaderBlock, (PCHAR)BootOptions, SystemPath, BootPath, _WIN32_WINNT_WS03);

    /* Save entry-point pointer and Loader block VAs */
    KiSystemStartup = (KERNEL_ENTRY_POINT)KernelDTE->EntryPoint;
    LoaderBlockVA = PaToVa(LoaderBlock);

    /* "Stop all motors", change videomode */
    MachPrepareForReactOS(TRUE);

    /* Debugging... */
    //DumpMemoryAllocMap();

    /* Turn on paging mode of CPU*/
    WinLdrTurnOnPaging(LoaderBlock, PcrBasePage, TssBasePage, GdtIdt);

    /* Save final value of LoaderPagesSpanned */
    LoaderBlock->Extension->LoaderPagesSpanned = LoaderPagesSpanned;

    DPRINTM(DPRINT_WINDOWS, "Hello from paged mode, KiSystemStartup %p, LoaderBlockVA %p!\n",
        KiSystemStartup, LoaderBlockVA);

    //WinLdrpDumpMemoryDescriptors(LoaderBlockVA);
    //WinLdrpDumpBootDriver(LoaderBlockVA);
    //WinLdrpDumpArcDisks(LoaderBlockVA);

    /*asm(".intel_syntax noprefix\n");
    asm("test1:\n");
    asm("jmp test1\n");
    asm(".att_syntax\n");*/

    /* Pass control */
    (*KiSystemStartup)(LoaderBlockVA);

    return;
}