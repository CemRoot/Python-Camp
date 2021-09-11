"""Fonksiyonlar - Varsayılan(Default) Parametreler."""
# Eğer p1 (veya p2 p3) değeri girilmezse varsayılan fonksiyondaki
# değer aktif olur ve 5 olarak tanımlanır.
# Bir parametreye değer atatığımızda sağındaki parametrede de
# değer olması gerekir aksi takdirde syntax hatası alınır.


def islem(p1, p2=4, p3='Python'):
    print(f'Çarpım sonucu: {p1 * p2}')
    print(f'Merhaba {p3}, Hoş Geldin!')


sayi1 = int(input('Lütfen "1. Sayıyı giriniz:'))
sayi2 = int(input('Lütfen 2. Sayıyı giriniz:'))
isim = input('Lütfen isminizi giriniz:')
islem(p1=sayi1, p2=sayi2, p3=isim)
