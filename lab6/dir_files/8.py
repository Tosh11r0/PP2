
import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("Error")
        return

    try:
        os.remove(file_path)
        print("Successfull")
    except:
        print("error")

file_path = input("Enter: ")
delete_file(file_path)