"""Fonksiyonlarda - Gecerlilik alanları"""
# Global x fonksiyonun içindende ulaşabiliriz dışındanda ulaşabiliriz.
x = 'Python'


def func():
    # Local 'Y' sadece tanımlı olduğu girintili alandan ulaşılabilir.
    y = 'merhaba'
    print('Fonksiyon içi', x)
    print('Fonskyion içi', y)
    return


func()
print('Fonksiyon dışı', x)
