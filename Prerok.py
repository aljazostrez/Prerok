from pomoznedefinicije import *
import ast

print('Dobrodošli v programu *Prerok*. Uporablja se za točkovanje uspešnosti napovedi.\n\
Program vas bo sam vodil skozi celotno točkovanje.\n\
Če se zmotite in potrdite izbiro, zaprite program in na novo začnite.')
while True:
    zacetek = input('\nAli je to novo prvenstvo? (DA, NE): ')
    if zacetek == 'DA':
        print('\nZačetek.')
        vsi_igralci = igralci()
        vse_tekme = tekme()
        vse_napovedi = napovedi(vsi_igralci, vse_tekme)
        vsi_rezultati = rezultati(vse_tekme)
        lestvica = {}
        for igralec in vsi_igralci:
            lestvica[igralec] = (0, 0)
        nova_lestvica = krog(vsi_igralci, vse_tekme, vse_napovedi, vsi_rezultati, lestvica)
        ime = input('\nKako naj bo ime datoteki, kjer bo shranjena lestvica?\n\
Taka datoteka še ne sme obstajati. \nDatoteka: ')
        with open(ime, 'w') as dat:
            dat.write(' '.join(vsi_igralci) + '\n')
            dat.write(str(nova_lestvica))
        ali_je_konec(nova_lestvica)
    elif zacetek == 'NE':
        done = None
        while not done == True:
            obstojeca_datoteka = input('\nVnesite ime obstoječe datoteke z lestvico\n(brez končnice .txt): ')
            try:
                with open(obstojeca_datoteka, 'r') as dat:
                    vsi_igralci = dat.readline()[:-1].split(' ')
                    lestvica = ast.literal_eval(dat.readline())
                done = True
            except FileNotFoundError:
                print('Datoteka ne obstaja. Še enkrat vpišite ime datoteke.\n\
Če je to novo prvenstvo, zaprite okno in znova zaženite program.')
        vse_tekme = tekme()
        vse_napovedi = napovedi(vsi_igralci, vse_tekme)
        vsi_rezultati = rezultati(vse_tekme)
        nova_lestvica = krog(vsi_igralci, vse_tekme, vse_napovedi, vsi_rezultati, lestvica)
        with open(obstojeca_datoteka, 'w') as dat:
            dat.write(' '.join(vsi_igralci) + '\n')
            dat.write(str(nova_lestvica))
        ali_je_konec(nova_lestvica)
    else:
        print('Napačen vnos. Odgovorite z DA oz. NE.')


