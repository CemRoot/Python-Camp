"""Kullanıcıdan bir sayı isteyin ve bu sayının kaç basamaklı olduğunu bulun.
Bu işlemi döngüler kullanarak yapın.
"""
""""
Sayi = int(input("Bir sayı giriniz:"))
basamak_sayisi = 0

while(Sayi > 0):
    Sayi = Sayi // 10
    basamak_sayisi = basamak_sayisi + 1

print("Girilen sayının basamak sayısı:", basamak_sayisi)"""

"""Kullanıcıdan bir sayı isteyin ve bu sayıyı
    ters çevirerek yeniden yazdırın."""
"""
sayi = int(input('Bir sayı giriniz:'))
basamak_ekleme = 0
while sayi > 0:
    son_basamak = sayi % 10
    basamak_ekleme = basamak_ekleme * 10 + son_basamak
    sayi = sayi // 10
print('Ters Cevirilmiş sayı:', basamak_ekleme)
"""
"""Kullanıcıdan bir sayı isteyin. Bu sayının basamaklarının toplamını bulun."""

"""sayi = int(input('Bir Sayı giriniz:'))
basamak_toplamı = 0
while sayi > 0:
    toplamı = sayi % 10
    basamak_toplamı += toplamı
    sayi = sayi // 10
print('Basamak Toplamları:', basamak_toplamı)
"""
"""Kullanıcıdan bir sayı isteyin. Bu sayının palindrom olup olmadığını
yazdırın. Palindrom sayı, iki taraftan okunduğu zaman okunuş yönüyle
aynı olan sayılardır.Tüm rakamlar palindrom sayıdır.
Örneğin: 11, 121, 454, 8558 vb."""

"""sayi = int(input('Bir Sayı giriniz:'))
son_sayı = sayi
basamak_ekleme = 0
while sayi > 0:
    son_basamak = sayi % 10
    basamak_ekleme = basamak_ekleme * 10 + son_basamak
    sayi = sayi // 10
if son_sayı == basamak_ekleme:
    print('Sayi Palindrom')
else:
    print('Sayı Palindrom değil')
"""
"""Kullanıcıdan bir sayı isteyin. Bu sayının güçlü(strong) sayı olup
olmadığını yazdırın. Güçlü sayı, basamaklarının faktöriyel değerlerinin
toplamının kendisine eşit olan sayılara denir.
Örneğin: 145 -> 1! + 4! + 5! = 145 olduğu için 145 güçlü sayıdır."""

"""sayi = int(input('Bir sayı giriniz:'))
gecici = sayi
toplam = 0
while sayi > 0:
    # Her yenilendiğinde tekrardan i ve faktoriyel değerler resetleniyor.
    i = 1
    fakt = 1
# Son basamağı bulabilmek için (bölümden kalan MOD)
    son_basamak = sayi % 10
# Son basamağı çıkarmak taban bölme (int)
    sayi = sayi // 10
    while i <= son_basamak:
        fakt = fakt * i
        i += 1
    toplam += fakt
if toplam == gecici:
    print('Güçlü sayı')
else:
    print('Güçsüz sayı')"""

"""10 elemanlı ve sadece tam sayılardan oluşan bir liste oluşturun.
Aşağıdaki işlemleri gerçekleştirin. Hazır fonksiyon (sum, sorted, max, min vb.)
kullanmayın.

a) Sayıların toplamını bulun.

b) Elemanların ortalamasını bulun.

c) Listenin en büyük elemanını bulun.

d) Listenin en küçük elemanını bulun."""

"""
Sayilar = [56, 23, 8, 1, 98, 64, 22, 0, 71, 35]
liste = Sayilar
toplam = 0
en_buyuk = liste[0]
en_kucuk = liste[0]
i = 0

while i < len(liste):
    if liste[i] > en_buyuk:
        en_buyuk = liste[i]
    if liste[i] < en_kucuk:
        en_kucuk = liste[i]

    toplam = toplam + liste[i]
    i += 1
ortalama = toplam / len(liste)

print('Toplam:', toplam)
print('Ortalama:', ortalama)
print('En Buyuk:', en_buyuk)
print('En Kucuk:', en_kucuk)
"""
"""Alt ve üst limit olarak belirlenen iki sayının arasında kalan ve belirli
bir sayıya bölünebilen tüm sayıları gösterin. Örneğin 1 ve 80 arasında 5’e
bölünebilen sayıları listeleyin."""
"""
alt_sınır = int(input('Bir alt sınır giriniz:'))
ust_sınır = int(input('Bir üst sınır giriniz:'))
bolme = int(input('Bolme kontrolu yapılacak sayıyı giriniz:'))
i = 0

for i in range(alt_sınır, ust_sınır):
    if i % 7 == 0:
        print("Tam bölünen sayı:", i)
    else:
        continue
print('Program sonlandırıldı.')
"""
"""Kullanıcıdan 0 ile 9 arasında bir rakam isteyin.
Girilen rakama göre aşağıdaki çıktıyı
üreten programın kaynak kodlarını yazın."""
"""
sayı = int(input('(0-9) arasında bir sayı giriniz:'))
if sayı >= 0 and sayı <= 9:

    for a in range(1, sayı+1):
        print(str(a)*a)
else:
    print('Sayı 0-9 aralığında değildir.')
"""
"""Aşağıdaki ‘*’ karakterlerinden oluşmuş ve 
bir terim sırasına doğru giden deseni
çizdirin."""
"""
     * # 5 boşluk 1 yıldız
    *** # 4 boşluk 3 yıldız
   ***** # 3 boşluk 5 yıldız
  ******* # 2 boşluk 7 yıldız
 ********* # 1 boşluk 9 yıldız
  ******* # 2 boşluk 7 yıldız
   ***** # 3 boşluk 5 yıldız
    *** # 4 boşluk 3 yıldız
     * # 5 boşluk 1 yıldız
"""
"""
n = int(input('Bosluk Sayısını belirleyin'))
s = ''
# Sayı birden başla n(5) e kadar git
for i in range(1, n+1):
    # Boşluk bırakmak için 5 - 1 (1. döngüde olduğu için 1 yazıldı)
    for j in range(n-i):
        # Burada olan boşluğa boşluk ataması yapıyoruz
        # ki diğer veriler silinmesin.
        s = ' ' + s
        # yıldız eklemek için i kaçıncı değerdeyse onu yazıyor
    for k in range((i*2)-1):
        s = s + '*'
    print(s)
    s = ''
for i in range(n, 0, -1):
    for j in range(n-i):
        s = ' ' + s
    for k in range((i*2)-1):
        s = s + '*'
    print(s)
    s = ''
"""