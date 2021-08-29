"""Bir sayının 7'ye bölünebilir olup olmadığını
   kontrol etmek için bir program yazın."""
Sayi = 8

if Sayi % 7 == 0:
    print("Sayı 7' e bölünebiliyor.")
else:
    print("Sayı 7'e tam bölünmüyor.")

"""Kullanıcıdan vize ve final notu isteyin. Girilen vize notunun %40’ı
ve girilen final notunun ise %60’ı alınarak yıl sonu not
ortalaması hesaplanacaktır. Bu not ortalaması eğer 85 ve üzeri ise AA,
75 ve 85 arasında ise BA, 70 ve 75 arasında ise BB, 65 ve 70 arasında ise CB,
60 ve 65 arasında ise CC, 55 ve 60 arasında ise DC, 50 ve 55 arasında ise DD
olarak hesaplanacaktır. Bu öğrencinin yıl sonu toplam notu 50’nin altında ise
FF ile dersten kalacaktır.Ayrıca öğrencinin final notu 50’nin altında ise
direkt FF ile kalacaktır.
"""

Vize = float(input("Vize Notunuzu Giriniz (%40):"))
Final = float(input("Final Notunuzu Giriniz (%60):"))
Not_ortalaması = float(Vize * 0.4) + (Final * 0.6)

if Final < 50:
    print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
    print("Finalden FF ile kaldınız.")
elif Final >= 50:
    if Not_ortalaması >= 85:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("AA notunu aldınız.")
    elif Not_ortalaması >= 75 and Not_ortalaması < 85:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("BA notunu aldınız.")

    elif Not_ortalaması >= 70 and Not_ortalaması < 75:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("BB notunu aldınız.")

    elif Not_ortalaması >= 65 and Not_ortalaması < 70:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("CB notunu aldınız.")

    elif Not_ortalaması >= 60 and Not_ortalaması < 65:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("CC notunu aldınız.")

    elif Not_ortalaması >= 55 and Not_ortalaması < 60:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("DC notunu aldınız.")

    elif Not_ortalaması >= 50 and Not_ortalaması < 55:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("DD notunu aldınız.")

    elif Not_ortalaması < 50:
        print("Yıl sonu ders ortalamanız:{0}".format(Not_ortalaması))
        print("FF notunu aldınız. Kaldınız!")
    else:
        print("Yanlış bir değer girdiniz")
else:
    print("Yanlış bir değer girdiniz.")

"""Kullanıcıdan iki tam sayı değeri alın ve
    aralarında büyük olanı ekrana yazdırın"""

sayi = float(input("Birinci Sayıyı Giriniz:"))
sayi2 = float(input("İkinci Sayıyı Giriniz:"))

if sayi > sayi2:
    print("1. sayi 2. sayindan büyüktür. Sayı {0}".format(sayi))
elif sayi < sayi2:
    print("2. sayi 1. sayindan büyüktür Sayı {0}".format(sayi2))

else:
    print("Sayılar Eşittir.")

"""3 Kişinin yaşlarını sırasıyla kullanıcıdan alın.
    Aralarından en büyük olanı ekrana yazdırın."""

kisi = int(input("1. kişinin yaşını giriniz:"))
kisi2 = int(input("2. kişinin yaşını giriniz:"))
kisi3 = int(input("3. kişinin yaşını giriniz:"))
enbuyuk = 0

if kisi > kisi2 and kisi > kisi3:
    enbuyuk = kisi
    print("1. kişinin yaşı daha büyüktür. Yaş:{0}".format(enbuyuk))
elif kisi2 > kisi and kisi2 > kisi3:
    enbuyuk = kisi2
    print("2. kişinin yaşı daha büyüktür. Yaş:{0}".format(enbuyuk))
elif kisi3 > kisi and kisi3 > kisi2:
    enbuyuk = kisi3
    print("3. kişinin yaşı daha büyüktür. Yaş:{0}".format(enbuyuk))
else:
    print("Yaşlar birbirine eşit")

"""Bir sayının son hanesinin 3'e bölünüp bölünemeyeceğini,
  kontrol etmek için bir program yazın. İpucu: Herhangi bir
  sayının son basamağını bulmak için sayı%10 yapabilirsiniz."""

num = int(input("bir sayı giriniz:"))
son_basamak = num % 10

if son_basamak % 3 == 0:
    print("Son basamak 3 sayısına tam bölünür")
else:
    print("Son basamak 3 sayısana tam bölünmez")

"""
Bir yılın artık yıl olup olmadığını kontrol etmek için bir program yazın.
Artık yıl kuralı:
a) Eğer yılın son iki basamağı (00) ile bitmiyorsa yalnızca 4'e tam bölünmesi
gerekir.
b) Eğer yılın son iki basamağı (00) ile bitiyorsa hem4'e hem de 400' e tam
bölünmesi gerekir.
Örneğin 1905 sayısının son iki basamağı 00 olmadığı için yalnızca 4 sayısına
tam bölünmesi kontrol edilmelidir.
Ancak 1900 sayısının son iki basamağı 00 ile bittiği için hem 4'e hem de 400'e
tam bölünmesi kontrol edilmelidir."""

yil = int(input("Lütfen bir yıl giriniz:"))

if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print("artık yıl")
        else:
            print("artık yıl değildir")
    else:
        print("Artık yıl")
else:
    print("artık yıl değildir")


"""Kullanıcıdan bir harf isteyin.
    Girilen bu harfin sesli harf olup olmadığını kontrol edin."""

harf = str(input("Bir harf giriniz:"))
sesli_harfler = ['a', 'A', 'E', 'e', 'I', 'ı', 'İ',
                 'i', 'O', 'o', 'Ö', 'ö', 'U', 'u', 'Ü', 'ü']
for sesli_harfler in harf:
    if sesli_harfler == harf:
        print("Girilen harf sesli harftir!")
    else:
        print("Girilen harf sessiz harftir!")

"""Kullanıcıdan bir üçgenin kenarları için 3 adet kenar uzunluğu isteyin.
Girilen kenar uzunluklarına göre bu üçgenin eşkenar, ikizkenar veya çeşitkenar
üçgen olma durumunu kontrol edin."""

uzunluk = int(input("1. kenar uzunluğunu giriniz:"))

uzunluk2 = int(input("2. kenar uzunluğunu giriniz:"))

uzunluk3 = int(input("3. kenar uzunluğunu giriniz:"))

if uzunluk == uzunluk2 == uzunluk3:
    print("Eş kenar Üçgen")
elif ((uzunluk == uzunluk2 and uzunluk2 != uzunluk3) or
      (uzunluk == uzunluk3 and uzunluk3 != uzunluk2) or
      (uzunluk2 == uzunluk3 and uzunluk2 != uzunluk)):
    print("İkizKenar Üçgen")
else:
    print("Çeşitkenar Üçgen")

""" Kullanıcıdan iki sayı ve temel matematiksel operatör isteyin.
Bunun sonucunda ilgili işlemi gerçekleştirin."""

# Toplama Fonksiyonu


def Topla(x, y):
    return x + y

# Çıkarma Fonksiyonu


def Cikar(x, y):
    return x - y

# Çarpma Fonksiyonu


def Carp(x, y):
    return x * y

# Bölme Fonksiyonu


def Bol(x, y):
    return x / y


print("Yapılacak İşlemi Seçin.")
print("=======================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

# Kullanıcıdan Seçim İsteme
secim = input("Seçiminiz (1/2/3/4):")

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

if secim == '1':
    print(sayi1, "+", sayi2, "=", Topla(sayi1, sayi2))

elif secim == '2':
    print(sayi1, "-", sayi2, "=", Cikar(sayi1, sayi2))

elif secim == '3':
    print(sayi1, "*", sayi2, "=", Carp(sayi1, sayi2))

elif secim == '4':
    print(sayi1, "/", sayi2, "=", Bol(sayi1, sayi2))
else:
    print("Geçersiz Giriş")
