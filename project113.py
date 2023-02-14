import os
import shutil

from_dir = "C:/Users/Ethan/Downloads/"
to_dir = "C:/Users/Ethan/Downloads/"

list_of_files = os.listdir(from_dir)

for filenames in list_of_files:
    name, extension = os.path.splitext(filenames)

    if extension == "":
        continue
    if extension in [".doc"]:
        path1 = from_dir + "/" + filenames
        path2 = to_dir + "/" + "doc_files"
        path3 = to_dir + "/" + "doc_files" + "/" + filenames

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)