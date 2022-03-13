"""
Give the user an win32 OS-warning dialog box
Schedule this script so that you can remind a user to create a periodic backup
"""

import ctypes  # An included library with Python install.

title = "Ext.HD Backup reminder"
text = "Copy the backup-drive (E) to the WD external HD"

ctypes.windll.user32.MessageBoxA(0, text, title, 1)
