expenses = {}
category_total = {}
total = 0
total_balance = []
bank = [
    {"category": "Maaş", "amount": 30000},
    {"category": "Market", "amount": -850},
    {"category": "Ulaşım", "amount": -120},
    {"category": "Market", "amount": -230},
    {"category": "Fatura", "amount": -600},
    {"category": "Kira", "amount": -12000},
    {"category": "Eğlence", "amount": -450},
    {"category": "Restoran", "amount": -700},
    {"category": "Sağlık", "amount": -300},
    {"category": "Alışveriş", "amount": -950},
    {"category": "Maaş", "amount": 32000},
    {"category": "Ulaşım", "amount": -150},
    {"category": "Market", "amount": -400},
    {"category": "Fatura", "amount": -750},
    {"category": "Eğlence", "amount": -500}
]
for item in bank:

    category = item["category"]
    amount = item["amount"]

    expenses[category] = expenses.get(category, 0) + amount

    if amount < 0:
        category_total[category] = category_total.get(category, 0) + amount

for key, value in expenses.items():

    total = total + value
total_balance.append(total)

print("Total categories expenses",category_total)
print("Total categories",expenses)
print("Total net balance",total_balance)