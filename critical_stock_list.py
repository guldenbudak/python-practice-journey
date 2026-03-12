limited_stock = {}
stock = {
    "SKU1": 10,
    "SKU2": 8,
    "SKU3": 1,
    "SKU4": 6,
    "SKU5": 12,
    "SKU6": 3,
    "SKU7": 14,
    "SKU8": 7,
    "SKU9": 4,
    "SKU10": 5,
    "SKU11": 13,
    "SKU12": 16,
    "SKU13": 2,
    "SKU14": 3,
    "SKU15": 17,
    "SKU16": 22,
    "SKU17": 0
}
for item in stock.items():
    key = item[0]
    value = item[1]
    if value < 5 :
        limited_stock[key] = value
print(limited_stock)
