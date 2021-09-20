"""Parametre olarak verilen bir cümledeki büyük harf ve küçük harflerin
sayısını bulan bir fonksiyon yazın"""


def harf_tespit(Veri):
    # Buyuk ve kucuk harflari 0'a eşitledik...
    # ...ve sözlük veri tipinde atatık.
    # Dist(sözlük) tipinden oluşturma sebebimizde anahtar-değer tespiti
    # ...kontrolu yapıyoruz.
    grup = {"buyuk_harf": 0, "kucuk_harf": 0}
    #  Verilen kelimeleri büyük küçüklüğünü kontrolu için...
    # ...girilen kelimeyi for döngüsüyle yazıyor ve in ile girilen veride
    # ...gezmiş oluyoruz.
    for i in Veri:
        # Buyuk harf tespiti için kullandığımız fonksiyon 'issupper()'
        if i.isupper():
            grup["buyuk_harf"] += 1
        # Kucuk harf tespiti için kullandığımız fonksiyon 'islower()'
        elif i.islower():
            grup["kucuk_harf"] += 1
        else:
            pass
# shift+alt+a ile hızlı yorum satırı yapabilirsiniz.
    print('Cumle:', Veri)
    print('Buyuk Harf Sayisi:', grup["buyuk_harf"])
    print('Kucuk Harf Sayisi:', grup["kucuk_harf"])


harf_tespit('Python Programlama Dili')
# Yukarıdaki kodumuzda return kullanmadık gerek duymadığımız için
# fakat eğer return kullanarak yazmamız gerekseydi şu şekilde yazabilirdik.
''' return f'Cumle:{Veri},\
           Buyuk Harf:{grup["buyuk_harf"]},\
           Kucuk Harf:{grup["kucuk_harf"]}'


Sonuc = harf_tespit('Python Prgoramlama Dili')
print(Sonuc) '''
# Böylece bu fonksiyonu hem return değerine sahip bir şekilde yazdırdık
# hemde return olmadanda yazdırabildik bu şekildeede farkını görebildik.
