"""Dosya İşlemleri - Dosya Okumak."""
"""
with open('asd.txt', 'w', encoding='utf-8') as f:
    f.write('Python\n')
    f.write('Merhaba\n')
    f.write('3.9.4')

"""
with open('asd.txt', 'r') as f:
    # Readline() Fonksiyonu:
    # Read() fonksiyonu bütün satırı okuyorken readline()satırsatır okumayapar.
    # Kullanımı read() fonks ile aynıdır.
    print(f.readline(), end='')
    print(f.readline(), end='')

"""Read() Fonksiyonu:
Bu fonksiyon ile dosyanın tamamı bir kerede okunur ve dosya karakter dizisi
şeklinde okunmaktadır.
oku = open(“dosya.txt”)
print(oku.read())

Readline() Fonksiyonu:
Read() fonksiyonu bütün satırı okuyorken readline() satır satır okuma yapar.
Kullanımı read() fonks ile aynıdır.

Readlines() Fonksiyonu:
Verileri liste veri tipinde okumaktadır.Yani okuma sonunda veriler liste tipindedir.

oku=open(“deneme.txt”)
print=(oku.readlines())
çıktı[‘python’]
"""
