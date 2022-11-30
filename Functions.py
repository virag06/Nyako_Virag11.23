from data import *
from os import system

def menu():
    system('cls')
    print('------------MENÜ------------')
    print('0 - Kilépés')
    print('1 - Virágok')
    print('2 - Színek')
    print('3 - Legolcsóbb virág')
    print('4 - Legdrágább virág')
    print('5 - Csokor összeállítása')
    return input('Kérem válasszon: ')

def viragokKiir():
    system('cls')
    print('----------VIRÁGOK-----------')
    for i in range(0,len(viragok)):
        print(f' - {viragok[i]}: {szin[i]}, {ar[i]} Ft')
    input('Tovább...')

def szinekKiir():
    system('cls')
    print('-----------SZÍNEK-----------')

def legolcsobb():
    system('cls')
    print('------LEGOLCSÓBB VIRÁG------')
    minPoz=0
    for i in range(1,len(ar)):
        if ar[i]<ar[minPoz]:
            minPoz=i
    print(f'A legolcsóbb virágunk ({ar[minPoz]} Ft):')
    for i in range(0,len(ar)):
        if ar[i]==ar[minPoz]:
            print(f'\t{viragok[i]}')
    input('Tovább...')

def legdragabb():
    system('cls')
    print('------LEGDRÁGÁBB VIRÁG------')

def csokor():
    system('cls')
    print('----CSOKOR ÖSSZEÁLLÍTÁSA----')