import subprocess as sp
import wget
from os.path import exists

# wget.download("http://192.168.29.62:8000/python.txt", "python.txt")
# sp.Popen(["notepad.exe", "python.txt"])
print(exists("python.txt"))