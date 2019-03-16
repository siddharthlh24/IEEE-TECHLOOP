import subprocess
import os


pdf = "rv.txt"
npPath = r'C:\Program Files\Notepad++\notepad++.exe'
subprocess.Popen("%s %s" % (npPath, pdf))

