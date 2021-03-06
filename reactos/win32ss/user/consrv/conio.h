/*
 * COPYRIGHT:       See COPYING in the top level directory
 * PROJECT:         ReactOS Console Server DLL
 * FILE:            win32ss/user/consrv/conio.h
 * PURPOSE:         Internal Console I/O Interface
 * PROGRAMMERS:     Hermes Belusca-Maito (hermes.belusca@sfr.fr)
 */

#pragma once

/* Macros used to call functions in the FRONTEND_VTBL virtual table */

#define ConioCleanupConsole(Console) \
    (Console)->TermIFace.Vtbl->CleanupConsole(Console)
#define ConioDrawRegion(Console, Region) \
    (Console)->TermIFace.Vtbl->DrawRegion((Console), (Region))
#define ConioWriteStream(Console, Block, CurStartX, CurStartY, ScrolledLines, Buffer, Length) \
    (Console)->TermIFace.Vtbl->WriteStream((Console), (Block), (CurStartX), (CurStartY), \
                                           (ScrolledLines), (Buffer), (Length))
#define ConioSetCursorInfo(Console, Buff) \
    (Console)->TermIFace.Vtbl->SetCursorInfo((Console), (Buff))
#define ConioSetScreenInfo(Console, Buff, OldCursorX, OldCursorY) \
    (Console)->TermIFace.Vtbl->SetScreenInfo((Console), (Buff), (OldCursorX), (OldCursorY))
#define ConioResizeTerminal(Console) \
    (Console)->TermIFace.Vtbl->ResizeTerminal(Console)
#define ConioProcessKeyCallback(Console, Msg, KeyStateMenu, ShiftState, VirtualKeyCode, Down) \
    (Console)->TermIFace.Vtbl->ProcessKeyCallback((Console), (Msg), (KeyStateMenu), (ShiftState), (VirtualKeyCode), (Down))
#define ConioRefreshInternalInfo(Console) \
    (Console)->TermIFace.Vtbl->RefreshInternalInfo(Console)

#define ConioChangeTitle(Console) \
    (Console)->TermIFace.Vtbl->ChangeTitle(Console)
#define ConioChangeIcon(Console, hWindowIcon) \
    (Console)->TermIFace.Vtbl->ChangeIcon((Console), (hWindowIcon))
#define ConioGetConsoleWindowHandle(Console) \
    (Console)->TermIFace.Vtbl->GetConsoleWindowHandle(Console)
#define ConioGetLargestConsoleWindowSize(Console, pSize) \
    (Console)->TermIFace.Vtbl->GetLargestConsoleWindowSize((Console), (pSize))
#define ConioGetDisplayMode(Console) \
    (Console)->TermIFace.Vtbl->GetDisplayMode(Console)
#define ConioSetDisplayMode(Console, NewMode) \
    (Console)->TermIFace.Vtbl->SetDisplayMode((Console), (NewMode))
#define ConioShowMouseCursor(Console, Show) \
    (Console)->TermIFace.Vtbl->ShowMouseCursor((Console), (Show))
#define ConioSetMouseCursor(Console, hCursor) \
    (Console)->TermIFace.Vtbl->SetMouseCursor((Console), (hCursor))
#define ConioMenuControl(Console, CmdIdLow, CmdIdHigh) \
    (Console)->TermIFace.Vtbl->MenuControl((Console), (CmdIdLow), (CmdIdHigh))
#define ConioSetMenuClose(Console, Enable) \
    (Console)->TermIFace.Vtbl->SetMenuClose((Console), (Enable))

/* EOF */
