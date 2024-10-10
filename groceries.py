def welcome():
    print("\t====== Hello =====")
    print('This is creating a list of groceries\n')
    print('for the week.  The project is a work in progress\n')
    print('and it will be finalized when it is completed.\n')
    print('\t==================')

#This will be the menu for what type of groceries people need 
def main(choice):
    print("What do you want to choose?")
    #list of choices 
    match choice:
        case 1:
               return "Groceries for week"
        case 2: 
              return "Writing someone else's groceries"
        case 3: 
               return "Template grocery for all cases"
        case _:
               return "Something is off.  Try again"



if __name__== "__main__":
    choice = type(int)
    welcome()
    main(choice)