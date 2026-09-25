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
         print("6. Exit")
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
              for index_num,expense in enumerate(expenses,start=1):
                   print(index_num,expense)
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
                   print(f"{category}: {total}")
         elif (option == 5):
              option_to_delete = int(input("Enter a number to delete: "))
              if option_to_delete >=1 and option_to_delete <= len(expenses):
                   expenses.pop(option_to_delete-1)
              else:
                   print("Choose between the number of expenses")
         elif (option == 6):
              print("Saved to file")
         elif (option == 7):
              print("Session terminated")
              break
         else:
              print("Invalid input")

main()