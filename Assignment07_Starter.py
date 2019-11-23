# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Nahien Chowdhury, November 15, 2019, Modified Lab Script for HW 7
# ------------------------------------------------- #
import pickle  # This imports code from another code file!
import shelve  # This allows you to store and randomly access multiple pickled objects in a file

# Menus and Exit functions -------------------------------------------- #
strFileName = 'AppData.dat' # File name of the binary file for pickling

def welcome():
    print("Welcome, Please enter an ID and name.")
    while True:
        global lstCustomer #declaring variable for the list destined for names and IDs
        id = input(str("Enter an ID: "))
        name = input(str("Enter the Name: "))
        lstCustomer = [(id, name)] #compiling the id and names intro a list
        return lstCustomer #returning the list

def exit(): #exit fuction
    global quit #declaring boolean variable for quitting
    global quit_choice #declaring variable for quitting input choice
    quit = input(str("Do you wish to exit? (Yes / No): "))
    quit = quit.lower() #converting inputs into lower
    if "yes" in quit:  #loop to alter quitting boolean
        quit_choice = True
    if "no" in quit:
        quit_choice = False
    return quit_choice


def menu(): #menu function
    global choice #declaring variable for menu choice
    choice = input(str("Save Data or Read from a file? (S/R)"))
    choice = choice.lower() #Converting input to lower
    return choice #returning menu choice

# Pickling -------------------------------------------- #

def stu_pickles(lstCustomer): #pickling function passing names and IDs
    print("Pickling lists.")
    try:
        f = open(strFileName, "wb") #Writes binary files
        pickle.dump(lstCustomer, f) #dumps the list
        f.close() #closing
    except:
        print("Pickling was unsuccessful </3")
    return lstCustomer

def tommy_pickles(): #unpickling function with no passing variables
    print("\nUnpickling lists.")
    try:
        f = open(strFileName, "rb")  #Reading the binary file
        global list_of_data #delaring global variable for new list
        list_of_data = [pickle.load(f)] #writing new list
        f.close() # closing
    except:
        print("Unpickling was unsuccessful :-(")
    return list_of_data

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data): #passing file name and unpickled data
   try:
        text_file = open(file_name, "w+") #writing to file
        text_file.writelines(str(list_of_data)) #wriningLines
        text_file.close()
   except:
       print("Error - Data was not saved")

def read_data_from_file(file_name):
    try:
        print("\nReading the entire file into a list.")
        text_file = open(file_name, "r")
        lines = text_file.readlines()
        print("length of line is: ", len(lines))
        for line in lines:
            print(line)
        text_file.close()
    except:
        print("Error - Data could not be read.")

def wrong_entry():
    print("Please Enter a correct entry")
    return

# Body ------------------------------------ #
while True:
    welcome()
    menu()
    stu_pickles(lstCustomer)
    tommy_pickles()
    if "s" in choice:
        file_name = input(str("Enter the name of the file you wish to SAVE: "))
        save_data_to_file(file_name, list_of_data)
    elif "r" in choice:
        file_name = input(str("Enter the name of the file you wish to READ: "))
        read_data_from_file(file_name)
    else:
        wrong_entry()
    exit()
    if quit_choice:
        break