<?xml version="1.0"?>
<!DOCTYPE module SYSTEM "../../../tools/rbuild/project.dtd">
<group>
<module name="advpack_winetest" type="win32cui" installbase="bin" installname="advpack_winetest.exe" allowwarnings="true">
	<include base="advpack_winetest">.</include>
	<file>files.c</file>
	<file>install.c</file>
	<file>testlist.c</file>
	<library>wine</library>
	<library>cabinet</library>
	<library>advapi32</library>
	<library>kernel32</library>
	<library>ntdll</library>
</module>
</group>
