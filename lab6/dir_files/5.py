import os

def user(file_path):
    data_list = []
    print("Enter: ")

    while True:
        item = input("> ")
        if item == "":
            break
        data_list.append(item)

    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(item + '\n')

        print(f"List has been written to '{file_path}' successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the file path to save the list: ")
user(file_path)
