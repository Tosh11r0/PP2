import os
path = input("Enter a path: ")

if not os.path.exists(path):
    print("No such path exists!")

else:
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    
    print("\nТолько директории:", directories)
    print("Только файлы:", files)
    print("Все файлы и директории:", all_items)




















