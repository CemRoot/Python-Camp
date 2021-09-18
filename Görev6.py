"""Parametre olarak bir kelime yada cümle alan ve aldığı bu değerin palindrom
olup olmadığını ‘True’ yada ‘false’ olarak geriye döndüren bir fonksiyon yazın.
Palindrom, tersten okunuşu ile normal okunuşu aynı olan cümle, sözcük ve sayı-
lara denilmektedir."""


def palindrom(veri):

    sol_indis = 0
    sag_indis = len(veri) - 1

    while sag_indis >= sol_indis:
        if not(veri[sol_indis] == veri[sag_indis]):
            return False
        sol_indis += 1
        sag_indis -= 1
    return True


metin = input('Lütfen bir veri giriniz:')
print('Sonuc:', palindrom(metin))
