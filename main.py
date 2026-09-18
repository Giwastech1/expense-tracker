def main():
    #print welcome and options menu
    print("You are welcome to expense tracker")
    print("Perform an operation by choosing from the options below")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total spending")
    print("4. Calculate spending by category")
    print("5. Delete an expence")
    print("6. Save expenses to a file")
    print("7. Exit")

main()

#option selection and action
option = int(input("Enter an option: "))

if (option == 1):
    print("Add an expense")

elif (option == 2):
    print("View all expenses")
elif (option == 3):
    print("Calculate total spending")
elif(option ==4 ):
    print("Calculate spending by category")
elif(option == 5):
    print("Delete an expense")
elif(option == 6):
    print("Saved to a file")
elif(option == 7):
    print("Session terminated")
    exit()
else:
    print("Invalid input")