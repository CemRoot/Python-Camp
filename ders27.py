"""Dosya İşlemleri - Dosya Güncellemek"""
"""
with open('asd.txt', 'r+') as f:
    # eski veri değişkeninde saklansın
    eski_veri = f.read()
    # Dosyanın imleci en başına gitsin
    # Amacım yukarıya eklemek olduğu için en başa gönderdim.
    f.seek(0)
    # Şimdi verileri tekrardan yazma işlemi yapıyorum.
    # Yeni veri ile eski verileri birleştirmek içinde şu şekilde yazıyorum.
    # Bunun sebebi eğer eski veriyi eklemezsem dosya kaybolacaktır.
    f.write('Merhaba 1234\n' + eski_veri)
"""

# En sonuna güncelleme yapmak için yazacağım kod şu şekilde olacaktır.

with open('asd.txt', 'a') as f:
    f.write('\nSon Veri Ekleme...')

# Dosyanın en sonunda ekleme yapmak içinse şu şekilde yazmamız gerekebilir.
with open('asd.txt', 'r+') as f:
    # eski veri değişkeninde saklansın
    # readlines yazmamın sebebi ise bütün verileri okuyor
    # ve her bir satırı liste türünde döndürüyordu.
    eski_veri = f.readlines()
    # ikinci satırda ekleme yapmak istiyorsak
    # format liste olduğu için insert fonks kullancağım.
    eski_veri.insert(1, 'Örnek veri\n')
    # Bunu tekrardan dosyaya yazdırmam için dosya imleci en başa alıyorum.
    f.seek(0)
    # Bu dosyaya liste eklememize yarıyor bu formatta
    f.writelines(eski_veri)
    print(eski_veri)
