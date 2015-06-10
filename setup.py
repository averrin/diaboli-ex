from cx_Freeze import setup, Executable
import os, sys
includefiles = ['locations', 'templates']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "diaboli-ex",
    version = "0.1",
    description = "Diabloi Ex",
    options = {"build_exe" : {"includes" : "PyQt5.QtPrintSupport", 'include_files':includefiles}},
    executables = [Executable("main.py", base = base)],
)
