"""
This file is adding all the 
files in one file to make it easier 
to pass it along to the main.py file.


"""


import meat as mp
import beverages as bx
import condiments as cx 
import produce as px 
import grains as gx 
import nuts_seeds as nx
import dairy as dx
def welcome():
    print("\t====== Hello =====")
    print('This is creating a list of groceries\n')
    print('for the week.  The project is a work in progress\n')
    print('and it will be finalized when it is completed.\n')
    print('\t==================')

#This will be the menu for what type of groceries people need 
def main(choice):
        welcome()
    #the variable choose is another way of saying yes or no
    #yes will be 1 and no will be 0
  

        choice = int(input('What do you want to choose?'))
        #list of choices 
        match choice:
            case 1:
                print("Groceries for week")
            case 2: 
                print("Writing someone else's groceries")
            case 3: 
                    print("Template grocery for all cases")
            case _:
                print("Incorrect input.  Try again")

