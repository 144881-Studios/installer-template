# Template source code:
```python
# Start
from os import *
print("Welcome to Install Wizard")
raw = input(r"Please input the install directory(e.g.“C:\Program Files\”):") # Choose install directory
os.system("md "+raw+("\\"*(raw[-1]!="\\"))+"My Program\\") # Your Directory(Directories)
os.system("echo Hello World>>"+raw+("\\"*(raw[-1]!="\\"))+"My Program\\MyFile.txt") # Your Files
input("Done!")
# End
```
<a href="https://144881-studios.github.io/installer-template/python/installer.py" download="installer.py">Download template</a>
