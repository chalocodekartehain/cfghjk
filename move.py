import os
import shutil
fromdir="C:/Users/dell/Desktop"
todir="C:/Users/dell/Downloads"
list=os.listdir(fromdir)
for filename in list:
 name, extension = os.path.splitext(filename)
 if extension=='':
    continue
 if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
    path1 = fromdir + '/' + filename
    path2 = todir + '/' + "Image_Files"
    path3 = todir + '/' + "Image_Files" + '/' + filename
    if os.path.exists(path2):
        print("Moving " + filename + ".....")
        shutil.move(path1,path3)
    else:
        os.mkdir(path2)
        print("Moving " + filename + ".....")
        shutil.move(path1,path3)

 