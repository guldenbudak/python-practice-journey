harcama_0=[]
en_buyuk_sayi=0
toplam = 0
en_buyuk_gun = 0
gun = 1

for gun in range(1,8):
    gunluk_harcama = int(input("Harcamanızı giriniz :"))
    toplam += gunluk_harcama

    if gunluk_harcama == 0:
        harcama_0.append(gun)

    if gunluk_harcama > en_buyuk_sayi:
        en_buyuk_sayi = gunluk_harcama
        en_buyuk_gun =gun

print("Haftalık toplam harcama", toplam)
print("En yüksek harcama günü",en_buyuk_gun)
print("Harcama tutarı 0 olan gün",harcama_0)
