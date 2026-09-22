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
              #view all expenses
         elif (option == 2):
              for expense in expenses:
                   print(expense)
                   #calculate all spending
         elif (option == 3):
              amount = list(map(lambda expense:expense["amount"],expenses))
              total_expense = sum(amount)
              print(f"The total amount of the expense is {total_expense}")
         elif (option == 4):
              total_category = {}
              for expense in expenses:
                   category = expense["category"]
                   amount = expense["amount"]

                   if category in total_category:
                        total_category[category] += amount
                   else:
                        total_category[category] = amount
               #print total category and total amount of category
              for category, total in total_category.items():
                   print(f"Category:{category} Total:{total}")
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