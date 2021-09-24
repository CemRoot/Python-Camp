"""Dosya İşlemleri - With Deyimi"""
f = None
try:
    f = open('asd.txt', 'x')
    f.write('Python')
except OSError as e:
    print(e)
finally:
    f.close()
# Yukarıda ki kodun kısa hali bu şekilde olmaktadır.
with open('asd2.txt', mode='w', encoding='utf-8') as f:
    f.write('HELLO!')
# Bu şekildede kodu yazabilirdik with deyimi...
# otomatik olarak dosyayı kapatacaktır...
# ve burada  parametresine ihtiyaç kalmayacaktır.
