import json
def main():
    expenses = []
    try:
         with open("expenses.json","r") as file:
              expenses = json.load(file)
    except FileNotFoundError:
         expenses = []
    except json.JSONDecodeError:
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
         #option = int(input("Enter an option: "))
         input_not_valid = True
         while input_not_valid:
              try:
                   option = int(input("Enter an option: "))
                   input_not_valid = False
              except ValueError:
                   print("Enter a valid input as an option")
         if (option == 1):
              expense = {
                   "amount": 0,
                   "category": "",
                   "description": ""
              }
              amount_not_valid = True
              amount = 0
              while amount_not_valid:
                   try:
                        amount = int(input("Enter expense amount: "))
                        amount_not_valid = False
                   except ValueError:
                        print("Enter a valid amount")
              #amount = int(input("Enter the amount of the expense: "))
              expense["amount"] = amount
              category = input("What category is the expense: ")
              expense["category"] = category
              description = input("Write the description of the expense: ")
              expense["description"] = description                     
              #add an expense to a list
              expenses.append(expense)
              #add expenses to json
              with open("expenses.json","w") as file:
                   json.dump(expenses,file,indent=3)
             
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
                   #update json by writing current expense to file
                   with open("expenses.json","w") as file:
                        json.dump(expenses,file,indent=3)
              else:
                   print("Choose between the number of expenses")
         elif (option == 6):
              print("Session terminated")
              break
         else:
              print("Invalid input")

main()