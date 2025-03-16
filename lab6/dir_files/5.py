import os

list = ["P.Diddy ","is ","pdf ","file"]
with open("writable_file.txt","w") as w:
    w.writelines(list)