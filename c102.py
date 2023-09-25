import os
import shutil
#print (dir(os))
path = os.getcwd()
#print ("The path of the file is", path)
#os.mkdir('noah')
file = os.listdir("C:/Users/User/Downloads")
#print (file)
isexists= os.path.exists("C:/Users/User/Downloads/abc")

print (isexists)
root,ext=os.path.splitext("C:/Users/User/Downloads/desktop.ini")
print ("The root of the file is", root)
print ("The extension of the file is", ext)

source="C:/Users/User/Downloads/abc"
destination = "C:/Users/User/Desktop"
files= os.listdir(source)
for file_names in files:
    name,ext=os.path.splitext(file_names)
    if ext== '':
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1=source + '/' + file_names
        path2=destination + '/' + 'image_files'
        path3=destination + '/' + 'image_files' + '/' + file_names

        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Creating folder and moving' )
            shutil.move(path1,path3)