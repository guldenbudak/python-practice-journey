new_items =[]
items = \
["süt"
,
"ekmek"
,
"süt"
,
"peynir"
,
"ekmek"
,
"yoğurt"]
for item in items:
    if item not in new_items:
     new_items.append(item)
print("Tekrarsız veriler kaldırılmıştır.",new_items)
print("Tekrarsız veriler kaldırılmamıştır.",items)