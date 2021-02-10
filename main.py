from scripts import parser, run
import os
import sys
from scripts.config import config

if len(sys.argv) > 1:
    file = sys.argv[-1]
else:
    if os.name == 'nt' and config.get("Console", "use_fileopen_dialog") == 'yes':
        from tkinter.filedialog import askopenfilename
        from tkinter import Tk
        window = Tk()
        window.withdraw()
        # window.iconbitmap('icon.ico')
        file = askopenfilename()
    else:
        file = input("Enter file name: ")

run.run(*parser.parse(file))
input("Press ENTER to exit...")
