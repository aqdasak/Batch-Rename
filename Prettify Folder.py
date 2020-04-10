import os


def batch_rename(files, avoid, start):
    i = start
    for file in files:
        if file not in avoid:
            os.rename(file, f"{i}{os.path.splitext(file)[1]}")
            i += 1


def capital(files, avoid):
    for file in files:
        if file not in avoid:
            os.rename(file, file.capitalize())


if __name__ == '__main__':
    print("1. Batch Rename\n2. Capitalize I letter")
    userChoice = input()
    print("Input the path of the folder that contains the files to be renamed")
    path = input()
    print(
        "If you want to ignore some files, add name of those files in pfavd.txt \nin the same folder in which files to be renamed are present.")
    os.chdir(path)
    files = os.listdir(path)
    print(files)
    avoid = []
    try:
        with open("pfavd.txt") as f:
            avoid = f.read().split("\n")
            # print("1>>>>>",avoid)
    except:
        print("No file ignored")
    avoid.append("pfavd.txt")
    # print("2>>>>>", avoid)

    if userChoice == "1":
        start = int(input("Enter a number from which renaming counter will start : "))
        batch_rename(files, avoid, start)
    elif userChoice == "2":
        capital(files, avoid)
