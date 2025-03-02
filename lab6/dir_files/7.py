import os
import shutil

def copy(source, destination):
    if not os.path.exists(source):
        print("Error")
        return

    directory = os.path.dirname(destination)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        shutil.copyfile(source, destination)
        print("Successfull")
    except Exception as e:
        print("error")

source = input("Enter the source: ")
destination = input("Enter the destination: ")

copy(source, destination)