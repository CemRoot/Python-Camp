"""Hata Yönetimi - Raise Deyimi."""

# Python dili kırmızı yazılar ile kendine has hata mesajları yayınlamaktadır
# Bizde bir hata meydana geldiğinde bu şekilde mesajlar yayınlayabiliriz.
# Bunun için Raise deyimi kullanılır.

sayi = 5

try:
    if sayi == 5:
        raise Exception('Sayı 5\'e eşit olamaz!')
    else:
        print(sayi)
except Exception as e:
    print('ERROR! =>', e)
