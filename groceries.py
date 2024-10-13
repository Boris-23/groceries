def welcome():
    print("\t====== Hello =====")
    print('This is creating a list of groceries\n')
    print('for the week.  The project is a work in progress\n')
    print('and it will be finalized when it is completed.\n')
    print('\t==================')

#This will be the menu for what type of groceries people need 
def main(choice, choose):

    #the variable choose is another way of saying yes or no
    #yes will be 1 and no will be 0
    choose = int(input('Want to continue? 0 for no and 1 for yes'))

    while choose > 0:

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



if __name__== "__main__":
    choice = type(int)
    choose = type(int)
    welcome()
    main(choice, choose)