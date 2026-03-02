vat_included = {}
menu = {
    "Hamburger": 180,
    "Pizza": 220,
    "Ayran": 30
}
print(menu)
for key, item in menu.items():
    kdv = ((item * 10) / 100) + item
    menu[key] = kdv

print(menu)