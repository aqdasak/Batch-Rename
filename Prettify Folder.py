import os


def capital(path, avoid):
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        if file not in avoid:
            os.rename(file, file.capitalize())


def batch_rename(path, avoid):
    os.chdir(path)
    files = os.listdir(path)
    i = 1
    for file in files:
        if file not in avoid:
            os.rename(file, f"i{os.path.splitext(file)[1]}")
            i += 1


# soldier("D:\zsnak", "a.txt", ".ico")

if __name__ == '__main__':
    print("1. Batch Rename\n2. Capitalize I letter")
    userChoice = input()
    print("Input the path of the folder that contains the files to be renamed")
    path = input()
    a = input("Do you want add some files in the ignore list (y/n): ")
    if a == "y":
        exceptFileList = []
        print("Enter ':q' to exit")
        while True:
            st = input()
            if st == ':q':
                break
            exceptFileList.append(st)
    if userChoice == "1":
        batch_rename(path, exceptFileList)
    elif userChoice == "2":
        capital(path, exceptFileList)
