
add_definitions(-D__WINESRC__)
include_directories(${REACTOS_SOURCE_DIR}/include/reactos/wine)
spec2def(faultrep.dll faultrep.spec)

list(APPEND SOURCE
    faultrep.c
    ${CMAKE_CURRENT_BINARY_DIR}/faultrep_stubs.c
    ${CMAKE_CURRENT_BINARY_DIR}/faultrep.def)

add_library(faultrep SHARED ${SOURCE})
set_module_type(faultrep win32dll)
target_link_libraries(faultrep wine)
add_importlibs(faultrep advapi32 msvcrt kernel32 ntdll)
add_cd_file(TARGET faultrep DESTINATION reactos/system32 FOR all)
