# Bir python programında istisna türünde hata yaptığımızda bu hatayı
# yakalarken hata mesajını da ayrıca görmek isteyebiliriz.
try:
    sayi1 = int(input('sayi gir:'))
    sayi2 = int(input('sayi gir:'))
    print(sayi1 * sayi2)
except ValueError as mesaj:
    print('lütfen sadece sayısal değer girin')

    # burada ki mesajı tuple şekilde alabiliriz.
    """print(mesaj.args)"""

    # Normal yazımda bu şekildedir.
    print('hata mesajı:', mesaj)

print('Blok Dışı')
