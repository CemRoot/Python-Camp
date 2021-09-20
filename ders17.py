"""Hata Yönetimi - Try/Exception Yapısı"""


while True:

    try:
        sayi = int(input('Lütfen  1. sayı giriniz:'))
        sayi2 = int(input('Lütfen 2. sayı giriniz:'))
        # Hata yapmasından şüphe duyduğumuz bütün kodları try bloğunun içine
        # yazmamız gerekiyor aksi takdirde try içine değilde else durumuna
        # yazsaydık kodumuz çökecekti.
        print(sayi / sayi2)

# Eğer syntax hatası olursa çalışacak kod bloğu
    except ValueError:
        print('Lütfen sadece tam sayı değerleri giriniz!')

# Eğer Sıfır'a bölünme hatası alınırsa çalışacak kod bloğu.
    except ZeroDivisionError:
        print('Bir Sayı 0\'a bölünmez!')

# Eğer program except bölümlerine düşmezse else programı sürekli çalışacaktır.
    else:
        print('Doğru çalıştı!')
        break
    """print(sayi / sayi2)"""

print('Blok dışı')
