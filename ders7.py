"""Fonksiyonlar - İsimsiz Parametreler."""
# Bir fonksiyonda birden fazla parametre vermek mümkündür.
# Ancak önemli olan verilen bu parametrelerin sırasını doğru vermektir


def islem(p1, p2, p3):
    print(f'Çarpım sonucu: {p1 * p2}')
    print(f'Merhaba {p3}, Hoş Geldin!')


sayi1 = int(input('Lütfen "1. Sayıyı giriniz:'))
sayi2 = int(input('Lütfen 2. Sayıyı giriniz:'))
isim = input('Lütfen isminizi giriniz:')
islem(sayi1, sayi2, isim)
