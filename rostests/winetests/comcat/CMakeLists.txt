
add_definitions(
    -D__ROS_LONG64__
    -D_DLL -D__USE_CRTIMP)

add_executable(comcat_winetest comcat.c testlist.c)
target_link_libraries(comcat_winetest wine uuid)
set_module_type(comcat_winetest win32cui)
add_importlibs(comcat_winetest ole32 advapi32 msvcrt kernel32 ntdll)
add_cd_file(TARGET comcat_winetest DESTINATION reactos/bin FOR all)
