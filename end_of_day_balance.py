transactions = [1000,
                -200,
                -150,
                500,
                -50,
                700,
                250,
                -300
                ]
biggest_expense = 0
expense_list = []
for transaction in transactions:
    if transaction < 0:
        expense_list.append(transaction)
print("Expense list :", expense_list)
total = float(sum(transactions))
print("Total :", total)
for expense in expense_list:
    if expense < biggest_expense:
        biggest_expense = expense
print("Big expense :", biggest_expense)
