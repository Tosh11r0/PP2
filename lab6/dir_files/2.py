import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("OK")

    #check readability
    if os.access(path, os.R_OK):
        print("OK")
    else:
        print("Not readeable")

    # Check writability
    if os.access(path, os.W_OK):
        print("OK")
    else:
        print("NOT writable")

    # Check executability
    if os.access(path, os.X_OK):
        print("OK")
    else:
        print("NOT executable")

else:
    print("No such path")
