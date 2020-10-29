# This project represents a login / register system that uses
#   a .txt file to store the user information.
# Every user in "Users" class has a username, password, year and level
#   information. These Users are stored in a list named "user_list"
#   and this list is used to control login info. 
# New user can register with above informations and they would be
#   stored in the .txt file for later login.

# Users Class
class Users:
    def __init__(self, username, password, year, level):
        self.username   = username
        self.password   = password
        self.year       = year
        self.level      = level


# variable initialization
username = ""
password = ""
user_list = []
filepath = r"*filepath*\database.txt"

# read .txt for user info's
def read_database_file(filepath):
    try:
        database_file = open(filepath)
        for line in database_file:
            curr_line = line.split(',')
            user_list.append(Users(curr_line[0], curr_line[1], curr_line[2], curr_line[3]))
    except:
        print("file not found.")
    database_file.close()
    return

# enter new user information to the .txt file
def enter_database_file(filepath, username, password, year, level):
    database_file = open(filepath, "a")
    database_file.write("\n" + 
                        username + "," + 
                        password + "," +
                        year + "," +
                        level)
    
    print("\nnew user informations are registered.\n")
    database_file.close()
    return

# print options
def print_options():
    print("-" *50)
    print("For Login, enter: " + "\"L\"")
    print("For Register, enter: " + "\"R\"")
    return

# get user's choice from given options
def get_user_choice():
    return input("\nPlease enter your choice: ")

# login the system with given username and password
def login(username_, password_):

    # check if username and password matches
    for user in user_list:
        if (username_ == user.username and password_ == user.password):
            return print("-"*50 + "\n" + "welcome, " + user.username)

    return print("*** your entries does not match with database ***\n")


# main
if __name__ == "__main__":
    # read the .txt file and store informations
    # into the "user_list" that contains Users objects
    read_database_file(filepath)

    # print the options for user
    print_options()

    # get user's choice
    user_choice = get_user_choice()

    # 
    if user_choice.upper() == 'L':
        username = input("\tplease enter username: ")
        password = input("\tplease enter password: ")
        print("\n")

        login(username, password)
    
    elif user_choice.upper() == 'R':
        print("\n")
        username    = input("\tusername: ")
        year        = input("\tyear: ")
        level       = input("\tlevel: ")
        password    = input("\tpassword: ")
        con_pass    = input("\tconfirm given password: ")

        if password == con_pass:
            enter_database_file(filepath, username, password, year, level)

        else:
            print("given passwords doesn't match. please enter again.")
            pass
    else:
        print("unvalid choice.")
