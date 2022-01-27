
"""3 ün ve 5 in katları."""
"""
toplam = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        toplam = toplam + i
    else:
        pass

print(toplam)
"""
########################################
"""Cümledeki kelime sayısı."""
"""
Cumle = str(input('Cümle giriniz:'))
sayac = 0
for i in Cumle:
    if i == ' ':
        sayac += 1

print('Cumlede sayısı:', sayac+1)
"""
######################################
"""Toplam Kare farkı ilk 100
    doğal sayının toplamlarının
    karesi ile karelerinin toplamı
    arasındaki farkı bulunuz.
"""


def kare_toplam(num):
    kare = 2
    toplam = 0
    for sayılar in range(1, num+1):
        toplam += sayılar ** kare
    return toplam


def toplamlarin_karesi(num):
    toplam = 0
    kare = 2
    for sayilar in range(1, num+1):
        toplam += sayilar

    return toplam ** kare


def fark_toplami(num):
    a = kare_toplam(num)
    b = toplamlarin_karesi(num)
    fark = b - a
    return fark


num = int(input('Bir sayı giriniz:'))
print('Fark toplamları:', fark_toplami(num))
