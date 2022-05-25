import boto3
import json

# Import functions from functions.py
from functions import createGroup, createUser, listUsers, disableUsers

def get_menu_choice():
    def print_menu():
        print(30 * "-", "MANAGER IAM AWS", 30 * "-")
        print("1. Create group ReadOnly and Admin ")
        print("2. Create User ")
        print("3. Disable User ")
        print("4. Report All Users ")        
        print("5. Exit ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:     
        print_menu()
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            createGroup()
            loop = True
        elif choice == '2':
            createUser()
            loop = True
        elif choice == '3':
            disableUsers()
            loop = True
        elif choice == '4':
            listUsers()
            loop = True
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


print(get_menu_choice())
