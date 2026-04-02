goals = {
    "Ahmet": [1, 0, 2, 1],
    "Burak": [0, 0],
    "Can": [2, 2, 0, 1, 0],
    "Deniz": [0, 1, 0, 2],
    "Eren": [1, 1, 1],
    "Furkan": [0, 2, 0, 0],
    "Gökhan": [3, 1, 0],
    "Hakan": [0, 0, 0, 1],
    "İsmail": [2, 1, 2],
    "Kerem": [1, 0, 1, 0],
    "Levent": [0, 3, 1],
    "Mert": [1, 1, 0],
    "Necati": [2, 0, 0, 1],
    "Okan": [0, 0, 0],
    "Polat": [3, 0, 2],
    "Rıza": [0, 0, 1, 1],
    "Serkan": [2, 2, 1],
    "Tolga": [1, 0, 0, 0],
    "Uğur": [0, 2, 2],
    "Volkan": [1, 1, 1, 1],
    "Yasin": [0, 3, 0],
    "Zafer": [2, 0, 1],
    "Emre": [1, 2, 0],
    "Kaan": [0, 0, 1],
    "Baran": [1, 1, 0, 2]
}
total_goals = {}
highest_score = 0
lowest_score = 10000000000
highest = []
lowest = []
# en büyük ve en küçük gol sayılarını bulduk
for key, item in goals.items():

    sum_goal = sum(item)
    name = key
    total_goals[name] = sum_goal
    if sum_goal > highest_score:
        highest_score = sum_goal

    if sum_goal < lowest_score:
        lowest_score = sum_goal

# en büyük değerleri dict şeklinde listeye ekledik
for key, item in goals.items():

    sum_goal = sum(item)
    name = key
    if sum_goal == highest_score:
        highest.append({name: sum_goal})

# en küçük değerleri dict şeklinde listeye ekledik
for key, item in goals.items():

    sum_goal = sum(item)
    name = key
    if sum_goal == lowest_score:
        lowest.append({name: sum_goal})

print(highest)
print(lowest)
print(total_goals)
