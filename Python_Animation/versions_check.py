# PyQt6 Version check
from PyQt6.QtCore import QT_VERSION_STR
print("PyQt6 version:", QT_VERSION_STR)

# PySide6 Version check
import PySide6
print("PySide6 version:", PySide6.__version__)

# Python Version check
import sys
print("Python version:", sys.version)

# Windows Version check
import platform
print("Windows version:", platform.platform())