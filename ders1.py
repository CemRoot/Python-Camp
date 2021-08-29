""" Veri Türleri ."""

"""Temel Veri Türleri
        Sayısal Türler: int, float, complex
        Boole Türü: bool (True&False)
    Gelişmiş Türler
        Metinsel Tür: list, tuple, range
        Dizi Türleri: dict
        Eşleme Türleri: set, frozenset
        İkili Türler: Bytes, bytearray, memoryview
"""
Veri = frozenset('book')
int()
float()
complex()
print(Veri)

"""Metin Biçimlendirme (format(), F-string >= 3.6.x)."""
İsim = 'Cem'
Soyİsim = 'Koyluoglu'
# String için %s, sayısal veriler için %d kullanılır. C dilinde olduğu gibi.
print('%s %s' % (İsim, Soyİsim))

# Fakat Python'da bu şekilde format fonksiyonu ile kullanılır.
print('{0} {1}'.format(İsim, Soyİsim))

# F-strings biçimi
# Yanına eklenidiği zaman 15 boşluk eklemiş oluyoruz.
# Print(f'{İsim:*<15} {Soyİsim}') ilk başa yıldız ekleyecektir.
print(f'{İsim:15} {Soyİsim}')

# Raw String bir stringi ham bir şekilde yazar.
print(r'\n kaçış karakteri bir alt saıra geçmeye yarar')

"""Bit (bitwise) Operatörleri."""
bit = 0b10100
print(bit)
# Veya
bit1 = 50
print(bin(bit1))

# And yada &
# T + T = T
# T + F = F
# F + T = F
# F + F = F
x = 40
y = 50
print(bin(x))
print(bin(y))
z = x & y
print(bin(z))


# OR yada |
# T + T = T
# T + F = T
# F + T = T
# F + F = F

x = 40
y = 50
print(bin(x))
print(bin(y))
z = x | y
print(bin(z))

# XOR yada ^
# T + T = F
# T + F = T
# F + T = T
# F + F = F

x = 40
y = 50
print(bin(x))
print(bin(y))
z = x ^ y
print(bin(z))
