import subprocess as sp
import os
import time as t
import datetime as dt

temp = "/home"
enter = 0
action = 0
answer = 0
sure = 0
overwrite = 0
num = 0
move = 0
sure2 = 0
sure3 = 0
reallocation = False
isafile = False
removelogthere = False
filethere = False

removelog = []
def moveitem(directory):
    reallocation = False
    print("Here you can find where you want to move your item")
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
                if location != directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '') and location != "/home" and directory not in location and directory != "/home/edward-penny" and directory != "RemoveLog":
                    here = True
                    reallocation = True
                    print(f"Moved {directory} to {location}")
                    sp.run(["mv", directory, location])
                    num = 4
                elif directory == "/home/edward-penny":
                    print("Cannot move this")
                elif directory == "RemoveLog":
                    sp.run(["touch", f"{location}/RemoveLog"])
                    here = True
                    reallocation = True
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
                    print(location)
    return location

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
                directory = temp
            else:
                isafile = os.path.isfile(directory)
                #checks if the path is a file
                if not isafile:
                    folderaction = 0
                    removelogthere = False
                    #move folder the same way as files
                    #make sure they can't move /home/edward-penny
                    #make sure not moved to same location

                    if directory !=  "/home" and directory != "/home/edward-penny":
                        while folderaction != "1" and folderaction != "2" and folderaction != "3" and folderaction != "4":
                            folderaction = input("What would you like to do with the folder?\n 1. Enter it\n 2. Move it\n 3. Remove folder\n 4. End process\n")
                            if folderaction == "1":
                                print("Opening folder")
                                break
                            elif folderaction == "2":
                                directory = moveitem(directory)
                                print(f"Returning to {directory}")
                            elif folderaction == "3":
                                sure3 = 0
                                filecheck = sp.run(["find", directory, "-not", "-name", '.*', "-type", "f"],stdout=sp.PIPE, text=True)
                                filecheck = filecheck.stdout.splitlines()
                                for i in range(0, len(filecheck)):
                                    if __file__ in filecheck[i]:
                                        filethere = True
                                        print("You cannot delete this\n")
                                        print(f"returning to {directory}")
                                if not filethere:
                                    while sure3 != "y" and sure3 != "n":
                                        sure3 = input("Are you sure you want to remove the folder? (Y/N)\n")
                                        sure3 = sure3.lower()
                                        if sure3 == "y":
                                            print(f"{directory} removed")
                                            while not removelogthere:
                                                removelogcheck = sp.run( ["find", "/home", "-not", "-name", '.*', "-type", "f"], stdout=sp.PIPE, text=True)
                                                removelogcheck = removelogcheck.stdout.splitlines()
                                                for i in range(0, len(removelogcheck)):
                                                    if "RemoveLog" in removelogcheck[i]:
                                                        removeloglocation = removelogcheck[i]
                                                        removelogthere = True
                                                        print(removeloglocation)
                                                if removelogthere:
                                                    removelog = open(removeloglocation, "a")
                                                    now = dt.datetime.now()
                                                    removelog.write(f"{directory} removed at {now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-7]}\n")
                                                    removelog.close()
                                                else:
                                                    print("There is no remove log, choose where do you want to put it:\n")
                                                    moveitem("RemoveLog")
                                            sp.run(["rm", "-r", directory])
                                            directory = temp
                                            print(f"Returning to {directory}")
                                        elif sure3 == "n":
                                            print(f"Returning to {directory}")
                                        else:
                                            print("Please enter a valid answer")
                            elif folderaction == "4":
                                isafile = True
                            else:
                                print("Enter a valid answer")
                    else:
                        while folderaction != "1" and folderaction != "2":
                            folderaction = input("What would you like to do with the folder?\n 1. Enter it\n 2. End process\n")
                            if folderaction == "1":
                                print("Opening folder")
                                break
                            elif folderaction == "2":
                                isafile = True
                            else:
                                print("Enter a valid answer")
                elif isafile:
                    enter = 0
                    num = 0

                    size = os.path.getsize(directory)
                    date = t.ctime(os.path.getmtime(directory))
                    print(f"The file's size is {size} bytes, the location is {directory}, and it was last modified on {date}")
                    while enter != "y" and enter != "n":
                        enter = input("Would you like to continue? (Y/N)\n")
                        enter = enter.lower()
                        if enter == "y" and directory != __file__ and "RemoveLog" not in directory:
                            while num != "1" and num != "2" and num != "3" and num != "4":
                                num = input("Would you like to:\n 1. Open the file\n 2. Move the file\n 3. Remove the file\n 4. End process\n")
                                if num == "1":
                                    print("Opening")
                                    sp.run(["xdg-open", directory])
                                    num = 4
                                elif num == "2":
                                    blank = moveitem(directory)
                                    num = 4
                                elif num == "3":
                                    sure2 = 0
                                    while sure2 != "y" and sure2 != "n":
                                        sure2 = input("Are you sure you want to remove the file? (Y/N)\n")
                                        sure2 = sure2.lower()
                                        if sure2 == "y":
                                            while not removelogthere:
                                                removelogcheck = sp.run( ["find", "/home", "-not", "-name", '.*', "-type", "f"], stdout=sp.PIPE, text=True)
                                                removelogcheck = removelogcheck.stdout.splitlines()
                                                for i in range(0, len(removelogcheck)):
                                                    if "RemoveLog" in removelogcheck[i]:
                                                        removeloglocation = removelogcheck[i]
                                                        removelogthere = True
                                                if removelogthere:
                                                    removelog = open(removeloglocation, "a")
                                                    now = dt.datetime.now()
                                                    removelog.write(f"{directory} removed at {now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-7]}\n")
                                                    removelog.close()
                                                else:
                                                    print("There is no remove log, choose where do you want to put it:\n")
                                                    moveitem("RemoveLog")
                                            sp.run(["rm", "-r", directory])
                                            print(f"{directory} removed")
                                            isafile = False
                                            directory = "/home"
                                            print("Returning to home\n")
                                        elif sure == "n":
                                            num = 4
                                        else:
                                            print("Enter a valid answer\n")
                                elif num == "4":
                                    print("Ending process")
                                else:
                                    print("Please enter a valid number")
                        elif enter == "y" and directory == __file__:
                            print("Cannot access current file")
                        elif enter == "n":
                            print("Ending process")
                        else:
                            print("Please enter a valid answer")