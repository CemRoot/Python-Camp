"""Dosya İşlemleri Giriş"""
"""
Mod	    Açıklama
“r”  –   Read => (Okuma)	Bir dosyayı bu mod ile okuyabiliriz.
Eğer dosya mevcut değilse ekrana bir hata mesajı gelir.

“a”  -   Append => (Ekleme)	Bir dosyaya veri eklemek için kullanılır.
Eğer dosya mevcut değilse otomatik olarak yeni dosya oluşturur

“w”  –   Write => (Okuma) 	Bu mod ile yeni bir dosya açabiliriz.
Eğer dosya mevcut değilse yeni dosya oluşturur.

“x”  –   Create => (Oluşturma) 	Belirtilen dosya oluşturulur.
Eğer dosya mevcut ise hata meydana gelir

“t”  -   Text => 	Bir dosyayı metin modu olarak ele alırız.
“b”  –   Binary =>	Bir dosyayı ikili mod olarak ele alırız.
#BINARY (IKILI DOSYALAR)
    'rb' - Binary dosyaları okumak için kullanılır.
    'wb' - Binaru dosyalara yazmak için kullanılır.
    'ab' - Binary dosyalara eklemek için kullanılır.
    'xb' - Binary dosyalara yazmak için  kullanılır.
   
##########################################################################
'r+' - Read(+) -> Dosya Okuma-Yazma modu.
'w+' - Write(+) -> Dosya Okuma-Yazma modu. Dosya yok ise oluşturur.
'a+' - Append(+) -> Dosya Okuma-Ekleme modu.
'x+' - Create(+) -> Dosya Okuma-Yazma modu. Aynı isimde dosya varsa hata..
##########################################################################
"""
# Dosyalar ile işlem yaparken open() fonksiyonu kullanılır.
# 2 parametre alır 1. dosya adı ve yapmak istediğim komut.

open('C:\\Users\\*****\\Desktop\\Deneme.txt', 'w')
