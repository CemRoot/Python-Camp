"""Üst sınırı kullanıcı tarafından belirlenen aralıktaki tüm asal sayıları
yazdırın. Asal sayılar, sadece kendisine ve 1'e bölünebilen 1'den büyük
doğal sayılardır."""

sayı = int(input('Üst Sınır giriniz:'))

for i in range(2, sayı+1):
    bolen = 0
    for j in range(2, i):
        if i % j == 0:
            bolen = bolen + 1
    if bolen <= 0:
        print(i, end=' ')
