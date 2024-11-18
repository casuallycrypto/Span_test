from utils import read_text, read_file


if __name__ == "__main__":
    print("Welcome to ranking table\nType 'm' to begin using text, type 'f' to begin using a file.") 
    choice = input("Upload via file or manuallyl?\n")
    if choice == "m":
        print("enter the results here(Press Enter once you're done): \n")
        text = read_text()
    elif choice == "f":
        print("enter the file name here: \n")
        file_input = read_file()
    else:
        print("I didn't quite get that, please choose a valid choice")
