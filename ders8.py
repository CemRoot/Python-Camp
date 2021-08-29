"""Fonksiyonlar - İsimli Parametreler."""


def islem(p1, p2, p3):
    print(f'Çarpım sonucu: {p1 * p2}')
    print(f'Merhaba {p3}, Hoş Geldin!')


sayi1 = int(input('Lütfen "1. Sayıyı giriniz:'))
sayi2 = int(input('Lütfen 2. Sayıyı giriniz:'))
isim = input('Lütfen isminizi giriniz:')
islem(p1=sayi1, p2=sayi2, p3=isim)
