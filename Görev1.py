# 1)Python programlama dilindeki iki değişkenin değerinin takas özelliğini
# kullanmadan farklı yöntemlerle değiştirin. Bu programın kaynak kodunu yazın.

Num1 = 100
Num2 = 200
Num3 = Num1, Num2 = Num2, Num1
print(Num3)

# 2) Python programlama dilindeki iki değişkenin değerinin takas özelliğini
# kullanmadan ve 3.değişken kullanmadan farklı yöntemlerle değişkenlerin
# değerini takas yapın. Bu programın kaynak kodunu yazın.

Nm1 = 100
Nm2 = 200
Nm2 = 100
Nm1 = 200

print(Nm1, Nm2)

""" Python ~ Uygulamalar
    Kullanıcıdan isim, soyisim ve şehir bilgisini alıp
    tek bir print() içerisinde alt alta yazdırın.
    Programın kaynak kodunu yazın.
"""
Name = str(input('Pls Enter your name:'))
Surname = str(input('Pls Enter your surname:'))
City = str(input('Pls Enter your city:'))
print(f'Name: {Name}\nSurname: {Surname}\nCity: {City}')

""" Python ~ Uygulamalar
    Kullanıcıdan bir sayı isteyin. Bu sayıya “n” diyelim.
    Girilen bu sayı için “n + nn + nnn + nnnn” işlemini gerçekleştirin.
    Programın kaynak kodunu yazın.
"""
n = input('Lütfen bir sayı girin: ')
b2 = n + n  # 88
b3 = n + n + n  # 888
b4 = n + n + n + n  # 8888

sonuc = int(n) + int(b2) + int(b3) + int(b4)
sonuc2 = n + b2 + b3 + b4

print(f'Sonuc: {n} + {b2} + {b3} + {b4} = {sonuc} ')

""" Python ~ Uygulamalar
    Kullanıcıdan 2 tam sayı isteyin. Girilen bu sayılar için 4 temel işlemi
    (toplama, çıkarma, çarpma, bölme) gerçekleştirin.
    Ayrıca bu sayıların ortalamasını da yazdırın.
    Aşağıdaki ekran çıktısını veren programın kaynak kodunu yazın.
    (Not: Formatlama yönteminde format() biçimlendirme yöntemini kullanın.
    Bölme işleminde 2 basamak hassasiyet olması gerekmektedir.)
"""

sayi1 = int(input('Lütfen 1.sayıyı girin: '))
sayi2 = int(input('Lütfen 2.sayıyı girin: '))

# Toplama İşlemi
print('{0} + {1} = {2}'.format(sayi1, sayi2, sayi1 + sayi2))

# Çıkarma İşlemi
print('{0} - {1} = {2}'.format(sayi1, sayi2, sayi1 - sayi2))

# Çarpma İşlemi
print('{0} x {1} = {2}'.format(sayi1, sayi2, sayi1 * sayi2))

# Bölme İşlemi
print('{0} / {1} = {2:.2f}'.format(sayi1, sayi2, sayi1 / sayi2))

# Ortalama
print('Ortalama: ({0} + {1}) / 2 = {2:.2f}'.format(sayi1,
      sayi2, (sayi1 + sayi2)/2))

""" Python ~ Uygulamalar
    Kullanıcıdan 1 vize ve 1 final notu isteyin.
    Vize notunun %40’ı ile Final notunun %60 değerini alıp
    genel not ortalamasını elde edin.
    Bu ortalama 50 ve üzeri ise ekranda “True” sonucu ve
    ortalama notunu gösterin. Eğer ortalama 50’den küçükse
    ekranda “False” sonucu ve ortalama notunu gösterin.
"""

vize_notu = input('Lütfen vize notu girin: ')
final_notu = input('Lütfen final notu girin: ')
VIZE_KATSAYI = 0.40
FINAL_KATSAYI = 0.60

ortalama = (float(vize_notu) * VIZE_KATSAYI) + \
    (float(final_notu) * FINAL_KATSAYI)

print('Ortalama: {0}, Sonuç: {1}'.format(ortalama, ortalama >= 50))

""" Python ~ Uygulamalar
    Kullanıcıdan 1 kısa kenar ve 1 uzun kenar değeri isteyin.
    Girilen bu değerlerden bir dikdörtgenin alanı ve çevresini hesaplayın.
    Ayrıca Dikdörtgen şeklini sadece 1 print() fonksiyonu kullanarak ekranda çizdirin.
"""
uzun_kenar = int(input('Lütfen uzun kenar girin: '))
kisa_kenar = int(input('Lütfen kısa kenar girin: '))

uzun_bosluk = uzun_kenar - 2
kisa_bosluk = kisa_kenar - 2

alan = kisa_kenar * uzun_kenar
cevre = (kisa_kenar + uzun_kenar) * 2
print(f'Alan: {alan}')
print(f'Çevre: {cevre}')

print('Dikdörtgen Çizimi:\n')
print(('#'*uzun_kenar) + (('\n#' + ' ' * uzun_bosluk + '#')
      * kisa_bosluk) + '\n' + ('#' * uzun_kenar))
