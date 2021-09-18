"""Kaç parametre alacağı belirli olmayan ve aldığı parametredeki sayıların
toplamını geriye değer olarak döndüren bir fonksiyon yazın."""

# * tek yıldız tuple ** çift yıldız sözlük olarak tutar


def topla(*sayi):
    toplam = 0
    for i in sayi:
        # toplam += i
        toplam = toplam + i
    return toplam


"""def topla(*sayi):
    # Hazır fonksiyon ilede
    # bunu bu şekilde yazabilirdik
    return sum(sayi)
    """

print('Sonuc:', topla(4, 5, 6))
