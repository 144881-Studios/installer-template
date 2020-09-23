# Start
from os import *
print("Welcome to Install Wizard")
raw = input(r"Please input the install directory(e.g.“C:\Program Files\”):")
os.system("md "+raw+("\\"*(raw[-1]!="\\"))+"My Program\\")
os.system("echo Hello World>>"+raw+("\\"*(raw[-1]!="\\"))+"My Program\\MyFile.txt"
