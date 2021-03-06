#####################################
### Usage
### python cx_setup.py build
###
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","Arduino"],
                      "excludes": ["tkinter"],
                      "icon": "py.ico"}
install_exe_options = {}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Laser Control",
        version = "0.1",
        description = "Control AOTF Flexibly!",
        options = {
                   "build_exe" :build_exe_options
                   },
        executables = [Executable("Main.py", base=base, compress = True)])
