result_list=[]
max_price=3000
size=int(input("Kaç tane araç girmek istediğinizi giriniz :"))
for i in range(int(size)):
  cars = {"plate": input("Aracın plakasını giriniz :"),
          "brand": input("Aracın markasını giriniz :"),
          "model": input("Aracın modelini giriniz :"),
          "auto": input("aracın otomatik durumunu giriniz (True/False) :"),
          "daily": int(input("Aracın günlük fiyatını giriniz :"))}
  if cars["auto"]=="True" and cars["daily"]<= max_price:
    result_list.append(cars)
print(result_list)