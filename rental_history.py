rental_list = []
print("1-) Car rental\n"
      "2-) Exit")
exists = False
process = 0
while process != 2:

    process = int(input("Please select the action you wish to perform.\n"))
    if process == 1:
        customer_id = int(input("Please enter your customer ID number :"))

        date = input(
            "Please enter the date you would like to rent (Please enter the date in year-mount-day format.) :\n")

        plate = input("Please enter your plate number : ")
        rental = {
            "customer_id": customer_id,
            "date": date,
            "plate": plate,

        }
        # Eğer kullanıcı aynı veriyi eklemek isterse hata mesajı alacak ve veri eklenmeyecek exists true yapmamızın sebebi eğer false olurse ekliyor true için böyle bir durum yok
        for rentals in rental_list:
            if rentals["customer_id"] == customer_id and rentals["date"] == date and rentals["plate"] == plate:
                exists = True
                print("This data already exists and cannot be added.")
                break
            # Bu kısımda true olarak atanan veriyi tekrardan yeni veri girişi yapılma ihtimalilnden dolayı false olarak düzenliyoruz.
            else:
                exists = False
        # Eğer exists false ise veriyi ekliyor
        if exists == False:
            rental_list.append(rental)

    elif process == 2:
        print("The program has ended.")

print(rental_list)
