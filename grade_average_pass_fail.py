grades =[]
grades_number=int(input("Lütfen kaç tane not girmek istediğiniz yazınız :"))
for i in range(grades_number+1):
    user_grades = int(input("Lütfen not giriniz :"))
    if user_grades == 0:
        print("Lütfen doğru not giriniz.")
        continue
    if user_grades > 100:
          print("Lütfen doğru not giriniz.")
          continue
    grades.append(user_grades)
toplam =int(sum(grades))
ortalama=toplam/len(grades)
print(int(ortalama))
if ortalama >= 50:
    print("Geçti")
else:
    print("Kaldı !")
