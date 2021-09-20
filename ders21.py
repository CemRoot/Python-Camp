"""Hata Yönetimi - Assert Deyimi"""
# AssertionError
# Assert = İddia
# İddialar derleme sırasında python -o bayrağı ile devre dışı olabilir.
# OF Stateöemt vs Assert vs Raise

veri = []


def ekle(p1: list):
    assert len(p1) != 0, 'Liste uzunluğu 0!'
    p1.append('Python')
    return p1


try:
    print(ekle(veri))
except AssertionError as mesaj:
    print('Hata:', mesaj)
