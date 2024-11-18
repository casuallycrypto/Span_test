from utils import read_text, read_file


if __name__ == "__main__":
    print("Welcome to ranking table") 
    inp = input("Upload via file or manuallyl?\n")
    if inp == "manual":
        text = read_text()
    elif inp == "file":
        print("enter the file name here: ")
        file_input = read_file()
    else:
        print("I didn't quite get that, please choose a valid choice")
