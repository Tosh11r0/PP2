import os

path = input("Enter a path:")

if os.path.exists(path):
      directory, filename = os.path.split(path)
      print (directory,filename)
else:
    print ("No such path")