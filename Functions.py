from data import virag,ar,szin
from os import system

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0 - Kilépés')
    print('1 - Virágok')
    print('2 - Színek')
    print('3 - Legolcsóbb virág')
    print('4 - Legdrágább virág')
    print('5 - Csokor összeállítása')
    return input('Kérem válasszon:...')

def viragokKiir():
    system('cls')
    print('--------VIRÁGOK---------')

def szinekKiir():
    system('cls')
    print('---------SZÍNEK---------')

def legolcsobb():
    system('cls')
    print('----LEGOLCSÓBB VIRÁG----')

def legdragabb():
    system('cls')
    print('----LEGDRÁGÁBB VIRÁG----')

def csokor():
    system('cls')
    print('--CSOKOR ÖSSZEÁLLÍTÁSA--')