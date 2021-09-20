"""Try-Except-Finally Yapısı"""

# En çok kullanılan yapılardan bir tanesidir.
# Bu blok programda hatada olsa da olmasa da çalışır.

try:
    sayi1 = int(input('sayi gir: '))
    sayi2 = int(input('sayi gir: '))
except ValueError as mesaj:
    print('lütfen sadece sayısal değer girin')
    print('hata mesajı: ', mesaj)
finally:
    print('Bu kod her zaman çalışır')

print('Blok dışı')
