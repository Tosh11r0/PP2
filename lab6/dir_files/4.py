import os

def lines(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)  
        return line_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = input("Enter the file path: ")

line_count = lines(file_path)

