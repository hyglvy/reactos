
spec2def(d3dx9_25.dll d3dx9_25.spec)

list(APPEND SOURCE
    d3dx9_25_main.c
    version.rc
    ${CMAKE_CURRENT_BINARY_DIR}/d3dx9_25_stubs.c
    ${CMAKE_CURRENT_BINARY_DIR}/d3dx9_25.def)

add_definitions(-D__WINESRC__)
include_directories(${REACTOS_SOURCE_DIR}/include/reactos/wine)
add_library(d3dx9_25 SHARED ${SOURCE})
set_module_type(d3dx9_25 win32dll)
target_link_libraries(d3dx9_25 wine)

add_importlibs(d3dx9_25
    d3dx9_36
    d3dx9_24
    d3d9
    user32
    gdi32
    advapi32
    msvcrt
    kernel32
    ntdll)

add_dependencies(d3dx9_25 wineheaders)
add_cd_file(TARGET d3dx9_25 DESTINATION reactos/system32 FOR all)
