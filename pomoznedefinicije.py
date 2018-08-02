import time


def igralci():
    stevilo_igralcev = input('\nŠtevilo igralcev: ')
    try:
        stevilo_igralcev = int(stevilo_igralcev)
    except:
        print('Število igralcev mora biti celo število, večje od 0')
        return igralci()
    if type(stevilo_igralcev) == int and stevilo_igralcev > 0:
        sez_igralcev = []
        for i in range(stevilo_igralcev):
            igralec = input('Igralec št. ' + str(i + 1) +': ')
            if igralec != '':
                sez_igralcev.append(igralec)
            while igralec == '':
                print('Napisati morate vsaj en znak. Še enkrat vpišite ime tega igralca.')
                igralec = input('Igralec št. ' + str(i + 1) +': ')
                if igralec != '':
                    sez_igralcev.append(igralec)
                else:
                    pass
        return sez_igralcev
    else:
        print('Število igralcev mora biti celo število, večje od 0')
        return igralci()


def tekme():
    stevilo_tekem = input('\nŠtevilo tekem: ')
    try:
        stevilo_tekem = int(stevilo_tekem)
    except:
        print('Število tekem mora biti celo število, večje od 0')
        return tekme()
    if type(stevilo_tekem) == int and stevilo_tekem > 0:
        sez_tekem = []
        for i in range(stevilo_tekem):
            while True:
                tekma = input('Tekma št. ' + str(i + 1) +': ')
                if tekma == '':
                    print('Tekma mora imeti vsaj en znak. Ponovno vpiši tekmo.')
                else:
                    sez_tekem.append(tekma)
                    break
        return sez_tekem
    else:
        print('Število tekem mora biti celo število, večje od 0')
        return tekme()


def napovedi(vsi_igralci, vse_tekme):
    print('\nNapovejte rezultate. Napoved naj bo oblike: "a1:b1, ..., an:bn".\nNajvišja možna napoved je 9:9.')
    slovar = {}
    for igralec in vsi_igralci:
        while True:
            napoved = input('Napoved - {}: '.format(igralec))
            if napoved.count(':') != len(vse_tekme):
                print('Napačen vnos. Poskusite ponovno.\n(Napaka: napačno število tekem, nepravilen zapis, ...)')
                continue
            elif napoved.index(':') == napoved.index(':') + 2:
                print('Napačen vnos. Poskusite ponovno.\n(Napaka: napačno število tekem, nepravilen zapis, ...)')
                continue
            seznam = []
            for i in range(len(napoved)):
                if 2 <= i and napoved[i] == napoved[i - 2] == ':':
                    print('Napačen vnos. Poskusite ponovno.\n(Napaka: napačno število tekem, nepravilen zapis, ...)')
                    break
                if napoved[i] == ':':
                    try:
                        a = int(napoved[i - 1])
                        b = int(napoved[i + 1])
                        seznam.append((a, b))
                    except:
                        print('Napačen vnos. Poskusite ponovno.\n(Napaka: napačno število tekem, nepravilen zapis, ...)')
                        break
            if len(seznam) == len(vse_tekme):
                break
        slovar[igralec] = seznam
    return slovar


def rezultati(vse_tekme):
    sez_rezultatov = []
    print('\nNapišite rezultate tekem. Rezultat naj bo oblike "a:b". \nNajvišji možni rezultat je 9:9')
    for tekma in vse_tekme:
        while True:
            rezultat = input("Rezultat tekme {} : ".format(tekma)).replace(' ','')
            if rezultat[0] == ':' or rezultat.count(':') != 1 or len(rezultat) != 3:
                print('Napačen vnos. Poskusite znova.')
                continue
            try:
                ':' in rezultat
                type(rezultat.index(':') - 1) == int
                type(rezultat.index(':') + 1) == int
                a = int(rezultat[rezultat.index(':') - 1])
                b = int(rezultat[rezultat.index(':') + 1])
                sez_rezultatov.append((a, b))
                break
            except:
                print('Napačen vnos. Poskusite znova.')
    return sez_rezultatov


def tockuj(napoved, rezultat):
    if napoved == rezultat:
        return (5, 0)
    a = napoved[0]
    b = napoved[1]
    c = rezultat[0]
    d = rezultat[1]
    if a - b == c - d:
        return (3, 0)
    elif (a > b and c > d) or (b > a and d > c):
        return (2, abs(a - b - (c - d)))
    else:
        return (0, abs(a - b) + abs(c - d))


def sestevanje_oklepajev(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def krog(vsi_igralci, vse_tekme, vse_napovedi, vsi_rezultati, lestvica):
    nova_lestvica = {}
    for x in vse_napovedi:
        igr_tocke = lestvica[x]
        napoved = vse_napovedi[x]
        for i in range(len(napoved)):
            tocke = tockuj(napoved[i], vsi_rezultati[i])
            igr_tocke = sestevanje_oklepajev(tocke, igr_tocke)
        nova_lestvica[x] = igr_tocke
    return nova_lestvica


def zmagovalec_je(slovar):
	sez = []
	for item in slovar.items():
		sez.append(item)
	zmagovalec = sorted(sez, key=lambda x: (-x[1][0], x[1][1]))[0][0]
	return zmagovalec


def ali_je_konec(lestvica):
    while True:
        konec = input('\nAli je prvenstvo že zaključeno? (DA, NE): ')
        if konec == 'DA':
            print('\nPrvenstvo je zaključeno. Zmagal je *{}*. \nZa izhod pritisnite tipko X desno zgoraj.'.format(zmagovalec_je(lestvica).upper()))
            time.sleep(100)
        elif konec == 'NE':
            print('\nLestvica je shranjena. Trenutno vodi *{}*. Se vidimo prihodnjič! \nZa izhod pritisnite tipko X desno zgoraj.'.format(zmagovalec_je(lestvica).upper()))
            time.sleep(100)
        else:
            print('Napačen vnos. Odgovorite z DA oz. NE.')
