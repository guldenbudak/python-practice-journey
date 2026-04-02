result = {}
cart = [
    "SKU1"
    ,
    "SKU2"
    ,
    "SKU1"
    ,
    "SKU3"
    ,
    "SKU2"
    ,
    "SKU1"
    ,
    "SKU3"
    ,
    "SKU1"
    ,
    "SKU3"
    ,
    "SKU2"
    ,
    "SKU1"
    ,
    "SKU3"
]

for carts in cart:

    if carts in result:
        result[carts] += 1

    if carts not in result:
        result[carts] = 1

print(result)
