import subprocess as sp
import os
import time as t
temp = "/home/edward-penny"

answer = ""
isafile = False
print("Welcome, here you can choose files and get information about them! Make sure you use the correct capitalisation. press enter to begin")
input()

directory = "/home/edward-penny"
#begins the user at home
while not isafile:
    choice = ""
    folders = sp.run(["find", directory, "-not", "-name", '.*', "-type", "d", "-maxdepth", "1"], stdout = sp.PIPE, text=True)
    files = sp.run(["find", directory, "-not", "-name", '.*', "-type", "f", "-maxdepth", "1"], stdout=sp.PIPE, text=True)
    files = files.stdout.splitlines()
    folders = folders.stdout.splitlines()
    print("Here are the files:")
    for i in range(0, len(files)):
        type = sp.run(["file", files[i]], stdout=sp.PIPE, text=True)
        print(f"File: {files[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{files[i]}:", "")}")
    print("Here are the folders:")
    for i in range(1, len(folders)):
        type = sp.run(["file", folders[i]], stdout=sp.PIPE, text=True)
        print(f"Folder: {folders[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{folders[i]}:", "")}")
    print("Leave")
    check = sp.run(["ls", directory], stdout=sp.PIPE, text=True)
    items = check.stdout
    if items == "":
        print("Sorry there is nothing in this folder\n"
              "Try a different path")
        directory = "/home/edward-penny"
    else:
        #shows all the files in the folder
        temp2 = directory
        temp3 = answer
        answer = input("Where would you like to go?\n")
        if answer == "Leave":
            answer = "LeaveY"
            if directory == "/home":
                print("Sorry you can't leave here")
                answer = ""
            else:
                if "Leave" not in items:
                    directory = str(directory)
                    directory = directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '')
                    #removes the last item from the directory
                    print("Leaving")
                elif "Leave" in items:
                    while choice != "1" and choice != "2":
                        choice = input("Would you like to access leave or leave? (1,2)")
                        choice = choice.lower()
                        if choice == "1":
                            answer = "Leave"
                        elif choice == "2":
                            directory = str(directory)
                            directory = directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '')
                            print("Leaving")
                        else:
                            print("invalid answer, try again")
        if answer != "LeaveY":
            temp = directory
            if answer != "":
                directory = f"{directory}/{answer}"
            else:
                directory = directory
            #sets the directory to what the user chooses
            pathexists = os.path.exists(directory)
            if not pathexists:
                print("Path does not exist, try again")
                directory = temp2
            isafile = os.path.isfile(directory)
            #checks if the path is a file

            if isafile:
                size = os.path.getsize(directory)
                date = t.ctime(os.path.getmtime(directory))
                print(f"The file's size is {size} bytes, the location is {directory}, and it was last modified on {date}")