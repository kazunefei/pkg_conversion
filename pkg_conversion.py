import json
from pathlib import Path
import os
import sys
script_dir = os.path.dirname(sys.argv[0])
os.chdir(script_dir)
json_name = input("Enter JSON file name ")
output_name = input("Enter desired .h file name ")
pkg = open(f'{json_name}')
pkg_data =  json.load(pkg)

version = pkg_data['version']
version.split('.')
major = version.split('.')[0]
minor = version.split('.')[1]
patch = version.split('.')[2]

path = f'./{output_name}'
if os.path.isfile(path)==True:
    ver = open(f"{output_name}", "w")
    ver.write("#ifndef VERSION_H")
    ver.write("\n")
    ver.write("#define VERSION_H")
    ver.write("\n")
    ver.write("\n")
    ver.write(f"#define VER_MAJOR   {major}")
    ver.write("\n")
    ver.write(f"#define VER_MINOR   {minor}")
    ver.write("\n")
    ver.write(f"#define VER_PATCH   {patch}")
    ver.write("\n")
    ver.write("#define VER_BUILD   0")
    ver.write("\n")
    ver.write("\n")
    ver.write("\n")
    ver.write("\n")
    ver.write("#endif // VERSION_H")
    ver.close()

path = f'./{output_name}'
if os.path.isfile(path)==False:
    ver = open(f"{output_name}", "x")
    ver.write("#ifndef VERSION_H")
    ver.write("\n")
    ver.write("#define VERSION_H")
    ver.write("\n")
    ver.write("\n")
    ver.write(f"#define VER_MAJOR   {major}")
    ver.write("\n")
    ver.write(f"#define VER_MINOR   {minor}")
    ver.write("\n")
    ver.write(f"#define VER_PATCH   {patch}")
    ver.write("\n")
    ver.write("#define VER_BUILD   0")
    ver.write("\n")
    ver.write("\n")
    ver.write("\n")
    ver.write("\n")
    ver.write("#endif // VERSION_H")
    ver.close()