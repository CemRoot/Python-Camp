"""Parametre olarak verilen 3 sayı içerisinde ki en büyük sayıyı geriye değer
döndüren fonksiyonu yazın. Bu işlemi iki fonksiyon kullanarak yapın."""


def max_of_two(x: int, y: int) -> int:
    """Fonksiyon içinde Fonksiyon yaparak en büyük sayıyı bulmak.


    Args:
        x (int): int döndürerek bir sayı istiyoruz
        y (int): int döndürerek bir sayı istiyoruz

    Returns:
        int: fonksiyon içinde fonksiyon çağırarakta sayıların en büyüğü
            bulmaya çalışıyoruz.
    """
    if x > y:
        return x
    # iki şart olduğu için tek bir şekilde yazmak yeterlidir
    return y


def max_of_three(x, y, z):
    return max_of_two(max_of_two(x, y), z)


print('En Büyük sayı:', max_of_three(1, -3, 9))
