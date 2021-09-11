"""Fonksiynolar sonsuz (*arg, **kwargs) Parameterleri"""


def islem(**isimli):
    # sözlük yapısı oluşturmuş oluyor **
    return isimli


sonuc = islem(isim='Cem', soy_isim='koyluoglu', mesaj='Python')
print(sonuc)


def islem2(**isimli):
    for anahtar, deger in isimli.items():
        print(f'Anahtar-> {anahtar} \nDeger-> {deger}')
        print('-----------')


islem2(isim='Cem', soy_isim='koyluoglu', mesaj='Python')
