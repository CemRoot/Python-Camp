"""Parametre olarak verilen bir kelime yada cümlenin tersten yazılışını geriye
döndüren bir fonksiyon yazın. (2. çözüm olarak sadece dilimleme yöntemini
kullanın.)"""


def ters_cevir(veri):
    # Soruyu ele alış biçimini görebilmek yazım şekli
    # Aynı zamanda şirket mülakatlarındada bu şekilde yazmamızı isterler.

    ters = ''
    i = len(veri)
    while i > 0:
        ters += veri[i-1]
        i -= 1
    return ters


print('Sonuc:', ters_cevir('Python Programlama Dili'))

"""Aynı İşlemi dilimleme yönetemiyle bunu yapalım"""


def ters_cevir(veri):
    # Geri dönüşü dilimleme yöntemi yaparak tek satırda bitirdik.
    return veri[::-1]


print('Sonuc:', ters_cevir('Python Programlama Dili'))
