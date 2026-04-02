frequency = {}
new_dict = {}
answers = [
    "A"
    ,
    "B"
    ,
    "A"
    ,
    "C"
    ,
    "A"
    ,
    "C"
    ,
    "B"
    ,
    "C"
    ,
    "B"
    ,
    "A"
    ,
    "C"
    ,
    "B"
    ,
    "B"
    ,
    "C"
]
for answer in answers:

    total = len(answers)
    if answer not in frequency:
        frequency[answer] = 1

    elif answer in frequency:
        frequency[answer] += 1

for key, value in frequency.items():

    perc = int(100 * value / total)
    if key == "A":
        new_dict[key] = {"count" : value, "percentage" : perc}

    elif key == "B":
        new_dict[key] = {"count" : value, "percentage" : perc}

    elif key == "C":
        new_dict[key] = {"count" : value, "percentage" : perc}

print(new_dict)

