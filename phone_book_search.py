phone_book = {}
number = int(input("Kaç tane kullanıcı girmek istersiniz :"))

for i in range(number):
 key = str(input("İsim giriniz :"))
 value = int(input("Numara giriniz :"))
 phone_book[key] = value
print(phone_book)

istenen = str(input("Aradığınız ismi giriniz :"))

if istenen not in phone_book:
    print("Kayıt bulunamadı.")

elif istenen in phone_book:
    print(phone_book.get(istenen,value))

