import os
import shutil
diractory= input("Please folder name:")
ol=os.listdir(diractory)
for i in ol:
    file, Extenstion=os.path.splitext(i)
    Extenstion= Extenstion[1:]
    if Extenstion=="":
        continue
    if os.path.exists(diractory+"/"+Extenstion):
        shutil.move(diractory+"/"+i, diractory+"/"+Extenstion+"/"+i)

    else:
        os.makedirs(diractory+"/"+Extenstion)
        shutil.move(diractory+"/"+i, diractory+"/"+Extenstion+"/"+i)

