"""Cümledeki kelime sayısı."""

Cumle = str(input('Cümle giriniz:'))
sayac = 0
for i in Cumle:
    if i == ' ':
        sayac += 1

print('Cumlede sayısı:', sayac+1)
