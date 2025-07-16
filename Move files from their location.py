import subprocess as sp
import os
import time as t
temp = "/home"
enter = 0
action = 0
answer = 0
sure = 0
overwrite = 0
num = 0
reallocation = False

isafile = False
print("Welcome, here you can choose files and get information about them! Make sure you use the correct capitalisation. press enter to begin")
input()
directory = "/home"
#begins the user at home
while not isafile:
    choice = ""
    folders = sp.run(["find", directory, "-not", "-name", '.*', "-type", "d", "-maxdepth", "1"], stdout = sp.PIPE, text=True)
    files = sp.run(["find", directory, "-not", "-name", '.*', "-type", "f", "-maxdepth", "1"], stdout=sp.PIPE, text=True)
    files = files.stdout.splitlines()
    folders = folders.stdout.splitlines()
    print("Here are the files:\n")
    for i in range(0, len(files)):
        type = sp.run(["file", files[i]], stdout=sp.PIPE, text=True)
        print(f"File: {files[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{files[i]}:", "")}")
    print("Here are the folders:\n")
    for i in range(1, len(folders)):
        type = sp.run(["file", folders[i]], stdout=sp.PIPE, text=True)
        print(f"Folder: {folders[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{folders[i]}:", "")}")
    print("Leave")
    check = sp.run(["ls", directory], stdout=sp.PIPE, text=True)
    items = check.stdout
    if items == "":
        print("Sorry there is nothing in this folder\n"
              "Try a different path")
        directory = "/home"
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
                while enter != "y" and enter != "n":
                    enter = input("Would you like to continue? (Y/N)\n")
                    enter = enter.lower()
                    if enter == "y":
                        while num != "1" and num != "2" and num != "3":
                            num = input("Would you like to:\n 1. Open the file\n 2. Move the file\n 3. End process\n")
                            if num == "1":
                                print("Opening")
                                sp.run(["xdg-open", directory])
                                num = 4
                            elif num == "2":
                                while not reallocation:
                                    here = False
                                    temp1 = "/home"
                                    answer1 = 0
                                    location = "/home"
                                    # begins the user at home
                                    while not here:
                                        choice1 = ""
                                        folders1 = sp.run(
                                            ["find", location, "-not", "-name", '.*', "-type", "d", "-maxdepth", "1"], stdout=sp.PIPE, text=True)
                                        folders1 = folders1.stdout.splitlines()
                                        print("Here are the folders:\n")
                                        for i in range(1, len(folders1)):
                                            type1 = sp.run(["file", folders1[i]], stdout=sp.PIPE, text=True)
                                            print(
                                                f"Folder: {folders1[i].replace(f"{location}/", "")}\nType: {type1.stdout.replace(f"{folders1[i]}:", "")}")
                                        print("Place it here? (Y)\n")
                                        print("Leave")
                                        check1 = sp.run(["ls", location], stdout=sp.PIPE, text=True)
                                        items1 = check1.stdout
                                        # shows all the files in the folder
                                        temp4 = location
                                        temp5 = answer1
                                        answer1 = input("Where would you like to go?\n")
                                        if answer1 == "Leave":
                                            answer1 = "LeaveY"
                                            if location == "/home":
                                                print("Sorry you can't leave here")
                                                answer1 = ""
                                            else:
                                                if "Leave" not in items1:
                                                    location = str(location)
                                                    location = location.replace(f"/{location.rsplit('/', 1)[-1]}", '')
                                                    # removes the last item from the directory
                                                    print("Leaving")
                                                elif "Leave" in items1:
                                                    while choice1 != "1" and choice1 != "2":
                                                        choice1 = input("Would you like to access leave or leave? (1,2)")
                                                        choice1 = choice1.lower()
                                                        if choice1 == "1":
                                                            answer1 = "Leave"
                                                        elif choice1 == "2":
                                                            location = str(location)
                                                            location = location.replace(f"/{location.rsplit('/', 1)[-1]}", '')
                                                            print("Leaving")
                                                        else:
                                                            print("invalid answer, try again")
                                        if answer1 == "Y":
                                            if location != directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '') and location != "/home":
                                                here = True
                                                reallocation = True
                                                print(f"Moved {directory} to {location}")
                                                sp.run(["mv", directory, location])
                                                num = 4
                                            else:
                                                print("Cannot move here")
                                                num = 4
                                        elif answer1 != "LeaveY":
                                            temp1 = location
                                            if answer1 != "":
                                                location = f"{location}/{answer1}"
                                            else:
                                                location = location
                                                # sets the directory to what the user chooses
                                                pathexists1 = os.path.exists(location)
                                                if not pathexists1:
                                                    print(location)
                                                    print("Path does not exist, try again")
                                                    location = temp4
                            elif num == "3":
                                print("Ending process")
                            else:
                                print("Please enter a valid number")

                    elif enter == "n":
                        print("Ending process")