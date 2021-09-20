"""Hata Yönetimi -Giriş"""

"""
Hata Türleri
    Syntax (sözdizimi) Hatası -> Geliştirici Hataları
    Mantık Hataları
    İstisnalar (Exception)
"""
# Örnek vermek gerekirse bu şekilde yazım Syntax yani söz dizimi hatasıdır.
''' print 'Merhabalar'


def islem()
    print('Selam')
 '''
# Mantıksal Hatalar en zorudur program çalışır fakat
# mantık hatası yapar örnek olarak;

''' Sayi = int(input("Lütfen bir sayı giriniz:"))
print('Sayının karesi:', Sayi**3) '''
# Biz karesini almak istedik fakat küpünü aldık.
# Uzun yazılmış kodlarda bu gibi hataları görmek bazen zordur.

# Exception hatalar programın çökmesine yol açan ve oldukça büyük bir hatadır
# python, dilinde bu hataların yönetimi vardır.
# Python'da bu gibi buglarda bu gibi hatalarda neler yapacağımızı görelim.
# Bu istisnaların yönetimini yapamazsak programımız çökecektir.

sayi = int(input('Lütfen bir sayı giriniz:'))
print(sayi)
# Yukarıda kullancıdan bir sayı istediğimiz zaman 10 değerinden farklı bir
# değer girebilir. Mesela 14 yazmaya çalışırken 14i yazarak enter'a bastı ve
# programımız çöktü.
