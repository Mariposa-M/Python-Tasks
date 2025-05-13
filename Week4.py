# File Read & Write Challenge 🖋️: 
# Create a program that reads a file and writes a modified version to a new file.
with open("bike_sales.txt", "r") as file:
    # Note: read >> saves string not list like readlines
    data = file.read()
    data += "\nnew line"
    with open("new.txt", "w") as new_file:
        new_file.write(data)

# Error Handling Lab 🧪: 
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
ask_user = input("Which file do you want to open?: ")
file_name = ask_user + ".txt"
try:
    file = open(file_name, "r")
    print(file.read())
    
except FileNotFoundError:
    print("Double check the name again please")
    
# Added Permission Error exception & Decoding ones 
except PermissionError:
    print("Seems you don't have permission to access that file")
    
except UnicodeDecodeError:
    print("The file exists but for some reason the file is unreadable")

finally:
    file.close()
    