cars = [
    {"plate": "34 ABC 01", "daily": 1200, "days": 3},
    {"plate": "35 SS 453", "daily": 1500, "days": 2},
    {"plate": "06 DF 234", "daily": 1100, "days": 5},
    {"plate": "16 GH 789", "daily": 1800, "days": 1},
    {"plate": "07 JK 456", "daily": 1400, "days": 4},
    {"plate": "01 LM 321", "daily": 1000, "days": 6},
    {"plate": "09 NO 852", "daily": 2000, "days": 2},
    {"plate": "20 PR 147", "daily": 1700, "days": 3},
    {"plate": "41 ST 963", "daily": 1300, "days": 7},
    {"plate": "45 UV 258", "daily": 1600, "days": 2},
    {"plate": "26 WX 369", "daily": 1900, "days": 4},
    {"plate": "10 YZ 741", "daily": 1250, "days": 3},
    {"plate": "54 AA 852", "daily": 2100, "days": 1},
    {"plate": "22 BB 963", "daily": 1750, "days": 5},
    {"plate": "48 CC 159", "daily": 1450, "days": 2},
    {"plate": "11 DD 357", "daily": 1550, "days": 6},
    {"plate": "38 EE 456", "daily": 1350, "days": 4},
    {"plate": "52 FF 654", "daily": 2200, "days": 3},
    {"plate": "60 GG 789", "daily": 1150, "days": 5},
    {"plate": "27 HH 951", "daily": 1650, "days": 2},
]
cars_fees_total = 0
for car in cars:
    print(car)
    print(car["plate"])
    plate = car["plate"]
    daily = car["daily"]
    days = car["days"]
    total = daily * days
    print("Total fee :", total)
    cars_fees_total += total
print("Cars fees total :", cars_fees_total)
