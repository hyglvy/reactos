@ stdcall AcquireSRWLockExclusive(ptr) ntdll.RtlAcquireSRWLockExclusive
@ stdcall AcquireSRWLockShared(ptr) ntdll.RtlAcquireSRWLockShared
@ stdcall ActivateActCtx(ptr ptr)
@ stdcall AddAtomA(str)
@ stdcall AddAtomW(wstr)
@ stdcall AddConsoleAliasA(str str str) ;check
@ stdcall AddConsoleAliasW(wstr wstr wstr) ;check
;@ stdcall -arch=x86_64 AddIntegrityLabelToBoundaryDescriptor ; Win 7
@ stdcall AddLocalAlternateComputerNameA(str ptr)
@ stdcall AddLocalAlternateComputerNameW(wstr ptr)
@ stdcall AddRefActCtx(ptr)
;@ stdcall AddSIDToBoundaryDescriptor ; Win 7
;@ stdcall AddSecureMemoryCacheCallback ; Win 7
@ stdcall AddVectoredContinueHandler(long ptr) ntdll.RtlAddVectoredContinueHandler
@ stdcall AddVectoredExceptionHandler(long ptr) ntdll.RtlAddVectoredExceptionHandler
;@ stdcall AdjustCalendarDate ; Win 7
@ stdcall AllocConsole()
;@ stub AllocLSCallback ; missing in XP SP3 and 2003 R2 and Win 7
@ stdcall AllocateUserPhysicalPages(long ptr ptr)
;@ stdcall AllocateUserPhysicalPagesNuma ; Win 7
;@ stdcall ApplicationRecoveryFinished ; Win 7
;@ stdcall ApplicationRecoveryInProgress ; Win 7
@ stdcall AreFileApisANSI()
@ stdcall AssignProcessToJobObject(ptr ptr)
@ stdcall AttachConsole(long)
@ stdcall BackupRead(ptr ptr long ptr long long ptr)
@ stdcall BackupSeek(ptr long long ptr ptr ptr)
@ stdcall BackupWrite(ptr ptr long ptr long long ptr)
@ stdcall BaseCheckAppcompatCache(long long long ptr) ;check
;@ stdcall BaseCheckAppcompatCacheEx ; Win7
;@ stub BaseCheckRunApp ; Win7
@ stdcall BaseCleanupAppcompatCache() ; missing in Win 7
@ stdcall BaseCleanupAppcompatCacheSupport(ptr)
;@ stdcall BaseDllReadWriteIniFile ; Win 7
@ stdcall BaseDumpAppcompatCache()
@ stdcall BaseFlushAppcompatCache()
;@ stdcall BaseFormatObjectAttributes ; Win 7
;@ stdcall BaseFormatTimeOut ; Win 7
;@ stdcall BaseGenerateAppCompatData ; Win 7
;@ stdcall BaseGetNamedObjectDirectory ; Win 7
@ stdcall BaseInitAppcompatCache() ; missing in Win 7
@ stdcall BaseInitAppcompatCacheSupport()
;@ stdcall BaseIsAppcompatInfrastructureDisabled ; Win 7
@ stdcall BaseProcessInitPostImport() ; missing in Win 7
@ stdcall BaseQueryModuleData(str str ptr ptr ptr) ;check
;@ stdcall BaseThreadInitThunk ; Win 7
;@ stdcall BaseSetLastNTError ; Win 7, not 64 bit (present on w2k3 but not exported)
@ stdcall BaseUpdateAppcompatCache(long long long)
;@ stdcall BaseVerifyUnicodeString ; Win 7
;@ stdcall Basep8BitStringToDynamicUnicodeString ; Win 7
;@ stdcall BasepAllocateActivationContextActivationBlock ; Win 7
;@ stdcall BasepAnsiStringToDynamicUnicodeString ; Win 7
;@ stdcall BasepCheckAppCompat ; Win 7
;@ stdcall BasepCheckBadapp ; Win 7
@ stdcall BasepCheckWinSaferRestrictions(long long long long long long)
;@ stub BasepDebugDump ; missing in XP SP3 and Win 7
;@ stdcall BasepFreeActivationContextActivationBlock ; Win 7
;@ stdcall BasepFreeAppCompatData ; Win 7
;@ stdcall BasepMapModuleHandle ; Win 7
@ stdcall Beep(long long)
@ stdcall BeginUpdateResourceA(str long)
@ stdcall BeginUpdateResourceW(wstr long)
@ stdcall BindIoCompletionCallback(long ptr long)
@ stdcall BuildCommDCBA(str ptr)
@ stdcall BuildCommDCBAndTimeoutsA(str ptr ptr)
@ stdcall BuildCommDCBAndTimeoutsW(wstr ptr ptr)
@ stdcall BuildCommDCBW(wstr ptr)
@ stdcall CallNamedPipeA(str ptr long ptr long ptr long)
@ stdcall CallNamedPipeW(wstr ptr long ptr long ptr long)
;@ stdcall CallbackMayRunLong ; Win 7
@ stdcall CancelDeviceWakeupRequest(long)
@ stdcall CancelIo(long)
@ stdcall CancelIoEx(long ptr)
@ stdcall CancelSynchronousIo(long)
;@ stdcall CancelThreadpoolIo(ptr) ntdll.TpCancelAsyncIoOperation; Win 7
@ stdcall CancelTimerQueueTimer(long long)
@ stdcall CancelWaitableTimer(long)
@ stdcall ChangeTimerQueueTimer(ptr ptr long long)
;@ stdcall CheckElevation ; Win 7
;@ stdcall CheckElevationEnabled ; Win 7
;@ stdcall CheckForReadOnlyResource ; Win 7
@ stdcall CheckNameLegalDOS8Dot3A(str str long long long)
@ stdcall CheckNameLegalDOS8Dot3W(wstr str long long long)
@ stdcall CheckRemoteDebuggerPresent(long ptr)
@ stdcall ClearCommBreak(long)
@ stdcall ClearCommError(long ptr ptr)
@ stdcall CloseConsoleHandle(long)
@ stdcall CloseHandle(long)
;@ stdcall ClosePrivateNamespace ; Win 7
@ stdcall CloseProfileUserMapping()
; @ stub CloseSystemHandle ; missing in XP SP3 and Win 7
;@ stdcall CloseThreadpool(ptr) ntdll.TpReleasePool ; Win 7
;@ stdcall CloseThreadpoolCleanupGroup(ptr) ntdll.TpReleaseCleanupGroup ; Win 7
;@ stdcall CloseThreadpoolCleanupGroupMembers(ptr long ptr) ntdll.TpReleaseCleanupGroupMembers ; Win 7
;@ stdcall CloseThreadpoolIo ntdll.TpReleaseIoCompletion ; Win 7
;@ stdcall CloseThreadpoolTimer ntdll.TpReleaseTimer ; Win 7
;@ stdcall CloseThreadpoolWait ntdll.TpReleaseWait ; Win 7
;@ stdcall CloseThreadpoolWork ntdll.TpReleaseWork ; Win 7
@ stdcall CmdBatNotification(long)
@ stdcall CommConfigDialogA(str long ptr)
@ stdcall CommConfigDialogW(wstr long ptr)
;@ stdcall CompareCalendarDates ; Win 7
@ stdcall CompareFileTime(ptr ptr)
@ stdcall CompareStringA(long long str long str long)
;@ stdcall CompareStringEx ; Win 7
;@ stdcall CompareStringOrdinal ; Win 7
@ stdcall CompareStringW(long long wstr long wstr long)
@ stdcall ConnectNamedPipe(long ptr)
@ stdcall ConsoleMenuControl(long long long)
; @ stub ConsoleSubst ; missing in XP SP3 and Win 7
@ stdcall ContinueDebugEvent(long long long)
;@ stdcall ConvertCalDateTimeToSystemTime ; Win 7
@ stdcall ConvertDefaultLocale (long)
@ stdcall ConvertFiberToThread()
;@ stdcall ConvertNLSDayOfWeekToWin32DayOfWeek ; Win 7
;@ stdcall ConvertSystemTimeToCalDateTime ; Win 7
@ stdcall ConvertThreadToFiber(ptr)
@ stdcall ConvertThreadToFiberEx(ptr long)
;@ stdcall CopyExtendedContext ; Win 7
@ stdcall CopyFileA(str str long)
@ stdcall CopyFileExA (str str ptr ptr ptr long)
@ stdcall CopyFileExW (wstr wstr ptr ptr ptr long)
;@ stdcall CopyFileTransactedA ; Win 7
;@ stdcall CopyFileTransactedW ; Win 7
@ stdcall CopyFileW(wstr wstr long)
@ stdcall CopyLZFile(long long) LZCopy
@ stdcall CreateActCtxA(ptr)
@ stdcall CreateActCtxW(ptr)
;@ stdcall CreateBoundaryDescriptorA ; Win 7
;@ stdcall CreateBoundaryDescriptorW ; Win 7
@ stdcall CreateConsoleScreenBuffer(long long ptr long ptr)
@ stdcall CreateDirectoryA(str ptr)
@ stdcall CreateDirectoryExA(str str ptr)
@ stdcall CreateDirectoryExW(wstr wstr ptr)
;@ stdcall CreateDirectoryTransactedA ; Win 7
;@ stdcall CreateDirectoryTransactedW ; Win 7
@ stdcall CreateDirectoryW(wstr ptr)
@ stdcall CreateEventA(ptr long long str)
@ stdcall CreateEventExA(ptr str long long)
@ stdcall CreateEventExW(ptr wstr long long)
@ stdcall CreateEventW(ptr long long wstr)
@ stdcall CreateFiber(long ptr ptr)
@ stdcall CreateFiberEx(long long long ptr ptr)
@ stdcall CreateFileA(str long long ptr long long long)
@ stdcall CreateFileMappingA(long ptr long long long str)
;@ stdcall CreateFileMappingNumaA ; Win 7
;@ stdcall CreateFileMappingNumaW ; Win 7
@ stdcall CreateFileMappingW(long ptr long long long wstr)
;@ stdcall CreateFileTransactedA ; Win 7
;@ stdcall CreateFileTransactedW ; Win 7
@ stdcall CreateFileW(wstr long long ptr long long long)
@ stdcall CreateHardLinkA(str str ptr)
;@ stdcall CreateHardLinkTransactedA ; Win 7
;@ stdcall CreateHardLinkTransactedW ; Win 7
@ stdcall CreateHardLinkW(wstr wstr ptr)
@ stdcall CreateIoCompletionPort(long long long long)
@ stdcall CreateJobObjectA(ptr str)
@ stdcall CreateJobObjectW(ptr wstr)
@ stdcall CreateJobSet(long ptr long)
;@ stub CreateKernelThread ; missing in XP SP3 and Win 7
@ stdcall CreateMailslotA(ptr long long ptr)
@ stdcall CreateMailslotW(ptr long long ptr)
@ stdcall CreateMemoryResourceNotification(long)
@ stdcall CreateMutexA(ptr long str)
@ stdcall CreateMutexExA(ptr str long long)
@ stdcall CreateMutexExW(ptr wstr long long)
@ stdcall CreateMutexW(ptr long wstr)
@ stdcall CreateNamedPipeA(str long long long long long long ptr)
@ stdcall CreateNamedPipeW(wstr long long long long long long ptr)
@ stdcall CreateNlsSecurityDescriptor(ptr long long) ; missing in Win 7
@ stdcall CreatePipe(ptr ptr ptr long)
;@ stdcall CreatePrivateNamespaceA ; Win 7
;@ stdcall CreatePrivateNamespaceW ; Win 7
@ stdcall CreateProcessA(str str ptr ptr long long ptr str ptr ptr)
;@ stdcall CreateProcessAsUserW ; Win 7
@ stdcall CreateProcessInternalA(ptr str str ptr ptr long long ptr str ptr ptr long)
@ stdcall CreateProcessInternalW(ptr wstr wstr ptr ptr long long ptr wstr ptr ptr long)
@ stdcall CreateProcessInternalWSecure() ; missing in Win 7
@ stdcall CreateProcessW(wstr wstr ptr ptr long long ptr wstr ptr ptr)
@ stdcall CreateRemoteThread(long ptr long ptr long long ptr)
;@ stdcall CreateRemoteThreadEx api-ms-win-core-processthreads-l1-1-0.CreateRemoteThreadEx ; Win 7
@ stdcall CreateSemaphoreA(ptr long long str)
@ stdcall CreateSemaphoreExA(ptr long long str long long)
@ stdcall CreateSemaphoreExW(ptr long long wstr long long)
@ stdcall CreateSemaphoreW(ptr long long wstr)
@ stdcall CreateSocketHandle()
@ stdcall CreateSymbolicLinkA(str str long)
;@ stdcall CreateSymbolicLinkTransactedA ; Win 7
;@ stdcall CreateSymbolicLinkTransactedW ; Win 7
@ stdcall CreateSymbolicLinkW(wstr wstr long)
@ stdcall CreateTapePartition(long long long long)
@ stdcall CreateThread(ptr long ptr long long ptr)
;@ stdcall CreateThreadpool ; Win 7
;@ stdcall CreateThreadpoolCleanupGroup ; Win 7
;@ stdcall CreateThreadpoolIo ; Win 7
;@ stdcall CreateThreadpoolTimer ; Win 7
;@ stdcall CreateThreadpoolWait ; Win 7
;@ stdcall CreateThreadpoolWork ; Win 7
@ stdcall CreateTimerQueue ()
@ stdcall CreateTimerQueueTimer(ptr long ptr ptr long long long)
@ stdcall CreateToolhelp32Snapshot(long long)
;@ stdcall arch=x86_64 CreateUmsCompletionList
;@ stdcall arch=x86_64 CreateUmsThreadContext
@ stdcall CreateVirtualBuffer(long long long) ; missing in Win 7
@ stdcall CreateWaitableTimerA(ptr long str)
@ stdcall CreateWaitableTimerExA(ptr str long long)
@ stdcall CreateWaitableTimerExW(ptr wstr long long)
@ stdcall CreateWaitableTimerW(ptr long wstr)
@ stdcall DeactivateActCtx(long ptr)
@ stdcall DebugActiveProcess(long)
@ stdcall DebugActiveProcessStop(long)
@ stdcall DebugBreak() ntdll.DbgBreakPoint
@ stdcall DebugBreakProcess(long)
@ stdcall DebugSetProcessKillOnExit(long)
@ stdcall DecodePointer(ptr) ntdll.RtlDecodePointer
@ stdcall DecodeSystemPointer(ptr) ntdll.RtlDecodeSystemPointer
@ stdcall DefineDosDeviceA(long str str)
@ stdcall DefineDosDeviceW(long wstr wstr)
@ stdcall DelayLoadFailureHook(str str)
@ stdcall DeleteAtom(long)
;@ stdcall DeleteBoundaryDescriptor ntdll.RtlDeleteBoundaryDescriptor ; Win 7
@ stdcall DeleteCriticalSection(ptr) ntdll.RtlDeleteCriticalSection
@ stdcall DeleteFiber(ptr)
@ stdcall DeleteFileA(str)
;@ stdcall DeleteFileTransactedA ; Win 7
;@ stdcall DeleteFileTransactedW ; Win 7
@ stdcall DeleteFileW(wstr)
;@ stdcall DeleteProcThreadAttributeList api-ms-win-core-processthreads-l1-1-0.DeleteProcThreadAttributeList ; Win 7
@ stdcall DeleteTimerQueue(long)
@ stdcall DeleteTimerQueueEx (long long)
@ stdcall DeleteTimerQueueTimer(long long long)
;@ stdcall -arch=x86_64 DeleteUmsCompletionList
;@ stdcall -arch=x86_64 DeleteUmsThreadContext
@ stdcall DeleteVolumeMountPointA(str) ;check
@ stdcall DeleteVolumeMountPointW(wstr) ;check
;@ stdcall -arch=x86_64 DequeueUmsCompletionListItems
@ stdcall DeviceIoControl(long long ptr long ptr long ptr ptr)
@ stdcall DisableThreadLibraryCalls(long)
;@ stdcall DisableThreadProfiling ; Win 7
;@ stdcall DisassociateCurrentThreadFromCallback ntdll.TpDisassociateCallback ; Win 7
@ stdcall DisconnectNamedPipe(long)
@ stdcall DnsHostnameToComputerNameA (str ptr ptr)
@ stdcall DnsHostnameToComputerNameW (wstr ptr ptr)
@ stdcall DosDateTimeToFileTime(long long ptr)
@ stdcall DosPathToSessionPathA(long str str)
@ stdcall DosPathToSessionPathW(long wstr wstr)
@ stdcall DuplicateConsoleHandle(long long long long)
@ stdcall DuplicateHandle(long long long ptr long long long)
;@ stdcall EnableThreadProfiling ; Win 7
@ stdcall EncodePointer(ptr) ntdll.RtlEncodePointer
@ stdcall EncodeSystemPointer(ptr) ntdll.RtlEncodeSystemPointer
@ stdcall EndUpdateResourceA(long long)
@ stdcall EndUpdateResourceW(long long)
@ stdcall EnterCriticalSection(ptr) ntdll.RtlEnterCriticalSection
;@ stdcall -arch=x86_64 EnterUmsSchedulingMode
@ stdcall EnumCalendarInfoA(ptr long long long)
@ stdcall EnumCalendarInfoExA(ptr long long long)
;@ stdcall EnumCalendarInfoExEx ; Win 7
@ stdcall EnumCalendarInfoExW(ptr long long long)
@ stdcall EnumCalendarInfoW(ptr long long long)
@ stdcall EnumDateFormatsA(ptr long long)
@ stdcall EnumDateFormatsExA(ptr long long)
;@ stdcall EnumDateFormatsExEx ; Win 7
@ stdcall EnumDateFormatsExW(ptr long long)
@ stdcall EnumDateFormatsW(ptr long long)
@ stdcall EnumLanguageGroupLocalesA(ptr long long ptr)
@ stdcall EnumLanguageGroupLocalesW(ptr long long ptr)
@ stdcall EnumResourceLanguagesA(long str str ptr long)
;@ stdcall EnumResourceLanguagesExA ; Win 7
;@ stdcall EnumResourceLanguagesExW ; Win 7
@ stdcall EnumResourceLanguagesW(long wstr wstr ptr long)
@ stdcall EnumResourceNamesA(long str ptr long)
;@ stdcall EnumResourceNamesExA ; Win 7
;@ stdcall EnumResourceNamesExW ; Win 7
@ stdcall EnumResourceNamesW(long wstr ptr long)
@ stdcall EnumResourceTypesA(long ptr long)
;@ stdcall EnumResourceTypesExA ; Win 7
;@ stdcall EnumResourceTypesExW ; Win 7
@ stdcall EnumResourceTypesW(long ptr long)
@ stdcall EnumSystemCodePagesA(ptr long)
@ stdcall EnumSystemCodePagesW(ptr long)
;@ stdcall EnumSystemFirmwareTables ; Win 7
@ stdcall EnumSystemGeoID(long long ptr)
@ stdcall EnumSystemLanguageGroupsA(ptr long ptr)
@ stdcall EnumSystemLanguageGroupsW(ptr long ptr)
@ stdcall EnumSystemLocalesA(ptr long)
;@ stdcall EnumSystemLocalesEx ; Win 7
@ stdcall EnumSystemLocalesW(ptr long)
@ stdcall EnumTimeFormatsA(ptr long long)
;@ stdcall EnumTimeFormatsEx ; Win 7
@ stdcall EnumTimeFormatsW(ptr long long)
@ stdcall EnumUILanguagesA(ptr long long)
@ stdcall EnumUILanguagesW(ptr long long)
@ stdcall EnumerateLocalComputerNamesA(ptr long str ptr)
@ stdcall EnumerateLocalComputerNamesW(ptr long wstr ptr)
@ stdcall EraseTape(ptr long long)
@ stdcall EscapeCommFunction(long long)
@ stdcall ExitProcess(long) ; FIXME: ntdll.RtlExitUserProcess
@ stdcall ExitThread(long) ; FIXME: ntdll.RtlExitUserThread
@ stdcall ExitVDM(long long)
@ stdcall ExpandEnvironmentStringsA(str ptr long)
@ stdcall ExpandEnvironmentStringsW(wstr ptr long)
@ stdcall ExpungeConsoleCommandHistoryA(long)
@ stdcall ExpungeConsoleCommandHistoryW(long)
@ stdcall ExtendVirtualBuffer(long long) ; missing in Win 7
@ stdcall FatalAppExitA(long str)
@ stdcall FatalAppExitW(long wstr)
@ stdcall FatalExit(long)
@ stdcall FileTimeToDosDateTime(ptr ptr ptr)
@ stdcall FileTimeToLocalFileTime(ptr ptr)
@ stdcall FileTimeToSystemTime(ptr ptr)
@ stdcall FillConsoleOutputAttribute(long long long long ptr)
@ stdcall FillConsoleOutputCharacterA(long long long long ptr)
@ stdcall FillConsoleOutputCharacterW(long long long long ptr)
@ stdcall FindActCtxSectionGuid(long ptr long ptr ptr)
@ stdcall FindActCtxSectionStringA(long ptr long str ptr)
@ stdcall FindActCtxSectionStringW(long ptr long wstr ptr)
@ stdcall FindAtomA(str)
@ stdcall FindAtomW(wstr)
@ stdcall FindClose(long)
@ stdcall FindCloseChangeNotification(long)
@ stdcall FindFirstChangeNotificationA(str long long)
@ stdcall FindFirstChangeNotificationW(wstr long long)
@ stdcall FindFirstFileA(str ptr)
@ stdcall FindFirstFileExA(str long ptr long ptr long)
@ stdcall FindFirstFileExW(wstr long ptr long ptr long)
;@ stdcall FindFirstFileNameTransactedW ; Win 7
;@ stdcall FindFirstFileNameW ; Win 7
;@ stdcall FindFirstFileTransactedA ; Win 7
;@ stdcall FindFirstFileTransactedW ; Win 7
@ stdcall FindFirstFileW(wstr ptr)
;@ stdcall FindFirstStreamTransactedW ; Win 7
@ stdcall FindFirstStreamW(wstr ptr ptr long)
@ stdcall FindFirstVolumeA(ptr long)
@ stdcall FindFirstVolumeMountPointA(str ptr long)
@ stdcall FindFirstVolumeMountPointW(wstr ptr long)
@ stdcall FindFirstVolumeW(ptr long)
;@ stdcall FindNLSString ; Win 7
;@ stdcall FindNLSStringEx ; Win 7
@ stdcall FindNextChangeNotification(long)
@ stdcall FindNextFileA(long ptr)
;@ stdcall FindNextFileNameW ; Win 7
@ stdcall FindNextFileW(long ptr)
;@ stdcall FindNextStreamW ; Win 7
@ stdcall FindNextVolumeA(long ptr long)
@ stdcall FindNextVolumeMountPointA(long str long)
@ stdcall FindNextVolumeMountPointW(long wstr long)
@ stdcall FindNextVolumeW(long ptr long)
@ stdcall FindResourceA(long str str)
@ stdcall FindResourceExA(long str str long)
@ stdcall FindResourceExW(long wstr wstr long)
@ stdcall FindResourceW(long wstr wstr)
;@ stdcall FindStringOrdinal ; Win 7
@ stdcall FindVolumeClose(ptr)
@ stdcall FindVolumeMountPointClose(ptr)
;@ stdcall FlsAlloc(ptr) ; missing in XP SP3
;@ stdcall FlsFree(long) ; missing in XP SP3
;@ stdcall FlsGetValue(long) ; missing in XP SP3
;@ stdcall FlsSetValue(long ptr) ; missing in XP SP3
@ stdcall FlushConsoleInputBuffer(long)
@ stdcall FlushFileBuffers(long)
@ stdcall FlushInstructionCache(long long long)
;@ stdcall FlushProcessWriteBuffers ntdll.NtFlushProcessWriteBuffers ; Win 7
@ stdcall FlushViewOfFile(ptr long)
@ stdcall FoldStringA(long str long ptr long)
@ stdcall FoldStringW(long wstr long ptr long)
@ stdcall FormatMessageA(long ptr long long ptr long ptr)
@ stdcall FormatMessageW(long ptr long long ptr long ptr)
@ stdcall FreeConsole()
@ stdcall FreeEnvironmentStringsA(ptr)
@ stdcall FreeEnvironmentStringsW(ptr)
@ stdcall FreeLibrary(long)
@ stdcall FreeLibraryAndExitThread(long long)
;@ stdcall FreeLibraryWhenCallbackReturns ntdll.TpCallbackUnloadDllOnCompletion ; Win 7
@ stdcall FreeResource(long)
@ stdcall FreeUserPhysicalPages(long long long)
@ stdcall FreeVirtualBuffer(ptr) ; missing in Win 7
@ stdcall GenerateConsoleCtrlEvent(long long)
@ stdcall GetACP()
;@ stdcall GetActiveProcessorCount ; Win 7
;@ stdcall GetActiveProcessorGroupCount ; Win 7
;@ stdcall GetApplicationRecoveryCallback ; Win 7
;@ stdcall GetApplicationRestartSettings ; Win 7
@ stdcall GetAtomNameA(long ptr long)
@ stdcall GetAtomNameW(long ptr long)
@ stdcall GetBinaryType(str ptr) GetBinaryTypeA
@ stdcall GetBinaryTypeA(str ptr)
@ stdcall GetBinaryTypeW(wstr ptr)
@ stdcall GetCPFileNameFromRegistry(long wstr long) ;check missing in Win 7
@ stdcall GetCPInfo(long ptr)
@ stdcall GetCPInfoExA(long long ptr)
@ stdcall GetCPInfoExW(long long ptr)
;@ stdcall GetCalendarDateFormat ; Win 7
;@ stdcall GetCalendarDateFormatEx ; Win 7
;@ stdcall GetCalendarDaysInMonth ; Win 7
;@ stdcall GetCalendarDifferenceInDays ; Win 7
@ stdcall GetCalendarInfoA(long long long ptr long ptr)
;@ stdcall GetCalendarInfoEx ; Win 7
@ stdcall GetCalendarInfoW(long long long ptr long ptr)
;@ stdcall GetCalendarMonthsInYear ; Win 7
;@ stdcall GetCalendarSupportedDateRange ; Win 7
;@ stdcall GetCalendarWeekNumber ; Win 7
@ stdcall GetComPlusPackageInstallStatus()
@ stdcall GetCommConfig(long ptr long)
@ stdcall GetCommMask(long ptr)
@ stdcall GetCommModemStatus(long ptr)
@ stdcall GetCommProperties(long ptr)
@ stdcall GetCommState(long ptr)
@ stdcall GetCommTimeouts(long ptr)
@ stdcall GetCommandLineA()
@ stdcall GetCommandLineW()
@ stdcall GetCompressedFileSizeA(long ptr)
;@ stdcall GetCompressedFileSizeTransactedA ; Win 7
;@ stdcall GetCompressedFileSizeTransactedW ; Win 7
@ stdcall GetCompressedFileSizeW(long ptr)
@ stdcall GetComputerNameA(ptr ptr)
@ stdcall GetComputerNameExA(long ptr ptr)
@ stdcall GetComputerNameExW(long ptr ptr)
@ stdcall GetComputerNameW(ptr ptr)
@ stdcall GetConsoleAliasA(str str long str)
@ stdcall GetConsoleAliasExesA(str long)
@ stdcall GetConsoleAliasExesLengthA()
@ stdcall GetConsoleAliasExesLengthW()
@ stdcall GetConsoleAliasExesW(wstr long)
@ stdcall GetConsoleAliasW(wstr ptr long wstr)
@ stdcall GetConsoleAliasesA(str long str)
@ stdcall GetConsoleAliasesLengthA(str)
@ stdcall GetConsoleAliasesLengthW(wstr)
@ stdcall GetConsoleAliasesW(wstr long wstr)
@ stdcall GetConsoleCP()
@ stdcall GetConsoleCharType(long long ptr)
@ stdcall GetConsoleCommandHistoryA(long long long)
@ stdcall GetConsoleCommandHistoryLengthA(long)
@ stdcall GetConsoleCommandHistoryLengthW(long)
@ stdcall GetConsoleCommandHistoryW(long long long)
@ stdcall GetConsoleCursorInfo(long ptr)
@ stdcall GetConsoleCursorMode(long ptr ptr)
@ stdcall GetConsoleDisplayMode(ptr)
@ stdcall GetConsoleFontInfo(long long long ptr)
@ stdcall GetConsoleFontSize(long long)
@ stdcall GetConsoleHardwareState(long long ptr)
@ stdcall GetConsoleHistoryInfo(ptr)
@ stdcall GetConsoleInputExeNameA(long ptr)
@ stdcall GetConsoleInputExeNameW(long ptr)
@ stdcall GetConsoleInputWaitHandle()
@ stdcall GetConsoleKeyboardLayoutNameA(ptr)
@ stdcall GetConsoleKeyboardLayoutNameW(ptr)
@ stdcall GetConsoleMode(long ptr)
@ stdcall GetConsoleNlsMode(long ptr)
;@ stdcall GetConsoleOriginalTitleA ; Win 7
;@ stdcall GetConsoleOriginalTitleW ; Win 7
@ stdcall GetConsoleOutputCP()
@ stdcall GetConsoleProcessList(ptr long) ; missing in XP SP3
@ stdcall GetConsoleScreenBufferInfo(long ptr)
;@ stdcall GetConsoleScreenBufferInfoEx ; Win 7
@ stdcall GetConsoleSelectionInfo(ptr)
@ stdcall GetConsoleTitleA(ptr long)
@ stdcall GetConsoleTitleW(ptr long)
@ stdcall GetConsoleWindow()
@ stdcall GetCurrencyFormatA(long long str ptr str long)
;@ stdcall GetCurrencyFormatEx ; Win 7
@ stdcall GetCurrencyFormatW(long long str ptr str long)
@ stdcall GetCurrentActCtx(ptr)
@ stdcall GetCurrentConsoleFont(long long ptr)
;@ stdcall GetCurrentConsoleFontEx ; Win 7
@ stdcall GetCurrentDirectoryA(long ptr)
@ stdcall GetCurrentDirectoryW(long ptr)
@ stdcall GetCurrentProcess()
@ stdcall GetCurrentProcessId()
@ stdcall GetCurrentProcessorNumber() ntdll.RtlGetCurrentProcessorNumber
;@ stdcall GetCurrentProcessorNumberEx ntdll.RtlGetCurrentProcessorNumberEx ; Win 7
@ stdcall GetCurrentThread()
@ stdcall GetCurrentThreadId()
;@ stdcall GetCurrentUmsThread
@ stdcall GetDateFormatA(long long ptr str ptr long)
;@ stdcall GetDateFormatEx ; Win 7
@ stdcall GetDateFormatW(long long ptr wstr ptr long)
;@ stub GetDaylightFlag ; missing in XP SP3 and Win 7
@ stdcall GetDefaultCommConfigA(str ptr long)
@ stdcall GetDefaultCommConfigW(wstr ptr long)
@ stdcall GetDefaultSortkeySize(ptr) ; missing in Win 7
@ stdcall GetDevicePowerState(long ptr)
@ stdcall GetDiskFreeSpaceA(str ptr ptr ptr ptr)
@ stdcall GetDiskFreeSpaceExA (str ptr ptr ptr)
@ stdcall GetDiskFreeSpaceExW (wstr ptr ptr ptr)
@ stdcall GetDiskFreeSpaceW(wstr ptr ptr ptr ptr)
@ stdcall GetDllDirectoryA(long ptr)
@ stdcall GetDllDirectoryW(long ptr)
@ stdcall GetDriveTypeA(str)
@ stdcall GetDriveTypeW(wstr)
;@ stdcall GetDurationFormat ; Win 7
;@ stdcall GetDurationFormatEx ; Win 7
;@ stdcall GetDynamicTimeZoneInformation ; Win 7
;@ stdcall GetEnabledExtendedFeatures api-ms-win-core-xstate-l1-1-0.RtlGetEnabledExtendedFeatures ; Win 7
@ stdcall GetEnvironmentStrings()
@ stdcall GetEnvironmentStringsA() GetEnvironmentStrings
@ stdcall GetEnvironmentStringsW()
@ stdcall GetEnvironmentVariableA(str ptr long)
@ stdcall GetEnvironmentVariableW(wstr ptr long)
;@ stdcall GetEraNameCountedString ; Win 7
@ stdcall GetErrorMode()
@ stdcall GetExitCodeProcess(long ptr)
@ stdcall GetExitCodeThread(long ptr)
@ stdcall GetExpandedNameA(str ptr)
@ stdcall GetExpandedNameW(wstr ptr)
;@ stdcall GetExtendedContextLength ; Win 7
;@ stdcall GetExtendedFeaturesMask api-ms-win-core-xstate-l1-1-0.RtlGetExtendedFeaturesMask ; Win 7
@ stdcall GetFileAttributesA(str)
@ stdcall GetFileAttributesByHandle(long ptr long) ; missing in Win 7
@ stdcall GetFileAttributesExA(str long ptr)
@ stdcall GetFileAttributesExW(wstr long ptr)
;@ stdcall GetFileAttributesTransactedA ; Win 7
;@ stdcall GetFileAttributesTransactedW ; Win 7
@ stdcall GetFileAttributesW(wstr)
@ stdcall GetFileBandwidthReservation(long ptr ptr ptr ptr ptr)
@ stdcall GetFileInformationByHandle(long ptr)
;@ stdcall GetFileInformationByHandleEx ; Win 7
;@ stdcall GetFileMUIInfo ; Win 7
;@ stdcall GetFileMUIPath ; Win 7
@ stdcall GetFileSize(long ptr)
@ stdcall GetFileSizeEx(long ptr)
@ stdcall GetFileTime(long ptr ptr ptr)
@ stdcall GetFileType(long)
@ stdcall GetFinalPathNameByHandleA(long str long long)
@ stdcall GetFinalPathNameByHandleW(long wstr long long)
@ stdcall GetFirmwareEnvironmentVariableA(str str ptr long)
@ stdcall GetFirmwareEnvironmentVariableW(wstr wstr ptr long)
@ stdcall GetFullPathNameA(str long ptr ptr)
;@ stdcall GetFullPathNameTransactedA ; Win 7
;@ stdcall GetFullPathNameTransactedW ; Win 7
@ stdcall GetFullPathNameW(wstr long ptr ptr)
@ stdcall GetGeoInfoA(long long ptr long long)
@ stdcall GetGeoInfoW(long long ptr long long)
@ stdcall GetHandleContext(long) ; missing on x64
@ stdcall GetHandleInformation(long ptr)
;@ stub GetSCallbackTarget ; missing in XP SP3 and Win 7
;@ stub GetSCallbackTemplate ; missing in XP SP3 and Win 7
@ stdcall GetLargePageMinimum()
@ stdcall GetLargestConsoleWindowSize(long)
@ stdcall GetLastError() ntdll.RtlGetLastWin32Error
@ stdcall GetLinguistLangSize(ptr) ; missing in Win 7
@ stdcall GetLocalTime(ptr)
@ stdcall GetLocaleInfoA(long long ptr long)
@ stdcall GetLocaleInfoEx(wstr long wstr long) ; Vista+
@ stdcall GetLocaleInfoW(long long ptr long)
@ stdcall GetLogicalDriveStringsA(long ptr)
@ stdcall GetLogicalDriveStringsW(long ptr)
@ stdcall GetLogicalDrives()
@ stdcall GetLogicalProcessorInformation(ptr ptr)
;@ stdcall GetLogicalProcessorInformationEx api-ms-win-core-sysinfo-l1-1-0.GetLogicalProcessorInformationEx ; Win 7
@ stdcall GetLongPathNameA (str long long)
;@ stdcall GetLongPathNameTransactedA ; Win 7
;@ stdcall GetLongPathNameTransactedW ; Win 7
@ stdcall GetLongPathNameW (wstr long long)
@ stdcall GetMailslotInfo(long ptr ptr ptr ptr)
;@ stdcall GetMaximumProcessorCount ; Win 7
;@ stdcall GetMaximumProcessorGroupCount ; Win 7
@ stdcall GetModuleFileNameA(long ptr long)
@ stdcall GetModuleFileNameW(long ptr long)
@ stdcall GetModuleHandleA(str)
@ stdcall GetModuleHandleExA(long ptr ptr)
@ stdcall GetModuleHandleExW(long ptr ptr)
@ stdcall GetModuleHandleW(wstr)
;@ stdcall GetNLSVersion ; Win 7
;@ stdcall GetNLSVersionEx ; Win 7
;@ stdcall GetNamedPipeAttribute ; Win 7
;@ stdcall GetNamedPipeClientComputerNameA ; Win 7
;@ stdcall GetNamedPipeClientComputerNameW ; Win 7
;@ stdcall GetNamedPipeClientProcessId ; Win 7
;@ stdcall GetNamedPipeClientSessionId ; Win 7
@ stdcall GetNamedPipeHandleStateA(long ptr ptr ptr ptr str long)
@ stdcall GetNamedPipeHandleStateW(long ptr ptr ptr ptr wstr long)
@ stdcall GetNamedPipeInfo(long ptr ptr ptr ptr)
;@ stdcall GetNamedPipeServerProcessId ; Win 7
;@ stdcall GetNamedPipeServerSessionId ; Win 7
@ stdcall GetNativeSystemInfo(ptr)
;@ stdcall -arch=x86_64 GetNextUmsListItem
@ stdcall GetNextVDMCommand(long)
@ stdcall GetNlsSectionName(long long long str str long) ; missing in Win 7
@ stdcall GetNumaAvailableMemory(ptr long ptr) ; missing in Win 7
@ stdcall GetNumaAvailableMemoryNode(long ptr)
;@ stdcall GetNumaAvailableMemoryNodeEx ; Win 7
@ stdcall GetNumaHighestNodeNumber(ptr)
;@ stdcall GetNumaNodeNumberFromHandle ; Win 7
@ stdcall GetNumaNodeProcessorMask(long ptr)
;@ stdcall GetNumaNodeProcessorMaskEx ; Win 7
@ stdcall GetNumaProcessorMap(ptr long ptr) ; missing in Win 7
@ stdcall GetNumaProcessorNode(long ptr)
;@ stdcall GetNumaProcessorNodeEx ; Win 7
;@ stdcall GetNumaProximityNode ; Win 7
;@ stdcall GetNumaProximityNodeEx ; Win 7
@ stdcall GetNumberFormatA(long long str ptr ptr long)
;@ stdcall GetNumberFormatEx ; Win 7
@ stdcall GetNumberFormatW(long long wstr ptr ptr long)
@ stdcall GetNumberOfConsoleFonts()
@ stdcall GetNumberOfConsoleInputEvents(long ptr)
@ stdcall GetNumberOfConsoleMouseButtons(ptr)
@ stdcall GetOEMCP()
@ stdcall GetOverlappedResult(long ptr ptr long)
;@ stdcall GetPhysicallyInstalledSystemMemory ; Win 7
@ stdcall GetPriorityClass(long)
@ stdcall GetPrivateProfileIntA(str str long str)
@ stdcall GetPrivateProfileIntW(wstr wstr long wstr)
@ stdcall GetPrivateProfileSectionA(str ptr long str)
@ stdcall GetPrivateProfileSectionNamesA(ptr long str)
@ stdcall GetPrivateProfileSectionNamesW(ptr long wstr)
@ stdcall GetPrivateProfileSectionW(wstr ptr long wstr)
@ stdcall GetPrivateProfileStringA(str str str ptr long str)
@ stdcall GetPrivateProfileStringW(wstr wstr wstr ptr long wstr)
@ stdcall GetPrivateProfileStructA (str str ptr long str)
@ stdcall GetPrivateProfileStructW(wstr wstr ptr long wstr)
@ stdcall GetProcAddress(long str)
@ stdcall GetProcessAffinityMask(long ptr ptr)
;@ stdcall GetProcessFlags(long)
;@ stdcall GetProcessDEPPolicy ; Win 7
;@ stdcall GetProcessGroupAffinity ; Win 7
@ stdcall GetProcessHandleCount(long ptr)
@ stdcall GetProcessHeap()
@ stdcall GetProcessHeaps(long ptr)
@ stdcall GetProcessId(long)
;@ stdcall GetProcessIdOfThread ; Win 7
@ stdcall GetProcessIoCounters(long ptr)
;@ stdcall GetProcessPreferredUILanguages ; Win 7
@ stdcall GetProcessPriorityBoost(long ptr)
@ stdcall GetProcessShutdownParameters(ptr ptr)
@ stdcall GetProcessTimes(long ptr ptr ptr ptr)
@ stdcall GetProcessVersion(long)
@ stdcall GetProcessWorkingSetSize(long ptr ptr)
;@ stdcall GetProcessWorkingSetSizeEx ; Win 7
;@ stdcall GetProcessorSystemCycleTime ; Win 7
;@ stdcall GetProductInfo(long long long long ptr) ; Win 7
;@ stub GetProductName
@ stdcall GetProfileIntA(str str long)
@ stdcall GetProfileIntW(wstr wstr long)
@ stdcall GetProfileSectionA(str ptr long)
@ stdcall GetProfileSectionW(wstr ptr long)
@ stdcall GetProfileStringA(str str str ptr long)
@ stdcall GetProfileStringW(wstr wstr wstr ptr long)
@ stdcall GetQueuedCompletionStatus(long ptr ptr ptr long)
;@ stdcall GetQueuedCompletionStatusEx ; Win 7
;@ stub GetLSCallbackTarget ; missing in XP SP3 and Win 7
;@ stub GetLSCallbackTemplate ; missing in XP SP3 and Win 7
@ stdcall GetShortPathNameA(str ptr long)
@ stdcall GetShortPathNameW(wstr ptr long)
@ stdcall GetStartupInfoA(ptr)
@ stdcall GetStartupInfoW(ptr)
@ stdcall GetStdHandle(long)
;@ stdcall GetStringScripts ; Win 7
@ stdcall GetStringTypeA(long long str long ptr)
@ stdcall GetStringTypeExA(long long str long ptr)
@ stdcall GetStringTypeExW(long long wstr long ptr)
@ stdcall GetStringTypeW(long wstr long ptr)
;@ stdcall GetSystemDEPPolicy ; Win 7
@ stdcall GetSystemDefaultLCID()
@ stdcall GetSystemDefaultLangID()
;@ stdcall GetSystemDefaultLocaleName ; Win 7
@ stdcall GetSystemDefaultUILanguage()
@ stdcall GetSystemDirectoryA(ptr long)
@ stdcall GetSystemDirectoryW(ptr long)
;@ stdcall GetSystemFileCacheSize ; Win 7
;@ stdcall GetSystemFirmwareTable ; Win 7
@ stdcall GetSystemInfo(ptr)
@ stdcall GetSystemPowerStatus(ptr)
;@ stdcall GetSystemPreferredUILanguages ; Win 7
@ stdcall GetSystemRegistryQuota(ptr ptr)
@ stdcall GetSystemTime(ptr)
@ stdcall GetSystemTimeAdjustment(ptr ptr ptr)
@ stdcall GetSystemTimeAsFileTime(ptr)
@ stdcall GetSystemTimes(ptr ptr ptr)
@ stdcall GetSystemWindowsDirectoryA(ptr long)
@ stdcall GetSystemWindowsDirectoryW(ptr long)
@ stdcall GetSystemWow64DirectoryA(ptr long)
@ stdcall GetSystemWow64DirectoryW(ptr long)
@ stdcall GetTapeParameters(ptr long ptr ptr)
@ stdcall GetTapePosition(ptr long ptr ptr ptr)
@ stdcall GetTapeStatus(ptr)
@ stdcall GetTempFileNameA(str str long ptr)
@ stdcall GetTempFileNameW(wstr wstr long ptr)
@ stdcall GetTempPathA(long ptr)
@ stdcall GetTempPathW(long ptr)
@ stdcall GetThreadContext(long ptr)
;@ stdcall GetThreadErrorMode() ; Win 7
;@ stdcall GetThreadGroupAffinity ; Win 7
@ stdcall GetThreadIOPendingFlag(long ptr)
@ stdcall GetThreadId(ptr)
;@ stdcall GetThreadIdealProcessorEx ; Win 7
@ stdcall GetThreadLocale()
;@ stdcall GetThreadPreferredUILanguages ; Win 7
@ stdcall GetThreadPriority(long)
@ stdcall GetThreadPriorityBoost(long ptr)
@ stdcall GetThreadSelectorEntry(long long ptr)
@ stdcall GetThreadTimes(long ptr ptr ptr ptr)
;@ stdcall GetThreadUILanguage ; Win 7
@ stdcall GetTickCount()
@ stdcall -ret64 GetTickCount64()
@ stdcall GetTimeFormatA(long long ptr str ptr long)
;@ stdcall GetTimeFormatEx ; Win 7
@ stdcall GetTimeFormatW(long long ptr wstr ptr long)
@ stdcall GetTimeZoneInformation(ptr)
;@ stdcall GetTimeZoneInformationForYear ; Win 7
;@ stdcall GetUILanguageInfo ; Win 7
;@ stdcall -arch=x86_64 GetUmsCompletionListEvent
@ stdcall GetUserDefaultLCID()
@ stdcall GetUserDefaultLangID()
;@ stdcall GetUserDefaultLocaleName ; Win 7
@ stdcall GetUserDefaultUILanguage()
@ stdcall GetUserGeoID(long)
;@ stdcall GetUserPreferredUILanguages ; Win 7
@ stdcall GetVDMCurrentDirectories(long long)
@ stdcall GetVersion()
@ stdcall GetVersionExA(ptr)
@ stdcall GetVersionExW(ptr)
@ stdcall GetVolumeInformationA(str ptr long ptr ptr ptr ptr long)
;@ stdcall GetVolumeInformationByHandleW ; Win 7
@ stdcall GetVolumeInformationW(wstr ptr long ptr ptr ptr ptr long)
@ stdcall GetVolumeNameForVolumeMountPointA(str ptr long)
@ stdcall GetVolumeNameForVolumeMountPointW(wstr ptr long)
@ stdcall GetVolumePathNameA(str ptr long)
@ stdcall GetVolumePathNameW(wstr ptr long)
@ stdcall GetVolumePathNamesForVolumeNameA(str str long ptr)
@ stdcall GetVolumePathNamesForVolumeNameW(wstr wstr long ptr)
@ stdcall GetWindowsDirectoryA(ptr long)
@ stdcall GetWindowsDirectoryW(ptr long)
@ stdcall GetWriteWatch(long ptr long ptr ptr ptr)
@ stdcall GlobalAddAtomA(str)
@ stdcall GlobalAddAtomW(wstr)
@ stdcall GlobalAlloc(long long)
@ stdcall GlobalCompact(long)
@ stdcall GlobalDeleteAtom(long)
@ stdcall GlobalFindAtomA(str)
@ stdcall GlobalFindAtomW(wstr)
@ stdcall GlobalFix(long)
@ stdcall GlobalFlags(long)
@ stdcall GlobalFree(long)
@ stdcall GlobalGetAtomNameA(long ptr long)
@ stdcall GlobalGetAtomNameW(long ptr long)
@ stdcall GlobalHandle(ptr)
@ stdcall GlobalLock(long)
@ stdcall GlobalMemoryStatus(ptr)
@ stdcall GlobalMemoryStatusEx(ptr)
@ stdcall GlobalReAlloc(long long long)
@ stdcall GlobalSize(long)
@ stdcall GlobalUnWire(long)
@ stdcall GlobalUnfix(long)
@ stdcall GlobalUnlock(long)
@ stdcall GlobalWire(long)
@ stdcall Heap32First(ptr long long)
@ stdcall Heap32ListFirst(long ptr)
@ stdcall Heap32ListNext(long ptr)
@ stdcall Heap32Next(ptr)
@ stdcall HeapAlloc(long long long) ntdll.RtlAllocateHeap
@ stdcall HeapCompact(long long)
@ stdcall HeapCreate(long long long)
@ stdcall HeapCreateTagsW(long long wstr wstr) ; missing in Win 7
@ stdcall HeapDestroy(long)
@ stdcall HeapExtend(long long ptr long) ; missing in Win 7
@ stdcall HeapFree(long long long) ntdll.RtlFreeHeap
@ stdcall HeapLock(long)
@ stdcall HeapQueryInformation(long long ptr long ptr)
@ stdcall HeapQueryTagW(long long long long ptr) ; missing in Win 7
@ stdcall HeapReAlloc(long long ptr long) ntdll.RtlReAllocateHeap
;@ stub HeapSetFlags ; missing in XP SP3 and Win 7
@ stdcall HeapSetInformation(ptr long ptr long)
@ stdcall HeapSize(long long ptr) ntdll.RtlSizeHeap
@ stdcall HeapSummary(long long ptr)
@ stdcall HeapUnlock(long)
@ stdcall HeapUsage(long long long long ptr) ; missing in Win 7
@ stdcall HeapValidate(long long ptr)
@ stdcall HeapWalk(long ptr)
;@ stdcall IdnToAscii ; Win 7
;@ stdcall IdnToNameprepUnicode ; Win 7
;@ stdcall IdnToUnicode ; Win 7
@ stdcall InitAtomTable(long)
;@ stdcall InitOnceBeginInitialize ; Win 7
;@ stdcall InitOnceComplete ; Win 7
;@ stdcall InitOnceExecuteOnce ; Win 7
;@ stdcall InitOnceInitialize ntdll.RtlRunOnceInitialize ; Win 7
;@ stdcall InitializeConditionVariable ntdll.RtlInitializeConditionVariable ; Win 7
@ stdcall InitializeCriticalSection(ptr) ; FIXME: ntdll.RtlInitializeCriticalSection
@ stdcall InitializeCriticalSectionAndSpinCount(ptr long)
@ stdcall InitializeCriticalSectionEx(ptr long long)
;@ stdcall InitializeExtendedContext ; Win 7
;@ stdcall InitializeProcThreadAttributeList api-ms-win-core-processthreads-l1-1-0.InitializeProcThreadAttributeList ; Win 7
@ stdcall InitializeSListHead(ptr) ntdll.RtlInitializeSListHead
@ stdcall InitializeSRWLock(ptr) ntdll.RtlInitializeSRWLock
@ stdcall -arch=i386 InterlockedCompareExchange (ptr long long)
;@ stdcall -arch=i386 -ret64 InterlockedCompareExchange64(ptr double double) ntdll.RtlInterlockedCompareExchange64
@ stdcall -arch=i386 InterlockedDecrement(ptr)
@ stdcall -arch=i386 InterlockedExchange(ptr long)
@ stdcall -arch=i386 InterlockedExchangeAdd (ptr long )
@ stdcall InterlockedFlushSList(ptr) ntdll.RtlInterlockedFlushSList
@ stdcall -arch=i386 InterlockedIncrement(ptr)
@ stdcall InterlockedPopEntrySList(ptr) ntdll.RtlInterlockedPopEntrySList
@ stdcall InterlockedPushEntrySList(ptr ptr) ntdll.RtlInterlockedPushEntrySList
;@ stdcall InterlockedPushListSList ntdll.RtlInterlockedPushListSList ; Win 7
@ stdcall InvalidateConsoleDIBits(long long)
;@ stub InvalidateNSCache ; missing in XP SP3 and Win 7
@ stdcall IsBadCodePtr(ptr)
@ stdcall IsBadHugeReadPtr(ptr long)
@ stdcall IsBadHugeWritePtr(ptr long)
@ stdcall IsBadReadPtr(ptr long)
@ stdcall IsBadStringPtrA(ptr long)
@ stdcall IsBadStringPtrW(ptr long)
@ stdcall IsBadWritePtr(ptr long)
;@ stdcall IsCalendarLeapDay ; Win 7
;@ stdcall IsCalendarLeapMonth ; Win 7
;@ stdcall IsCalendarLeapYear ; Win 7
@ stdcall IsDBCSLeadByte(long)
@ stdcall IsDBCSLeadByteEx(long long)
@ stdcall IsDebuggerPresent()
;@ stdcall IsNLSDefinedString ; Win 7
;@ stdcall IsNormalizedString ; Win 7
@ stdcall IsProcessInJob(long long ptr)
@ stdcall IsProcessorFeaturePresent(long)
@ stdcall IsSystemResumeAutomatic()
@ stdcall IsThreadAFiber()
;@ stdcall IsThreadAFiber ; Win 7
;@ stdcall IsThreadpoolTimerSet ntdll.TpIsTimerSet ; Win 7
;@ stdcall IsTimeZoneRedirectionEnabled ; Win 7
;@ stdcall IsValidCalDateTime ; Win 7
@ stdcall IsValidCodePage(long)
@ stdcall IsValidLanguageGroup(long long)
@ stdcall IsValidLocale(long long)
;@ stdcall IsValidLocaleName ; Win 7
@ stdcall IsValidUILanguage(long) ; missing in Win 7
@ stdcall IsWow64Process(ptr ptr)
;@ stdcall K32EmptyWorkingSet ; Win 7
;@ stdcall K32EnumDeviceDrivers ; Win 7
;@ stdcall K32EnumPageFilesA ; Win 7
;@ stdcall K32EnumPageFilesW ; Win 7
;@ stdcall K32EnumProcessModules ; Win 7
;@ stdcall K32EnumProcessModulesEx ; Win 7
;@ stdcall K32EnumProcesses ; Win 7
;@ stdcall K32GetDeviceDriverBaseNameA ; Win 7
;@ stdcall K32GetDeviceDriverBaseNameW ; Win 7
;@ stdcall K32GetDeviceDriverFileNameA ; Win 7
;@ stdcall K32GetDeviceDriverFileNameW ; Win 7
;@ stdcall K32GetMappedFileNameA ; Win 7
;@ stdcall K32GetMappedFileNameW ; Win 7
;@ stdcall K32GetModuleBaseNameA ; Win 7
;@ stdcall K32GetModuleBaseNameW ; Win 7
;@ stdcall K32GetModuleFileNameExA ; Win 7
;@ stdcall K32GetModuleFileNameExW ; Win 7
;@ stdcall K32GetModuleInformation ; Win 7
;@ stdcall K32GetPerformanceInfo ; Win 7
;@ stdcall K32GetProcessImageFileNameA ; Win 7
;@ stdcall K32GetProcessImageFileNameW ; Win 7
;@ stdcall K32GetProcessMemoryInfo ; Win 7
;@ stdcall K32GetWsChanges ; Win 7
;@ stdcall K32GetWsChangesEx ; Win 7
;@ stdcall K32InitializeProcessForWsWatch ; Win 7
;@ stdcall K32QueryWorkingSet ; Win 7
;@ stdcall K32QueryWorkingSetEx ; Win 7
@ stdcall LCIDToLocaleName(long wstr long long) ; needed for wine gecko; missing in XP SP3
@ stdcall LCMapStringA(long long str long ptr long)
;@ stdcall LCMapStringEx ; Win 7
@ stdcall LCMapStringW(long long wstr long ptr long)
@ stdcall LZClose(long)
;@ stdcall LZCloseFile ; Win 7
@ stdcall LZCopy(long long)
;@ stdcall LZCreateFileW ; Win 7
@ stdcall LZDone()
@ stdcall LZInit(long)
@ stdcall LZOpenFileA(str ptr long)
@ stdcall LZOpenFileW(wstr ptr long)
@ stdcall LZRead(long str long)
@ stdcall LZSeek(long long long)
@ stdcall LZStart()
@ stdcall LeaveCriticalSection(ptr) ntdll.RtlLeaveCriticalSection
;@ stdcall LeaveCriticalSectionWhenCallbackReturns ntdll.TpCallbackLeaveCriticalSectionOnCompletion ; Win 7
;@ stdcall LoadAppInitDlls ; Win 7
@ stdcall LoadLibraryA(str)
@ stdcall LoadLibraryExA( str long long)
@ stdcall LoadLibraryExW(wstr long long)
@ stdcall LoadLibraryW(wstr)
@ stdcall LoadModule(str ptr)
@ stdcall LoadResource(long long)
;@ stdcall LoadStringBaseExW ; Win 7
;@ stdcall LoadStringBaseW ; Win 7
@ stdcall LocalAlloc(long long)
@ stdcall LocalCompact(long)
@ stdcall LocalFileTimeToFileTime(ptr ptr)
@ stdcall LocalFlags(long)
@ stdcall LocalFree(long)
@ stdcall LocalHandle(ptr)
@ stdcall LocalLock(long)
@ stdcall LocalReAlloc(long long long)
@ stdcall LocalShrink(long long)
@ stdcall LocalSize(long)
@ stdcall LocalUnlock(long)
;@ stub LocaleNameToLCID ; missing in XP SP3
;@ stdcall LocateExtendedFeature api-ms-win-core-xstate-l1-1-0.RtlLocateExtendedFeature ; Win 7
;@ stdcall LocateLegacyContext api-ms-win-core-xstate-l1-1-0.RtlLocateLegacyContext ; Win 7
@ stdcall LockFile(long long long long long)
@ stdcall LockFileEx(long long long long long ptr)
@ stdcall LockResource(long)
;@ stdcall MakeCriticalSectionGlobal(ptr) // ???
@ stdcall MapUserPhysicalPages(ptr long ptr)
@ stdcall MapUserPhysicalPagesScatter(ptr long ptr)
@ stdcall MapViewOfFile(long long long long long)
@ stdcall MapViewOfFileEx(long long long long long ptr)
;@ stdcall MapViewOfFileExNuma ; Win 7
@ stdcall Module32First(long ptr)
@ stdcall Module32FirstW(long ptr)
@ stdcall Module32Next(long ptr)
@ stdcall Module32NextW(long ptr)
@ stdcall MoveFileA(str str)
@ stdcall MoveFileExA(str str long)
@ stdcall MoveFileExW(wstr wstr long)
;@ stdcall MoveFileTransactedA ; Win 7
;@ stdcall MoveFileTransactedW ; Win 7
@ stdcall MoveFileW(wstr wstr)
@ stdcall MoveFileWithProgressA(str str ptr ptr long)
@ stdcall MoveFileWithProgressW(wstr wstr ptr ptr long)
@ stdcall MulDiv(long long long)
@ stdcall MultiByteToWideChar(long long str long ptr long)
@ stdcall NeedCurrentDirectoryForExePathA(str)
@ stdcall NeedCurrentDirectoryForExePathW(wstr)
;@ stdcall NlsCheckPolicy ; Win 7
@ stdcall NlsConvertIntegerToString(long long long wstr long) ; missing in Win 7
;@ stdcall NlsEventDataDescCreate ; Win 7
@ stdcall NlsGetCacheUpdateCount()
;@ stub NlsResetProcessLocale ; missing in XP SP3 and Win 7
;@ stdcall NlsUpdateLocale ; Win 7
;@ stdcall NlsUpdateSystemLocale ; Win 7
;@ stdcall NlsWriteEtwEvent ; Win 7
;@ stdcall NormalizeString ; Win 7
;@ stdcall NotifyMountMgr ; Win 7
;@ stub NotifyNLSUserCache ; missing in XP SP3 and win 7
;@ stdcall NotifyUILanguageChange ; Win 7
@ stdcall NumaVirtualQueryNode(long long long long) ; missing in win 7
@ stdcall OpenConsoleW(wstr long long long)
@ stdcall OpenDataFile(long long) ; missing in Win 7
@ stdcall OpenEventA(long long str)
@ stdcall OpenEventW(long long wstr)
@ stdcall OpenFile(str ptr long)
;@ stdcall OpenFileById ; Win 7
@ stdcall OpenFileMappingA(long long str)
@ stdcall OpenFileMappingW(long long wstr)
@ stdcall OpenJobObjectA(long long str)
@ stdcall OpenJobObjectW(long long wstr)
@ stdcall OpenMutexA(long long str)
@ stdcall OpenMutexW(long long wstr)
;@ stdcall OpenPrivateNamespaceA ; Win 7
;@ stdcall OpenPrivateNamespaceW ; Win 7
@ stdcall OpenProcess(long long long)
;@ stdcall OpenProcessToken api-ms-win-core-processthreads-l1-1-0.OpenProcessToken ; Win 7
@ stdcall OpenProfileUserMapping()
@ stdcall OpenSemaphoreA(long long str)
@ stdcall OpenSemaphoreW(long long wstr)
@ stdcall OpenThread(long long long)
;@ stdcall OpenThreadToken api-ms-win-core-processthreads-l1-1-0.OpenThreadToken ; win 7
@ stdcall OpenWaitableTimerA(long long str)
@ stdcall OpenWaitableTimerW(long long wstr)
@ stdcall OutputDebugStringA(str)
@ stdcall OutputDebugStringW(wstr)
@ stdcall PeekConsoleInputA(ptr ptr long ptr)
@ stdcall PeekConsoleInputW(ptr ptr long ptr)
@ stdcall PeekNamedPipe(long ptr long ptr ptr ptr)
@ stdcall PostQueuedCompletionStatus(long long ptr ptr)
;@ stdcall PowerClearRequest ; Win 7
;@ stdcall PowerCreateRequest ; Win 7
;@ stdcall PowerSetRequest ; Win 7
@ stdcall PrepareTape(ptr long long)
@ stdcall PrivCopyFileExW(wstr wstr ptr ptr long long)
@ stdcall PrivMoveFileIdentityW(long long long)
@ stdcall Process32First (ptr ptr)
@ stdcall Process32FirstW (ptr ptr)
@ stdcall Process32Next (ptr ptr)
@ stdcall Process32NextW (ptr ptr)
@ stdcall ProcessIdToSessionId(long ptr)
@ stdcall PulseEvent(long)
@ stdcall PurgeComm(long long)
;@ stdcall QueryActCtxSettingsW ; Win 7
;@ stdcall QueryActCtxW(long ptr ptr long ptr long ptr)
@ stdcall QueryActCtxW(long ptr ptr long ptr long ptr)
@ stdcall QueryDepthSList(ptr) ntdll.RtlQueryDepthSList
@ stdcall QueryDosDeviceA(str ptr long)
@ stdcall QueryDosDeviceW(wstr ptr long)
@ stdcall QueryFullProcessImageNameA(ptr long str ptr) ; Vista and later
@ stdcall QueryFullProcessImageNameW(ptr long wstr ptr) ; Vista and later
;@ stdcall QueryIdleProcessorCycleTime ; Win 7
;@ stdcall QueryIdleProcessorCycleTimeEx ; Win 7
@ stdcall QueryInformationJobObject(long long ptr long ptr)
@ stdcall QueryMemoryResourceNotification(ptr ptr)
;@ stub QueryNumberOfEventLogRecords ; missing in XP SP3 and Win 7
;@ stub QueryOldestEventLogRecord ; missing in XP SP3 and Win 7
@ stdcall QueryPerformanceCounter(ptr)
@ stdcall QueryPerformanceFrequency(ptr)
;@ stdcall QueryProcessAffinityUpdateMode ; Win 7
;@ stdcall QueryProcessCycleTime ; Win 7
;@ stdcall QueryThreadCycleTime ; Win 7
;@ stdcall QueryThreadProfiling ; Win 7
;@ stdcall QueryThreadpoolStackInformation ; Win 7
;@ stdcall -arch=x86_64 QueryUmsThreadInformation
;@ stdcall QueryUnbiasedInterruptTime ; Win 7
@ stdcall QueryWin31IniFilesMappedToRegistry(long long long long) ; missing in Win 7
@ stdcall QueueUserAPC(ptr long long)
@ stdcall QueueUserWorkItem(ptr ptr long)
@ stdcall RaiseException(long long long ptr)
;@ stdcall RaiseFailFastException ; Win 7
@ stdcall ReOpenFile(ptr long long long)
@ stdcall ReadConsoleA(long ptr long ptr ptr)
@ stdcall ReadConsoleInputA(long ptr long ptr)
@ stdcall ReadConsoleInputExA(long ptr long ptr long)
@ stdcall ReadConsoleInputExW(long ptr long ptr long)
@ stdcall ReadConsoleInputW(long ptr long ptr)
@ stdcall ReadConsoleOutputA(long ptr long long ptr)
@ stdcall ReadConsoleOutputAttribute(long ptr long long ptr)
@ stdcall ReadConsoleOutputCharacterA(long ptr long long ptr)
@ stdcall ReadConsoleOutputCharacterW(long ptr long long ptr)
@ stdcall ReadConsoleOutputW(long ptr long long ptr)
@ stdcall ReadConsoleW(long ptr long ptr ptr)
@ stdcall ReadDirectoryChangesW(long ptr long long long ptr ptr ptr)
@ stdcall ReadFile(long ptr long ptr ptr)
@ stdcall ReadFileEx(long ptr long ptr ptr)
@ stdcall ReadFileScatter(long ptr long ptr ptr)
@ stdcall ReadProcessMemory(long ptr ptr long ptr)
;@ stdcall ReadThreadProfilingData ; Win 7
;@ stdcall RegCloseKey ; Win 7
;@ stdcall RegCreateKeyExA ; Win 7
;@ stdcall RegCreateKeyExW ; Win 7
;@ stdcall RegDeleteKeyExA ; Win 7
;@ stdcall RegDeleteKeyExW ; Win 7
;@ stdcall RegDeleteTreeA ; Win 7
;@ stdcall RegDeleteTreeW ; Win 7
;@ stdcall RegDeleteValueA ; Win 7
;@ stdcall RegDeleteValueW ; Win 7
;@ stdcall RegDisablePredefinedCacheEx ; Win 7
;@ stdcall RegEnumKeyExA ; Win 7
;@ stdcall RegEnumKeyExW ; Win 7
;@ stdcall RegEnumValueA ; Win 7
;@ stdcall RegEnumValueW ; Win 7
;@ stdcall RegFlushKey ; Win 7
;@ stdcall RegGetKeySecurity ; Win 7
;@ stdcall RegGetValueA ; Win 7
;@ stdcall RegGetValueW ; Win 7
;@ stdcall RegKrnGetGlobalState ; Win 7
;@ stdcall RegKrnInitialize ; Win 7
;@ stdcall RegLoadKeyA ; Win 7
;@ stdcall RegLoadKeyW ; Win 7
;@ stdcall RegLoadMUIStringA ; Win 7
;@ stdcall RegLoadMUIStringW ; Win 7
;@ stdcall RegNotifyChangeKeyValue ; Win 7
;@ stdcall RegOpenCurrentUser ; Win 7
;@ stdcall RegOpenKeyExA ; Win 7
;@ stdcall RegOpenKeyExW ; Win 7
;@ stdcall RegOpenUserClassesRoot ; Win 7
;@ stdcall RegQueryInfoKeyA ; Win 7
;@ stdcall RegQueryInfoKeyW ; Win 7
;@ stdcall RegQueryValueExA ; Win 7
;@ stdcall RegQueryValueExW ; Win 7
;@ stdcall RegRestoreKeyA ; Win 7
;@ stdcall RegRestoreKeyW ; Win 7
;@ stdcall RegSaveKeyExA ; Win 7
;@ stdcall RegSaveKeyExW ; Win 7
;@ stdcall RegSetKeySecurity ; Win 7
;@ stdcall RegSetValueExA ; Win 7
;@ stdcall RegSetValueExW ; Win 7
;@ stdcall RegUnLoadKeyA ; Win 7
;@ stdcall RegUnLoadKeyW ; Win 7
;@ stdcall RegisterApplicationRecoveryCallback ; Win 7
@ stdcall RegisterApplicationRestart(wstr long)
@ stdcall RegisterConsoleIME(ptr ptr)
@ stdcall RegisterConsoleOS2(long)
@ stdcall RegisterConsoleVDM(long long long long long long long long long long long)
;@ stub RegisterServiceProcess ; missing in XP SP3 and Win 7
;@ stub RegisterSysMsgHandler ; missing in XP SP3 and win 7
@ stdcall RegisterWaitForInputIdle(ptr)
@ stdcall RegisterWaitForSingleObject(ptr long ptr ptr long long)
@ stdcall RegisterWaitForSingleObjectEx(long ptr ptr long long)
@ stdcall RegisterWowBaseHandlers(long)
@ stdcall RegisterWowExec(long)
;@ stdcall ReinitializeCriticalSection(ptr) ; ???
@ stdcall ReleaseActCtx(ptr)
@ stdcall ReleaseMutex(long)
;@ stdcall ReleaseMutexWhenCallbackReturns ntdll.TpCallbackReleaseMutexOnCompletion ; Win 7
@ stdcall ReleaseSRWLockExclusive(ptr) ntdll.RtlReleaseSRWLockExclusive
@ stdcall ReleaseSRWLockShared(ptr) ntdll.RtlReleaseSRWLockShared
@ stdcall ReleaseSemaphore(long long ptr)
;@ stdcall ReleaseSemaphoreWhenCallbackReturns ntdll.TpCallbackReleaseSemaphoreOnCompletion ; Win 7
@ stdcall RemoveDirectoryA(str)
;@ stdcall RemoveDirectoryTransactedA ; Win 7
;@ stdcall RemoveDirectoryTransactedW ; Win 7
@ stdcall RemoveDirectoryW(wstr)
@ stdcall RemoveLocalAlternateComputerNameA(str long)
@ stdcall RemoveLocalAlternateComputerNameW(wstr long)
;@ stdcall RemoveSecureMemoryCacheCallback ; Win 7
@ stdcall RemoveVectoredContinueHandler(ptr) ntdll.RtlRemoveVectoredContinueHandler
@ stdcall RemoveVectoredExceptionHandler(ptr) ntdll.RtlRemoveVectoredExceptionHandler
@ stdcall ReplaceFile(wstr wstr wstr long ptr ptr) ReplaceFileW
@ stdcall ReplaceFileA(str str str long ptr ptr)
@ stdcall ReplaceFileW(wstr wstr wstr long ptr ptr)
;@ stdcall ReplacePartitionUnit ; Win 7
@ stdcall RequestDeviceWakeup(long)
@ stdcall RequestWakeupLatency(long)
@ stdcall ResetEvent(long)
@ stdcall ResetWriteWatch(ptr long)
;@ stdcall ResolveLocaleName ; Win 7
@ stdcall RestoreLastError(long) ntdll.RtlRestoreLastWin32Error
@ stdcall ResumeThread(long)
@ cdecl -arch=x86_64 RtlAddFunctionTable(ptr long long) ntdll.RtlAddFunctionTable
@ stdcall -register RtlCaptureContext(ptr) ntdll.RtlCaptureContext
@ stdcall RtlCaptureStackBackTrace(long long ptr ptr) ntdll.RtlCaptureStackBackTrace
@ stdcall -arch=x86_64 RtlCompareMemory(ptr ptr ptr)
@ stdcall -arch=x86_64 RtlCopyMemory(ptr ptr ptr)
@ stdcall -arch=x86_64 RtlDeleteFunctionTable(ptr)
@ stdcall RtlFillMemory(ptr long long) ntdll.RtlFillMemory
@ stdcall -arch=x86_64 RtlInstallFunctionTableCallback(double double long ptr ptr ptr)
@ stdcall -arch=x86_64 RtlLookupFunctionEntry(ptr ptr ptr) ntdll.RtlLookupFunctionEntry
@ stdcall RtlMoveMemory(ptr ptr long) ntdll.RtlMoveMemory
@ stdcall -arch=x86_64 RtlPcToFileHeader(ptr ptr) ntdll.RtlPcToFileHeader
@ stdcall -arch=x86_64 RtlRaiseException(ptr) ntdll.RtlRaiseException
@ stdcall -arch=x86_64 RtlRestoreContext(ptr ptr) ntdll.RtlRestoreContext
@ stdcall RtlUnwind(ptr ptr ptr long) ntdll.RtlUnwind
@ stdcall -arch=x86_64 RtlUnwindEx(ptr ptr ptr ptr ptr ptr) ntdll.RtlUnwindEx
@ stdcall -arch=x86_64 RtlVirtualUnwind(ptr ptr ptr long) ntdll.RtlVirtualUnwind
@ stdcall RtlZeroMemory(ptr long) ntdll.RtlZeroMemory
@ stdcall ScrollConsoleScreenBufferA(long ptr ptr ptr ptr)
@ stdcall ScrollConsoleScreenBufferW(long ptr ptr ptr ptr)
@ stdcall SearchPathA(str str str long ptr ptr)
@ stdcall SearchPathW(wstr wstr wstr long ptr ptr)
@ stdcall SetCPGlobal(long) ; missing in Win 7
@ stdcall SetCalendarInfoA(long long long str)
@ stdcall SetCalendarInfoW(long long long wstr)
@ stdcall SetClientTimeZoneInformation(ptr)
@ stdcall SetComPlusPackageInstallStatus(ptr)
@ stdcall SetCommBreak(long)
@ stdcall SetCommConfig(long ptr long)
@ stdcall SetCommMask(long ptr)
@ stdcall SetCommState(long ptr)
@ stdcall SetCommTimeouts(long ptr)
@ stdcall SetComputerNameA(str)
@ stdcall SetComputerNameExA(long str)
@ stdcall SetComputerNameExW(long wstr)
@ stdcall SetComputerNameW(wstr)
@ stdcall SetConsoleActiveScreenBuffer(long)
@ stdcall SetConsoleCP(long)
@ stdcall SetConsoleCommandHistoryMode(long) ; missing in win 7
@ stdcall SetConsoleCtrlHandler(ptr long)
@ stdcall SetConsoleCursor(long long)
@ stdcall SetConsoleCursorInfo(long ptr)
@ stdcall SetConsoleCursorMode(long long long)
@ stdcall SetConsoleCursorPosition(long long)
@ stdcall SetConsoleDisplayMode(long long ptr)
@ stdcall SetConsoleFont(long long)
@ stdcall SetConsoleHardwareState(long long long)
@ stdcall SetConsoleHistoryInfo(ptr)
@ stdcall SetConsoleIcon(ptr)
@ stdcall SetConsoleInputExeNameA(ptr)
@ stdcall SetConsoleInputExeNameW(ptr)
@ stdcall SetConsoleKeyShortcuts(long long long long)
@ stdcall SetConsoleLocalEUDC(long long long long)
@ stdcall SetConsoleMaximumWindowSize(long long)
@ stdcall SetConsoleMenuClose(long)
@ stdcall SetConsoleMode(long long)
@ stdcall SetConsoleNlsMode(long long)
@ stdcall SetConsoleNumberOfCommandsA(long long)
@ stdcall SetConsoleNumberOfCommandsW(long long)
@ stdcall SetConsoleOS2OemFormat(long)
@ stdcall SetConsoleOutputCP(long)
@ stdcall SetConsolePalette(long long long)
;@ stdcall SetConsoleScreenBufferInfoEx ; Win 7
@ stdcall SetConsoleScreenBufferSize(long long)
@ stdcall SetConsoleTextAttribute(long long)
@ stdcall SetConsoleTitleA(str)
@ stdcall SetConsoleTitleW(wstr)
@ stdcall SetConsoleWindowInfo(long long ptr)
@ stdcall SetCriticalSectionSpinCount(ptr long) ntdll.RtlSetCriticalSectionSpinCount
;@ stdcall SetCurrentConsoleFontEx ; Win 7
@ stdcall SetCurrentDirectoryA(str)
@ stdcall SetCurrentDirectoryW(wstr)
;@ stub SetDaylightFlag ; missing in XP SP3 and Win 7
@ stdcall SetDefaultCommConfigA(str ptr long)
@ stdcall SetDefaultCommConfigW(wstr ptr long)
@ stdcall SetDllDirectoryA(str)
@ stdcall SetDllDirectoryW(wstr)
;@ stdcall SetDynamicTimeZoneInformation ; Win 7
@ stdcall SetEndOfFile(long)
;@ stdcall SetEnvironmentStringsA ; Win 7
;@ stdcall SetEnvironmentStringsW ; Win 7
@ stdcall SetEnvironmentVariableA(str str)
@ stdcall SetEnvironmentVariableW(wstr wstr)
@ stdcall SetErrorMode(long)
@ stdcall SetEvent(long)
;@ stdcall SetEventWhenCallbackReturns ntdll.TpCallbackSetEventOnCompletion ; Win 7
;@ stdcall SetExtendedFeaturesMask api-ms-win-core-xstate-l1-1-0.RtlSetExtendedFeaturesMask ; Win 7
@ stdcall SetFileApisToANSI()
@ stdcall SetFileApisToOEM()
@ stdcall SetFileAttributesA(str long)
;@ stdcall SetFileAttributesTransactedA ; Win 7
;@ stdcall SetFileAttributesTransactedW ; Win 7
@ stdcall SetFileAttributesW(wstr long)
;@ stdcall SetFileBandwidthReservation ; Win 7
;@ stdcall SetFileCompletionNotificationModes ; Win 7
;@ stdcall SetFileInformationByHandle ; Win 7
;@ stdcall SetFileIoOverlappedRange ; Win 7
@ stdcall SetFilePointer(long long ptr long)
@ stdcall SetFilePointerEx(long double ptr long)
@ stdcall SetFileShortNameA(long str)
@ stdcall SetFileShortNameW(long wstr)
@ stdcall SetFileTime(long ptr ptr ptr)
@ stdcall SetFileValidData(long double)
@ stdcall SetFirmwareEnvironmentVariableA(str str ptr long)
@ stdcall SetFirmwareEnvironmentVariableW(wstr wstr ptr long)
@ stdcall SetHandleContext(long long) ; missing in Win 7 x64
@ stdcall SetHandleCount(long)
@ stdcall SetHandleInformation(long long long)
@ stdcall SetInformationJobObject(long long ptr long)
@ stdcall SetLastConsoleEventActive() ; missing in XP SP3
@ stdcall SetLastError(long) ntdll.RtlSetLastWin32Error
@ stdcall SetLocalPrimaryComputerNameA(long long) ; missing in XP SP3
@ stdcall SetLocalPrimaryComputerNameW(long long) ; missing in XP SP3
@ stdcall SetLocalTime(ptr)
@ stdcall SetLocaleInfoA(long long str)
@ stdcall SetLocaleInfoW(long long wstr)
@ stdcall SetMailslotInfo(long long)
@ stdcall SetMessageWaitingIndicator(ptr long)
;@ stdcall SetNamedPipeAttribute ; Win 7
@ stdcall SetNamedPipeHandleState(long ptr ptr ptr)
@ stdcall SetPriorityClass(long long)
@ stdcall SetProcessAffinityMask(long long)
;@ stdcall SetProcessAffinityUpdateMode ; Win 7
;@ stdcall SetProcessDEPPolicy ; Win 7
;@ stdcall SetProcessPreferredUILanguages ; Win 7
@ stdcall SetProcessPriorityBoost(long long)
@ stdcall SetProcessShutdownParameters(long long)
@ stdcall SetProcessWorkingSetSize(long long long)
;@ stdcall SetProcessWorkingSetSizeEx ; Win 7
;@ stdcall SetSearchPathMode ; Win 7
@ stdcall SetStdHandle(long long)
;@ stdcall SetStdHandleEx ; Win 7
;@ stdcall SetSystemFileCacheSize ; Win 7
@ stdcall SetSystemPowerState(long long)
@ stdcall SetSystemTime(ptr)
@ stdcall SetSystemTimeAdjustment(long long)
@ stdcall SetTapeParameters(ptr long ptr)
@ stdcall SetTapePosition(ptr long long long long long)
@ stdcall SetTermsrvAppInstallMode(long)
@ stdcall SetThreadAffinityMask(long long)
@ stdcall SetThreadContext(long ptr)
;@ stdcall SetThreadErrorMode(long ptr) ; Win 7
@ stdcall SetThreadExecutionState(long)
;@ stdcall SetThreadGroupAffinity ; Win 7
@ stdcall SetThreadIdealProcessor(long long)
;@ stdcall SetThreadIdealProcessorEx ; Win 7
@ stdcall SetThreadLocale(long)
;@ stdcall SetThreadPreferredUILanguages ; Win 7
@ stdcall SetThreadPriority(long long)
@ stdcall SetThreadPriorityBoost(long long)
;@ stdcall SetThreadStackGuarantee ; Win 7
;@ stdcall SetThreadToken api-ms-win-core-processthreads-l1-1-0.SetThreadToken ; Win 7
@ stdcall SetThreadUILanguage(long)
;@ stdcall SetThreadpoolStackInformation ; Win 7
;@ stdcall SetThreadpoolThreadMaximum ntdll.TpSetPoolMaxThreads ; Win 7
;@ stdcall SetThreadpoolThreadMinimum ; Win 7
;@ stdcall SetThreadpoolTimer ntdll.TpSetTimer ; Win 7
;@ stdcall SetThreadpoolWait ntdll.TpSetWait ; Win 7
@ stdcall SetTimeZoneInformation(ptr)
@ stdcall SetTimerQueueTimer(long ptr ptr long long long)
;@ stdcall -arch?x86_64 SetUmsThreadInformation
@ stdcall SetUnhandledExceptionFilter(ptr)
@ stdcall SetUserGeoID(long)
@ stdcall SetVDMCurrentDirectories(long long)
@ stdcall SetVolumeLabelA(str str)
@ stdcall SetVolumeLabelW(wstr wstr)
@ stdcall SetVolumeMountPointA(str str)
@ stdcall SetVolumeMountPointW(wstr wstr)
@ stdcall SetWaitableTimer(long ptr long ptr ptr long)
;@ stdcall SetWaitableTimerEx api-ms-win-core-threadpool-l1-1-0.SetWaitableTimerEx ; Win 7
@ stdcall SetupComm(long long long)
@ stdcall ShowConsoleCursor(long long)
@ stdcall SignalObjectAndWait(long long long long)
@ stdcall SizeofResource(long long)
@ stdcall Sleep(long)
;@ stdcall SleepConditionVariableCS ; Win 7
;@ stdcall SleepConditionVariableSRW ; Win 7
@ stdcall SleepEx(long long)
;@ stdcall SortCloseHandle ; Win 7
;@ stdcall SortGetHandle ; Win 7
;@ stdcall StartThreadpoolIo ntdll.TpStartAsyncIoOperation ; Win 7
;@ stdcall SubmitThreadpoolWork ntdll.TpPostWork ; Win 7
@ stdcall SuspendThread(long)
@ stdcall SwitchToFiber(ptr)
@ stdcall SwitchToThread()
@ stdcall SystemTimeToFileTime(ptr ptr)
@ stdcall SystemTimeToTzSpecificLocalTime (ptr ptr ptr)
@ stdcall TerminateJobObject(long long)
@ stdcall TerminateProcess(long long)
@ stdcall TerminateThread(long long)
@ stdcall TermsrvAppInstallMode()
@ stdcall Thread32First(long ptr)
@ stdcall Thread32Next(long ptr)
@ stdcall TlsAlloc()
;@ stub TlsAllocInternal ; missing in XP SP3 and Win 7
@ stdcall TlsFree(long)
;@ stub TlsFreeInternal ; missing in XP SP3 and Win 7
@ stdcall TlsGetValue(long)
@ stdcall TlsSetValue(long ptr)
@ stdcall Toolhelp32ReadProcessMemory(long ptr ptr long ptr)
@ stdcall TransactNamedPipe(long ptr long ptr long ptr ptr)
@ stdcall TransmitCommChar(long long)
@ stdcall TrimVirtualBuffer(ptr) ; missing in Win 7
;@ stdcall TryAcquireSRWLockExclusive ntdll.RtlTryAcquireSRWLockExclusive ; Win 7
;@ stdcall TryAcquireSRWLockShared ntdll.RtlTryAcquireSRWLockShared ; Win 7
@ stdcall TryEnterCriticalSection(ptr) ntdll.RtlTryEnterCriticalSection
;@ stdcall TrySubmitThreadpoolCallback ; Win 7
@ stdcall TzSpecificLocalTimeToSystemTime(ptr ptr ptr)
@ stdcall UTRegister(long str str str ptr ptr ptr)
@ stdcall UTUnRegister(long)
;@ stdcall -arch=x86_64 UmsThreadYield
@ stdcall UnhandledExceptionFilter(ptr)
;@ stdcall UninitializeCriticalSection(ptr) ; ???
@ stdcall UnlockFile(long long long long long)
@ stdcall UnlockFileEx(long long long long ptr)
@ stdcall UnmapViewOfFile(ptr)
;@ stdcall UnregisterApplicationRecoveryCallback ; Win 7
;@ stdcall UnregisterApplicationRestart ; Win 7
@ stdcall UnregisterConsoleIME()
@ stdcall UnregisterWait(long)
@ stdcall UnregisterWaitEx(long long)
;@ stdcall UpdateCalendarDayOfWeek ; Win 7
;@ stdcall UpdateProcThreadAttribute api-ms-win-core-processthreads-l1-1-0.UpdateProcThreadAttribute ; Win 7
@ stdcall UpdateResourceA(long str str long ptr long)
@ stdcall UpdateResourceW(long wstr wstr long ptr long)
@ stdcall VDMConsoleOperation(long long)
@ stdcall VDMOperationStarted(long)
;@ stub ValidateCType ; missing in XP SP3 and Win 7
;@ stub ValidateLocale ; missing in XP SP3 and Win 7
@ stdcall VerLanguageNameA(long str long)
@ stdcall VerLanguageNameW(long wstr long)
@ stdcall -ret64 VerSetConditionMask(long long long long) ntdll.VerSetConditionMask
@ stdcall VerifyConsoleIoHandle(long)
;@ stdcall VerifyScripts ; Win 7
@ stdcall VerifyVersionInfoA(long long double)
@ stdcall VerifyVersionInfoW(long long double)
@ stdcall VirtualAlloc(ptr long long long)
@ stdcall VirtualAllocEx(long ptr long long long)
;@ stdcall VirtualAllocExNuma ; Win 7
@ stdcall VirtualBufferExceptionHandler(long long long) ; missing in Win 7
@ stdcall VirtualFree(ptr long long)
@ stdcall VirtualFreeEx(long ptr long long)
@ stdcall VirtualLock(ptr long)
@ stdcall VirtualProtect(ptr long long ptr)
@ stdcall VirtualProtectEx(long ptr long long ptr)
@ stdcall VirtualQuery(ptr ptr long)
@ stdcall VirtualQueryEx(long ptr ptr long)
@ stdcall VirtualUnlock(ptr long)
;@ stdcall WTSGetActiveConsoleSessionId ; Win 7
@ stdcall WaitCommEvent(long ptr ptr)
@ stdcall WaitForDebugEvent(ptr long)
@ stdcall WaitForMultipleObjects(long ptr long long)
@ stdcall WaitForMultipleObjectsEx(long ptr long long long)
@ stdcall WaitForSingleObject(long long)
@ stdcall WaitForSingleObjectEx(long long long)
;@ stdcall WaitForThreadpoolIoCallbacks ntdll.TpWaitForIoCompletion ; Win 7
;@ stdcall WaitForThreadpoolTimerCallbacks ntdll.TpWaitForTimer ; Win 7
;@ stdcall WaitForThreadpoolWaitCallbacks ntdll.TpWaitForWait ; Win 7
;@ stdcall WaitForThreadpoolWorkCallbacks ntdll.TpWaitForWork ; Win 7
@ stdcall WaitNamedPipeA (str long)
@ stdcall WaitNamedPipeW (wstr long)
@ stdcall WakeAllConditionVariable(ptr) ntdll.RtlWakeAllConditionVariable
@ stdcall WakeConditionVariable(ptr) ntdll.RtlWakeConditionVariable
;@ stdcall WerGetFlags ; Win 7
;@ stdcall WerRegisterFile ; Win 7
;@ stdcall WerRegisterMemoryBlock ; Win 7
;@ stdcall WerRegisterRuntimeExceptionModule ; Win 7
;@ stdcall WerSetFlags ; Win 7
;@ stdcall WerUnregisterFile ; Win 7
;@ stdcall WerUnregisterMemoryBlock ; Win 7
;@ stdcall WerUnregisterRuntimeExceptionModule ; Win 7
;@ stdcall WerpCleanupMessageMapping ; Win 7
;@ stdcall WerpInitiateRemoteRecovery ; Win 7
;@ stdcall WerpNotifyLoadStringResource ; Win 7
;@ stdcall WerpNotifyLoadStringResourceEx ; Win 7
;@ stdcall WerpNotifyUseStringResource ; Win 7
;@ stdcall WerpStringLookup ; Win 7
@ stdcall WideCharToMultiByte(long long wstr long ptr long ptr ptr)
@ stdcall WinExec(str long)
@ stdcall Wow64DisableWow64FsRedirection(ptr)
@ stdcall Wow64EnableWow64FsRedirection(long)
;@ stdcall Wow64GetThreadContext ; Win 7
;@ stdcall Wow64GetThreadSelectorEntry ; Win 7
@ stdcall Wow64RevertWow64FsRedirection(ptr)
;@ stdcall Wow64SetThreadContext ; Win 7
;@ stdcall Wow64SuspendThread ; Win 7
@ stdcall WriteConsoleA(long ptr long ptr ptr)
@ stdcall WriteConsoleInputA(long ptr long ptr)
@ stdcall WriteConsoleInputVDMA(long long long long)
@ stdcall WriteConsoleInputVDMW(long long long long)
@ stdcall WriteConsoleInputW(long ptr long ptr)
@ stdcall WriteConsoleOutputA(long ptr long long ptr)
@ stdcall WriteConsoleOutputAttribute(long ptr long long ptr)
@ stdcall WriteConsoleOutputCharacterA(long ptr long long ptr)
@ stdcall WriteConsoleOutputCharacterW(long ptr long long ptr)
@ stdcall WriteConsoleOutputW(long ptr long long ptr)
@ stdcall WriteConsoleW(long ptr long ptr ptr)
@ stdcall WriteFile(long ptr long ptr ptr)
@ stdcall WriteFileEx(long ptr long ptr ptr)
@ stdcall WriteFileGather(long ptr long ptr ptr)
@ stdcall WritePrivateProfileSectionA(str str str)
@ stdcall WritePrivateProfileSectionW(wstr wstr wstr)
@ stdcall WritePrivateProfileStringA(str str str str)
@ stdcall WritePrivateProfileStringW(wstr wstr wstr wstr)
@ stdcall WritePrivateProfileStructA (str str ptr long str)
@ stdcall WritePrivateProfileStructW(wstr wstr ptr long wstr)
@ stdcall WriteProcessMemory(long ptr ptr long ptr)
@ stdcall WriteProfileSectionA(str str)
@ stdcall WriteProfileSectionW(str str)
@ stdcall WriteProfileStringA(str str str)
@ stdcall WriteProfileStringW(wstr wstr wstr)
@ stdcall WriteTapemark(ptr long long long)
@ stdcall WTSGetActiveConsoleSessionId() ; missing in win 7
@ stdcall ZombifyActCtx(ptr)
;@ stdcall -arch=x86_64 __C_specific_handler ntdll.__C_specific_handler
;@ stdcall -arch=x86_64 __chkstk ntdll.__chkstk
;@ stdcall -arch=x86_64 __misaligned_access ntdll.__misaligned_access
;@ stub _DebugOut ; missing in XP SP3 and Win 7
;@ stub _DebugPrintf ; missing in XP SP3 and Win 7
@ stdcall _hread(long ptr long)
@ stdcall _hwrite(long ptr long)
@ stdcall _lclose(long)
@ stdcall _lcreat(str long)
@ stdcall _llseek(long long long)
;@ stdcall -arch=x86_64 _local_unwind ntdll._local_unwind; Win 7
@ stdcall _lopen(str long)
@ stdcall _lread(long ptr long) _hread
@ stdcall _lwrite(long ptr long) _hwrite
;@ stub dprintf ; missing in XP SP3 and Win 7
@ stdcall lstrcat(str str) lstrcatA
@ stdcall lstrcatA(str str)
@ stdcall lstrcatW(wstr wstr)
@ stdcall lstrcmp(str str) lstrcmpA
@ stdcall lstrcmpA(str str)
@ stdcall lstrcmpW(wstr wstr)
@ stdcall lstrcmpi(str str) lstrcmpiA
@ stdcall lstrcmpiA(str str)
@ stdcall lstrcmpiW(wstr wstr)
@ stdcall lstrcpy(ptr str) lstrcpyA
@ stdcall lstrcpyA(ptr str)
@ stdcall lstrcpyW(ptr wstr)
@ stdcall lstrcpyn(ptr str long) lstrcpynA
@ stdcall lstrcpynA(ptr str long)
@ stdcall lstrcpynW(ptr wstr long)
@ stdcall lstrlen(str) lstrlenA
@ stdcall lstrlenA(str)
@ stdcall lstrlenW(wstr)
;@ stdcall -arch=x86_64 uaw_lstrcmpW ; Win 7
;@ stdcall -arch=x86_64 uaw_lstrcmpiW ; Win 7
;@ stdcall -arch=x86_64 uaw_lstrlenW ; Win 7
;@ stdcall -arch=x86_64 uaw_wcschr ; Win 7
;@ stdcall -arch=x86_64 uaw_wcscpy ; Win 7
;@ stdcall -arch=x86_64 uaw_wcsicmp ; Win 7
;@ stdcall -arch=x86_64 uaw_wcslen ; Win 7
;@ stdcall -arch=x86_64 uaw_wcsrchr ; Win 7
