summa = 1.1
nachalo = 0.01
edinica = 0.01
raznica = 1
nashli = False
for myach in range(int(nachalo * 100), int(summa * 100), int(edinica * 100)):
    myach = myach / 100
    for bita in range(int(nachalo * 100), int(summa * 100), int(edinica * 100)):
        bita = bita / 100
        if myach + bita == summa and abs(myach - bita) == raznica:
            nashli = True
            break
    if nashli:
        break

if nashli:
    print('Бита стоит {}$, а мяч {}$'.format(bita, myach))
else:
    print('Говно какое-то, а не задача')