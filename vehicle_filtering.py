rental_cars = []
cars_in_maintenance = []
current_vehicle = []
number_of_vehicles = {}
cars = [
    {"plate": "34 ABC 101", "status": "available"},
    {"plate": "06 DEF 202", "status": "rented"},
    {"plate": "35 GHI 303", "status": "maintenance"},
    {"plate": "16 JKL 404", "status": "available"},
    {"plate": "07 MNO 505", "status": "rented"},
    {"plate": "01 PQR 606", "status": "available"},
    {"plate": "55 STU 707", "status": "maintenance"},
    {"plate": "41 VWX 808", "status": "available"},
    {"plate": "52 YZA 909", "status": "rented"},
    {"plate": "33 BCD 111", "status": "available"},
    {"plate": "26 EFG 222", "status": "maintenance"},
    {"plate": "48 HIJ 333", "status": "available"},
    {"plate": "38 KLM 444", "status": "rented"},
    {"plate": "44 NOP 555", "status": "available"},
    {"plate": "61 QRS 666", "status": "maintenance"},
    {"plate": "20 TUV 777", "status": "available"},
    {"plate": "54 WXY 888", "status": "rented"},
    {"plate": "10 ZAB 999", "status": "available"},
    {"plate": "46 CDE 123", "status": "maintenance"},
    {"plate": "58 FGH 234", "status": "available"}
]

for car in cars:
    plate = car["plate"]
    status = car["status"]
    if status == "rented":
        rental_cars.append(car)
    elif status == "maintenance":
        cars_in_maintenance.append(car)
    elif status == "available":
        current_vehicle.append(car)
print("1) Vehicles that are rented \n"
      "2) Current number of vehicles \n"
      "3) License plates of vehicles undergoing maintenance\n"
      "4) Exit\n"
      )
process = 0
while process != 4:
    process = int(input("Select the action you wish to perform :\n"))
    if process == 1:
        print(rental_cars)

    elif process == 2:

        for a in current_vehicle:
            status = a["status"]
            if status not in number_of_vehicles:
                number_of_vehicles[status] = 1
            elif status in number_of_vehicles:
                number_of_vehicles[status] += 1
        print(number_of_vehicles)

    elif process == 3:

        for i in cars_in_maintenance:
            plate = i["plate"]
            cars_in_maintenance = [plate]
            print(plate)

    elif process == 4:
        print("The program has ended.")
