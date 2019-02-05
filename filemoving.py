import os
import shutil

MAIN=r'C:\Users\admin\Desktop\file'

MAIN1=r'C:\Users\admin\Desktop\file\file1a'
MAIN2=r'C:\Users\admin\Desktop\file\file2b'

DIRS =r'C:\Users\admin\Desktop\interview call letter'

for root, subdirs, files in os.walk(DIRS):
    print('root', root)
    print('subdirs', subdirs)
    print('files', files)
    for file in files:
        if file.startswith("a"):
            path = os.path.join(root,file)
            shutil.move(path, MAIN1)
        if file.startswith("b"):
            path = os.path.join(root,file)
            shutil.move(path, MAIN2)
        else:
            path = os.path.join(root,file)
            shutil.move(path, MAIN)
