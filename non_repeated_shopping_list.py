new_items =[]
items = \
["milk"
,
"bread"
,
"milk"
,
"cheese"
,
"bread"
,
"yogurt"]
for item in items:
    if item not in new_items:
     new_items.append(item)
print("Duplicate data has been removed..",new_items)
print("Duplicate data was not deleted..",items)