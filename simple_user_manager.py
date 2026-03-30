a = {}
customers = []
print("1-) Add customer \n",
      "2-) List customer\n"
      "3-) Update Customer (Phone / Email) \n"
      "4-) Delete Customer \n"
      "5-) Search by Name \n"
      "6-) Customer Count by City Report \n"
      "7-) Exit \n")
counter = 0
process = 0
while process != 7:
    process = int(input("Enter your choice: "))
    if process == 1:
        name = input("Enter Customer Name: ")
        phone = input("Enter Customer Phone Number (5xxxxxxxxx) :")
        if not len(phone) == 10 or not phone.isdigit():
            print("Please enter a valid phone number")
            continue

        if not phone.startswith("5"):
            print("Please enter a valid phone number")
            continue

        email = input("Enter Customer Email: ")
        if '@' not in email and '.' not in email:
            print("Please enter a valid email address")
            continue
        city = input("Enter Customer City: ")

        user = {
            "id": counter,
            "name": name,
            "phone": phone,
            "email": email,
            "city": city
        }

        counter += 1
        customers.append(user)

    elif process == 2:
        for users in customers:
            user_id = int(input("Enter Customer ID: "))
            if user_id > len(customers) - 1:
                print(f"User list has not this user_id : {user_id}")
                continue
            else:
                print(f"Customer ID found : {users}")


    elif process == 3:
        user_id = int(input("Enter Customer ID: "))
        if user_id > len(customers):
            print("Please enter a valid customer ID")
            continue

        for users in customers:
            if users["id"] == user_id:
                phone = input("Enter Customer Phone Number: ")
                if not len(phone) == 10:
                    print("Please enter a valid phone number")
                    continue
                if not phone.isdigit():
                    print("Please enter a valid phone number")
                    continue
                if not phone.startswith("5"):
                    print("Please enter a valid phone number")
                    continue
                email = input("Enter Customer Email: ")
                if '@' not in email and '.' not in email:
                    print("Please enter a valid email address")
                    continue
                users["phone"] = phone
                users["email"] = email

                print(f"Customer details updated successfully : {phone}, {email}")

    elif process == 4:
        user_id = int(input("Enter Customer ID: "))
        if user_id > len(customers) - 1:
            print("Customer information could not be found. Please try again.")
            continue
        else:
            customers.pop(user_id)
            print("Customer details delete successfully :")

    elif process == 5:
        name = input("Enter the name you wish to search for :")
        for users in customers:
            if name.lower() in users["name"].lower() or name in users["name"].lower():
                print(f"Customer name found : {users}")
            else:
                print(f"Customer name not found : {name}")

    elif process == 6:
        for users in customers:
            city = users["city"]
            a[city] = a.get(city, 0) + 1
        print(a)

    elif process == 7:
        print("The program has ended.")
        break
