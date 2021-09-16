"""Parametre olarak bir sayı alan ve aldığı bu sayının asal olup olmadığını
gösteren bir fonksiyon yazın. Bu fonksiyon geriye değer döndüren bir
fonksiyon olmalıdır. Sayı asal ise ekran çıktısı olarak ‘true’ eğer asal
değilse ekran çıktısı olarak ‘false’ sonucunu versin.
(Fonksiyonu PEP257 standartlarına uygun olarak yazın.)
"""


def asal_sayi_kontrolu(sayi: int):
    """Asal Sayi Kontrolu.

    Args:
        sayi (int): int turunde veri alır.

    Returns:
        bool: True yada False sonucunu verir.
    """
    if(sayi < 2):
        return False
    elif(sayi == 2):
        return True
    else:
        for i in range(2, sayi):
            if(sayi % i == 0):
                return False
        return True


sayi = int(input('Lütfen bir sayı giriniz:'))
print('Sonuç:', asal_sayi_kontrolu(sayi))
