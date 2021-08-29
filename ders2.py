"""None veya Null Veri Türü."""

Sayi = 0
Metin = ''
Veri = None

print(Veri)
print(type(Veri))
"""Kullanıcı Etkilişimi."""
# Hatırlatma input normal bir şekilde kullanılırsa.
# string tipinde döndürecektir. sayısal değerler için int(input()) yazılır.
Out = input('Lütfen Bir Değer Giriniz: ')
print('Girdğiniz Değer: %s' % (Out))
# Veya bu şekildede parametre verebiliyoruz.
print('Girdğiniz Değer:', Out)
