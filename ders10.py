"""Fonksiyonlar - Return deyimi"""
# Temelde 2’e ayıran deyimdir.Bazı fonksiyonlar değer döndürürken=
# (return deyimi kullananlar) Bazı fonksiyonlar ise değer döndürmeyen
#  (return deyimi kullanmayan) fonksiyonlardır.Şu örneği verebilirim:
#  Bir iş verdiğinizi düşünün verdiğiniz işin geri dönüşü önemli değilse
# bu değer döndürmeyen fonksiyonlara örnektir. Yani sadece fonksiyon o işi yapar ve bitirir.
# Ancak bir işin sonucunu görmek istiyorsanız o iş bittiğinde size geri dönüş yapılır
# bu ise değer döndüren yani return  deyimi kullanılan fonksiyonlara örnektir.
# !!NOT!!: Nasıl “BREAK” komutundan sonra hiçbir kod çalışmıyorsa “RETURN”
# deyiminden sonrada fonksiyondan çıkılır.


def islem():
    print('Hi')


Sonuc1 = islem()
# Sonuc1 değer döndürmediği için saklanamaz ve None yazsını basar ekrana
print(Sonuc1)


def islem2():
    print('Çalışır')
    return 'Merhaba'
    print('çalışmayacak')


Sonuc = islem2()
print(Sonuc)
