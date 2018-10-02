# working with os module
import os
for dirpath,dirnames,filenames in os.walk('C:/Desktop'):
    print("Current working directory path: ",dirpath)
    print("Directories: ",dirnames)
    print("File names: ",filenames)
    print()
    
