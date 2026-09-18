def main():
    expenses = []
    #print welcome and options menu
    while True:
         print("You are welcome to expense tracker")
         print("Perform an operation by choosing from the options below")
         print("1. Add an expense")
         print("2. View all expenses")
         print("3. Calculate total spending")
         print("4. Calculate spending by category")
         print("5. Delete an expense")
         print("6. Save expenses to a file")
         print("7. Exit")
         #options selection and action
         option = int(input("Enter an option: "))
         if (option == 1):
              expense = {
                   "amount": 0,
                   "category": "",
                   "description": ""
              }
              amount = int(input("Enter the amount of the expense: "))
              expense["amount"] = amount
              category = input("What category is the expense: ")
              expense["category"] = category
              description = input("Write the description of the expense: ")
              expense["description"] = description

              #add to the expenses
              expenses.append(expense)
         elif (option == 2):
              print("View all expenses")
         elif (option == 3):
              print("Calculate total expenses")
         elif (option == 4):
              print("Calculate by category")
         elif (option == 5):
              print("Delete an expense")
         elif (option == 6):
              print("Saved to file")
         elif (option == 7):
              print("Session terminated")
              break
         else:
              print("Invalid input")
              
    print(expenses)

main()