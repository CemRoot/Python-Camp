"""Dosya İşlemleri - Dosya Üzerinde İşlemler."""

with open('asd.txt', 'r') as f:
    # tell fonksiyonu sayesinde imlecin konumunu öğrenebiliriz.
    print(f.tell())
    # Okuma işlemi yapıyoruz.
    print(f.read())
    print(f.tell())
    # İmleci başa almak için
    f.seek(0)
    print(f.read())
