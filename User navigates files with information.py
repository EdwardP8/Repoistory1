import subprocess as sp
import os
import time as t


isafile = False
print("Welcome, here you can choose files and get information about them! Make sure you use the correct capitalisation. press enter to begin")
input()

directory = "/home/edward-penny"
#begins the user at home
while not isafile:
    print("here are the files and folders:")
    sp.run(["ls", directory])
    #shows all the files in the folder
    temp = directory

    directory = f"{directory}/{input("Where would you like to go?\n")}"
    #sets the directory to what the user chooses
    pathexists = os.path.exists(directory)
    if not pathexists:
        print("Path does not exist, try again")
        directory = temp
    isafile = os.path.isfile(directory)
    #checks if the path is a file

    if isafile:
        size = os.path.getsize(directory)
        date = t.ctime(os.path.getmtime(directory))
        print(f"The file's size is {size} bytes, the location is {directory}, and it was last modified on {date}")
