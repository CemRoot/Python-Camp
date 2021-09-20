def max_of_three(x, y, z):
    res = x
    res2 = y if y > z else z
    return res if res > res2 else res2


print(max_of_three(1, 2, 3))
