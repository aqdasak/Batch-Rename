import os
from time import sleep


def batch_rename(files, avoid, start):
    i = start
    for file in files:
        if file not in avoid:
            try:
                os.rename(file, f"{i}{os.path.splitext(file)[1]}")
            except Exception as e:
                print(e)
            else:
                print(f"{file} renamed")
            i += 1


def capital(files, avoid):
    for file in files:
        if file not in avoid:
            try:
                os.rename(file, file.capitalize())
            except Exception as  e:
                print(e)
            else:
                print(f"{file} capitalized")

def arrange_by_extension(files):
    # Using list comprehension to get a list of extionsions of all files and saving them into a set to avoid repetitive values
    ext_set = set([os.path.splitext(file)[1] for file in files])
    # Converting set into list as 'set' object is not subscriptable
    ext_set = list(ext_set)

    files2 = []
    i = 0
    while i < len(ext_set):
        for file in files:
            if os.path.splitext(file)[1] == ext_set[i]:
                files2.append(file)
        i += 1
    return files2


if __name__ == '__main__':
    print("1. Batch Rename\n2. Capitalize I letter")
    userChoice = input()
    if userChoice not in ["1","2"]:
        print("Wrong input")
        exit()
    print(
        "# If you want to ignore some files, add name of those files in pfavd.txt in the same\n# folder in which files to be renamed are present. For now wildcards can't be used.\n")
    print("Input the path of the folder that contains the files to be renamed")
    path = input()

    os.chdir(path)
    files = arrange_by_extension(os.listdir(path))

    avoid = []
    try:
        with open("pfavd.txt") as f:
            avoid = f.read().split("\n")
    except:
        print("No file ignored")
    avoid.append("pfavd.txt")


    if userChoice == "1":
        start = int(input("Enter a number from which renaming counter will start : "))
        cnfrm = input("This can't be undone. Are you sure(y/n) : ").lower()
        if cnfrm == "y" or cnfrm == "yes":
            batch_rename(files, avoid, start)
        else:
            print("Nothing renamed")
    elif userChoice == "2":
        capital(files, avoid)
sleep(2)
