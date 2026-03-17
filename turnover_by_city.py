city_totals = {}
highest_turnover = 0
highest_city =[]
orders = [
    {"city": "İstanbul", "total": 1200},
    {"city": "Ankara", "total": 800},
    {"city": "İzmir", "total": 950},
    {"city": "Bursa", "total": 700},
    {"city": "İstanbul", "total": 1350},
    {"city": "Ankara", "total": 920},
    {"city": "İzmir", "total": 880},
    {"city": "Bursa", "total": 760},
    {"city": "İstanbul", "total": 1420},
    {"city": "Ankara", "total": 830},
    {"city": "İzmir", "total": 990},
    {"city": "Bursa", "total": 810},
    {"city": "İstanbul", "total": 1250},
    {"city": "Ankara", "total": 870},
    {"city": "İzmir", "total": 910}
]
for order in orders:

    total = order["total"]
    city = order["city"]
    city_totals[city] = city_totals.get(city, 0) + total
for key, value in city_totals.items():

    if value > highest_turnover:
        highest_turnover = value
        highest_city.append({key: highest_turnover})

print(highest_city)
print(city_totals)