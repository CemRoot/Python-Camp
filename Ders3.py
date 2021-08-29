"""List Veri Tipi . """
liste = ['Elma', 'Python', True, ['Armut', False], 10, 10.5]
print(liste)
liste[0] = False
# İçinde listeye girebilmek için kullandım.
print(liste[3][0])
print(type(liste))
print(len(liste))
print(dir(liste))
# Listeye bir eleman eklemek için kullandığım fonksiyon.
liste.append(25)
# İstediğimiz bir yere elema eklemek istersek.
liste.insert(1, 'Kivi')
# Eleman çıkarmak istersem
liste.remove(True)
# İçeri değer vermezsek en son elemanı silmektedir.
liste.pop()
# Eğer istediğimiz bir elemanı silmek istersek.
# Birinci indeksi siler.
liste.pop(1)
""" Pop ve Remove arasında ki en büyük fark Pop'da geri getirebiliyoruz
    fakat Remove fonksiyonunda geri getiremiyoruz. """
