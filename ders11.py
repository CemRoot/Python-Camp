"""Fonksiyonlar - Sonsuz (*args, **Kwargs) Parametreleri."""


def islem(*isimsiz):
    # fonksiyonlu sum() kullandığımızda
    return sum(isimsiz)


sonuc = islem(10, 20, 30, 40)
print(sonuc)


def islem(*isimsiz):
    # sum kullanmadan yapmaya çalıştığımızda
    toplam = 0.0
    for i in isimsiz:
        toplam = toplam + i

    return toplam


sonuc = islem(10, 20, 30, 40)
print(sonuc)
