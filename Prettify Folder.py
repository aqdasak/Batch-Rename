import os


def soldier(path, exceptFile, ext):
    os.chdir(path)
    files = os.listdir(path)
    i = 1
    with open(exceptFile) as f:
        exceptFileList = f.read().split("\n")
    for file in files:
        if file not in exceptFileList:
            os.rename(file, file.capitalize())
            if os.path.splitext(file)[1] == ext:
                os.rename(file, f"{i}{ext}")
                i += 1


soldier("D:\\snak","a.txt", ".ico")

