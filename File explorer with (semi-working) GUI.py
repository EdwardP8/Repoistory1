import subprocess as sp
import os
import time as t
import datetime as dt
import tkinter as tk

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
buttonpressed = False
Leave = False
RemoveLogthere2 = False

def folderactionc(action):
    global folderaction
    folderaction = action
    filesearcher.destroy()
def directoryassign(directory2):
    global answer
    answer = directory2
    filesearcher.destroy()

def directoryassign1(directory2):
    global answer1
    answer1 = directory2
    filesearcher1.destroy()
def leavetrue():
    global answer
    answer = "Leave12345real"
    filesearcher.destroy()

def leavetrue1():
    global answer1
    answer1 = "Leave12345real"
    filesearcher1.destroy()
def answertoy():
    global answer1
    answer1 = "Y"
    filesearcher1.destroy()
def sure2assign(value):
    global sure2
    sure2 = value
    sure2window.destroy()
def sure3assign(value):
    global sure3
    sure3 = value
    filesearcher.destroy()
def enterset(value):
    global enter
    enter = value
    fileinformationwindow.destroy()
def fileactionc(value):
    global num
    num = value
    fileoptionswindow.destroy()
def moveitem(directory):
    global answer1
    reallocation = False
    while not reallocation:
        here = False
        temp1 = "/home"
        location = "/home"
        # begins the user at home
        while not here:
            choice1 = ""
            folders1 = sp.run(
                ["find", location, "-not", "-name", '.*', "-type", "d", "-maxdepth", "1"], stdout=sp.PIPE, text=True)
            folders1 = folders1.stdout.splitlines()
            global filesearcher1
            filesearcher1 = tk.Tk()
            filesearcher1.title("File Searcher")
            filelabel = tk.Label(filesearcher1, text="Here are the files:")
            filelabel.pack()
            row = 2
            column = 0
            for i in range(1, len(folders1)):
                if i % 10 == 0:
                    column += 1
                    row = 0
                row += 1
                type = sp.run(["file", folders1[i]], stdout=sp.PIPE, text=True)
                folder = tk.Button(filesearcher1,
                                   text=f"Folder: {folders1[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{folders1[i]}:", "")}",
                                   command=lambda h=i: directoryassign1(folders1[h]))
                folder.grid(row = row, column = column)
            hereanswer = tk.Button(filesearcher1, text="Place it here", command=answertoy)
            hereanswer.pack()
            leave1 = tk.Button(filesearcher1, text="Leave", command=leavetrue1)
            leave1.pack()
            filesearcher1.mainloop()
            check1 = sp.run(["ls", location], stdout=sp.PIPE, text=True)
            items1 = check1.stdout
            # shows all the files in the folder
            temp4 = location
            if answer1 == "Leave12345real":
                if location != "/home":
                    location = str(location)
                    location = location.replace(f"/{location.rsplit('/', 1)[-1]}", '')
                else:
                    location = "/home"
            if answer1 == "Y":
                if location != directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '') and location != "/home" and directory not in location and directory != "/home/edward-penny" and directory != "RemoveLog":
                    here = True
                    reallocation = True
                    sp.run(["mv", directory, location])
                    num = 4
                elif directory == "/home/edward-penny":
                    x = 1
                elif directory == "RemoveLog":
                    sp.run(["touch", f"{location}/RemoveLog"])
                    here = True
                    reallocation = True
                else:
                    num = 4
            elif answer1 != "Leave12345real":
                temp1 = location
                if answer1 != "":
                    location = f"{answer1}"
                    here = False
                else:
                    location = location
                    # sets the directory to what the user chooses
                pathexists1 = os.path.exists(location)
                if not pathexists1:
                    location = temp4
    return location

begin = tk.Tk()
begin.title("File Searcher")
begin.geometry("300x222")
label = tk.Label(begin, text="Welcome to the File Searcher, click to begin:", padx=150, pady=50)
label.place(x=-135, y=20)
button = tk.Button(begin, text="Begin", command=begin.destroy, padx=25, pady=15)
button.place(x=105, y=100)
begin.mainloop()

directory = "/home"
#begins the user at home
while not isafile:
    choice = ""
    folders = sp.run(["find", directory, "-not", "-name", '.*', "-type", "d", "-maxdepth", "1"], stdout = sp.PIPE, text=True)
    files = sp.run(["find", directory, "-not", "-name", '.*', "-type", "f", "-maxdepth", "1"], stdout=sp.PIPE, text=True)
    files = files.stdout.splitlines()
    folders = folders.stdout.splitlines()
    filesearcher = tk.Tk()
    filesearcher.title("File Searcher")
    filelabel = tk.Label(filesearcher, text="Here are the items:")
    row = 0
    column = 1
    for i in range(0, len(files)):
        if row == 10:
            column += 1
            row = 0
        row += 1
        type = sp.run(["file", files[i]], stdout=sp.PIPE, text=True)

        file = tk.Button(filesearcher, text=f"File: {files[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{files[i]}:", "")}", padx=15, pady=10,  width=25, wraplength=250, command=lambda h=i : directoryassign(files[h]))
        file.grid(row=row, column=column)
    for i in range(1, len(folders)):
            if row == 10:
                column += 1
                row = 0
            row += 1
            type = sp.run(["file", folders[i]], stdout=sp.PIPE, text=True)
            folder = tk.Button(filesearcher, text=f"Folder: {folders[i].replace(f"{directory}/", "")}\nType: {type.stdout.replace(f"{folders[i]}:","")}",padx=15, pady=10, width=25, wraplength=350, command=lambda h=i : directoryassign(folders[h]))
            folder.grid(row=row, column=column, pady=5, padx=5)
    leave = tk.Button(filesearcher, text="Leave", command=leavetrue)
    leave.grid(row=10, column = column)
    if len(folders) == 2:
        filelabel.grid(row=0, column=1)
    else:
        filelabel.grid(row=0, column=1)
    filesearcher.mainloop()
    check = sp.run(["ls", directory], stdout=sp.PIPE, text=True)
    items = check.stdout
    #shows all the files in the folder
    temp2 = directory
    temp3 = answer
    if answer == "Leave12345real":
        if directory != "/home":
            directory = str(directory)
            directory = directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '')
        else:
            directory = "/home"
    if answer != "Leave12345real":
        temp = directory
        if answer != "":
            directory = f"{answer}"
        else:
            directory = directory
        #sets the directory to what the user chooses
        pathexists = os.path.exists(directory)
        if not pathexists:
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
                        filesearcher = tk.Tk()
                        filesearcher.title("File Searcher")
                        folderactionlabel = tk.Label(filesearcher, text="What would you like to do?" )
                        folderaction1 = tk.Button(filesearcher, text="1. Open the folder", command=lambda : folderactionc("1"))
                        folderaction2 = tk.Button(filesearcher, text="2. Move the folder", command=lambda : folderactionc("2"))
                        folderaction3 = tk.Button(filesearcher, text="3. Delete the folder", command=lambda : folderactionc("3"))
                        folderaction4 = tk.Button(filesearcher, text="4. End the process", command=lambda : folderactionc("4"))
                        folderactionlabel.pack()
                        folderaction1.pack()
                        folderaction2.pack()
                        folderaction3.pack()
                        folderaction4.pack()
                        filesearcher.mainloop()
                        if folderaction == "1":
                            break
                        elif folderaction == "2":
                            directory = moveitem(directory)
                        elif folderaction == "3":
                            sure3 = 0
                            filecheck = sp.run(["find", directory, "-not", "-name", '.*', "-type", "f"],stdout=sp.PIPE, text=True)
                            filecheck = filecheck.stdout.splitlines()
                            for i in range(0, len(filecheck)):
                                if __file__ in filecheck[i]:
                                    filethere = True
                                if "RemoveLog" in filecheck[i]:
                                    RemoveLogthere2 = True
                            if not filethere and not RemoveLogthere2:
                                while sure3 != "y" and sure3 != "n":
                                    filesearcher = tk.Tk()
                                    filesearcher.title("File Searcher")
                                    sure3lable = tk.Label(filesearcher, text="Are you sure you want to delete this folder?")
                                    sure3y = tk.Button(filesearcher, text="Yes", command=lambda : sure3assign("y"))
                                    sure3n = tk.Button(filesearcher, text="No", command=lambda : sure3assign("n"))
                                    sure3lable.pack()
                                    sure3y.pack()
                                    sure3n.pack()
                                    filesearcher.mainloop()
                                    if sure3 == "y":
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
                                                removelogwindow = tk.Tk()
                                                removelogwindow.title("File Searcher")
                                                removeloglabel = tk.Label(removelogwindow, text="There is no remove log, please create one")
                                                removelogcreate = tk.Button(removelogwindow, text="Create", command=removelogwindow.destroy)
                                                removeloglabel.pack()
                                                removelogcreate.pack()
                                                removelogwindow.mainloop()
                                                moveitem("RemoveLog")
                                        sp.run(["rm", "-r", directory])
                                        directory = temp

                                    elif sure3 == "n":
                                        directory = directory.replace(f"/{directory.rsplit('/', 1)[-1]}", '')
                            else:
                                nodeletewindow = tk.Tk()
                                nodeletewindow.title("File Searcher")
                                nodeletelabel = tk.Label(nodeletewindow, text="Cannot delete folder")
                                nodeletecontinue = tk.Button(nodeletewindow, text="Continue", command=nodeletewindow.destroy)
                                nodeletelabel.pack()
                                nodeletecontinue.pack()
                                nodeletewindow.mainloop()
                        elif folderaction == "4":
                            isafile = True
                        else:
                            x = 1
                else:
                    while folderaction != "1" and folderaction != "2":
                        filesearcher = tk.Tk()
                        filesearcher.title("File Searcher")
                        folderactionlabel = tk.Label(filesearcher, text="What would you like to do?" )
                        folderaction1 = tk.Button(filesearcher, text="1. Open the folder", command=lambda : folderactionc("1"))
                        folderaction2 = tk.Button(filesearcher, text="2. End the process", command=lambda : folderactionc("2"))
                        folderactionlabel.pack()
                        folderaction1.pack()
                        folderaction2.pack()
                        filesearcher.mainloop()
                        if folderaction == "1":
                            break
                        elif folderaction == "2":
                            isafile = True
                        else:
                            x = 1
            elif isafile:
                enter = 0
                num = 0

                size = os.path.getsize(directory)
                date = t.ctime(os.path.getmtime(directory))
                fileinformationwindow = tk.Tk()
                fileinformationwindow.title("File Searcher")
                fileinformationlabel = tk.Label(fileinformationwindow, text=f"The file's size is {size} bytes, the location is {directory}, and it was last modified on {date}")
                fileinformationlabel.pack()
                while enter != "y" and enter != "n":
                    enterlabel = tk.Label(fileinformationwindow, text="Would you like to continue?")
                    enterbuttony = tk.Button(fileinformationwindow, text="Yes", command=lambda : enterset("y"))
                    enterbuttonn  = tk.Button(fileinformationwindow, text="No", command=lambda : enterset("n"))
                    enterlabel.pack()
                    enterbuttony.pack()
                    enterbuttonn.pack()
                    fileinformationwindow.mainloop()
                    if enter == "y" and directory != __file__:
                        while num != "1" and num != "2" and num != "3" and num != "4":
                            fileoptionswindow = tk.Tk()
                            fileoptionswindow.title("File Searcher")
                            fileoptionslabel = tk.Label(fileoptionswindow, text="What would you like to do?")
                            fileaction1 = tk.Button(fileoptionswindow, text="1. Open the file",
                                                      command=lambda: fileactionc("1"))
                            fileaction2 = tk.Button(fileoptionswindow, text="2. Move the file",
                                                      command=lambda: fileactionc("2"))
                            fileaction3 = tk.Button(fileoptionswindow, text="3. Delete the file",
                                                      command=lambda: fileactionc("3"))
                            fileaction4 = tk.Button(fileoptionswindow, text="4. End the process",
                                                      command=lambda: fileactionc("4"))
                            fileoptionslabel.pack()
                            fileaction1.pack()
                            fileaction2.pack()
                            fileaction3.pack()
                            fileaction4.pack()
                            fileoptionswindow.mainloop()
                            if num == "1":
                                sp.run(["xdg-open", directory])
                                isafile = False
                            elif num == "2":
                                blank = moveitem(directory)
                                isafile = False
                            elif num == "3":
                                sure2 = 0
                                while sure2 != "y" and sure2 != "n":
                                    sure2window = tk.Tk()
                                    sure2window.title("File Searcher")
                                    sure2lable = tk.Label(sure2window, text="Are you sure you want to delete this file?")
                                    sure2y = tk.Button(sure2window, text="Yes", command=lambda: sure2assign("y"))
                                    sure2n = tk.Button(sure2window, text="No", command=lambda: sure2assign("n"))
                                    sure2lable.pack()
                                    sure2y.pack()
                                    sure2n.pack()
                                    sure2window.mainloop()
                                    if "RemoveLog" not in directory:
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
                                                    removelogwindow = tk.Tk()
                                                    removelogwindow.title("File Searcher")
                                                    removeloglabel = tk.Label(removelogwindow,
                                                                              text="There is no remove log, please create one")
                                                    removelogcreate = tk.Button(removelogwindow, text="Create",
                                                                                command=removelogwindow.destroy)
                                                    removeloglabel.pack()
                                                    removelogcreate.pack()
                                                    removelogwindow.mainloop()
                                                    moveitem("RemoveLog")
                                            sp.run(["rm", "-r", directory])
                                            isafile = False
                                            directory = "/home"
                                        elif sure == "n":
                                            isafile = False
                                        else:
                                            x = 1
                                    else:
                                        nodeletewindow = tk.Tk()
                                        nodeletewindow.title("File Searcher")
                                        nodeletelabel = tk.Label(nodeletewindow, text="Cannot delete file")
                                        nodeletecontinue = tk.Button(nodeletewindow, text="Continue",
                                                                     command=nodeletewindow.destroy)
                                        nodeletelabel.pack()
                                        nodeletecontinue.pack()
                                        nodeletewindow.mainloop()
                                        isafile = False
                            elif num == "4":
                                x = 1
                            else:
                                x = 1
                    elif enter == "y" and directory == __file__:
                        directory = "/home"
                        isafile = False
                    elif enter == "y" and "RemoveLog" in directory:
                        directory = "/home"
                        isafile = False
                    elif enter == "n":
                        x = 1
                        isafile = False
                    else:
                        x = 1