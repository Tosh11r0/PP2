import os

def lines(file_path):
    if not os.path.exists(file_path):
        print("No!")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)  
        return line_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


file_path = input("Enter the file path: ")

line_count = lines(file_path)

if line_count is not None:
    print(f"The file '{file_path}' has {line_count} lines.")
