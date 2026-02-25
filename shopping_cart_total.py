price =[12.5, 45.0, 9.99, 3.75]
toplam = float(sum(price))
print("The total price is ", toplam)

price =[12.5, 45.0, 9.99, 3.75]
toplam = 0
for sayi in price:
    toplam += sayi
print(f"The total price is {toplam:,}")