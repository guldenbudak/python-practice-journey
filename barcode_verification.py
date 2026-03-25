warehouse = [
    {"barcode": "1X1X1X1"},
    {"barcode": "1X2X3X4"},
    {"barcode": "2X1X2X3"},
    {"barcode": "2X3X1X5"},
    {"barcode": "3X2X4X1"},
    {"barcode": "3X4X2X6"},
    {"barcode": "4X1X3X2"},
    {"barcode": "4X3X5X4"},
    {"barcode": "5X2X1X3"},
    {"barcode": "5X4X3X5"},
    {"barcode": "6X1X2X4"},
    {"barcode": "6X3X4X2"},
    {"barcode": "7X2X5X1"},
    {"barcode": "7X4X1X6"},
    {"barcode": "8X1X3X3"},
    {"barcode": "8X3X2X5"},
    {"barcode": "9X2X4X4"},
    {"barcode": "9X4X5X2"},
    {"barcode": "10X1X1X6"},
    {"barcode": "10X3X3X1"}
]
while True:
    control_barcode = input("Please enter the barcode value you are looking for :")
    split_control_barcode = control_barcode.split("X")[0]

    if not split_control_barcode.isdigit():
        print("Please enter a numerical value.")
        continue

    else:
        break

for barcode in warehouse:
    if split_control_barcode == barcode["barcode"].split("X")[0]:
        print("Warehouse found !")
        break
else:
    print("Warehouse not found !")
