
remove_definitions(-D_WIN32_WINNT=0x502)
add_definitions(-D_WIN32_WINNT=0x600)

add_definitions(-D__WINESRC__)
include_directories(${REACTOS_SOURCE_DIR}/include/reactos/wine)

spec2def(dinput.dll dinput.spec ADD_IMPORTLIB)

add_library(dinput SHARED
    config.c
    data_formats.c
    device.c
    dinput_main.c
    effect_linuxinput.c
    joystick.c
    joystick_linux.c
    joystick_linuxinput.c
    joystick_osx.c
    keyboard.c
    mouse.c
    dinput.rc
    ${CMAKE_CURRENT_BINARY_DIR}/dinput.def)

add_library(dinput_data_formats data_formats.c)
add_dependencies(dinput_data_formats psdk)
set_module_type(dinput win32dll UNICODE)
target_link_libraries(dinput dxguid uuid wine)
add_importlibs(dinput comctl32 ole32 user32 advapi32 msvcrt kernel32 ntdll)
add_cd_file(TARGET dinput DESTINATION reactos/system32 FOR all)
