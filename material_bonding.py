mix_list = []
home = [
    "flour",
    "sugar",
    "egg",
    "milk",
    "butter",
    "cheese",
    "bread",
    "apple"
]
guest = [
    "sugar",
    "milk",
    "chocolate",
    "bread",
    "banana",
    "cheese",
    "coffee",
    "tea"
]
for item in home:

    if item not in mix_list:
        mix_list.append(item)

for item in guest:

    if item not in mix_list:
        mix_list.append(item)

print(mix_list)
