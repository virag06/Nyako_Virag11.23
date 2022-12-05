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
    bekertSzin=input('Kérem adjon meg egy színt: ')
    db=0
    for i in range(0, len(szin)):
        if szin[i]==bekertSzin:
            print(f'-{bekertSzin} {viragok[i]}')
            db+=1
    if db==0:
        print('Nincs ilyen színű virágunk.')
    input('Tovább...')

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
            print(f'- {viragok[i]}')
    input('Tovább...')

def legdragabb():
    system('cls')
    print('------LEGDRÁGÁBB VIRÁG------')
    maxPoz=0
    for i in range(1,len(ar)):
        if ar[i]>ar[maxPoz]:
            maxPoz=i
    print(f'A legdrágább virágunk ({ar[maxPoz]} Ft):')
    for i in range(0,len(ar)):
        if ar[i]==ar[maxPoz]:
            print(f'- {viragok[i]}')
    input('Tovább...')

def csokor():
    system('cls')
    print('----CSOKOR ÖSSZEÁLLÍTÁSA----')
    összeg = 0
    bekertViragdb = int(input('Kérem adja meg, hány virágból álljon a csokor: '))
    for i in range(0,int(bekertViragdb)):
        #igen = False
        bekertVirag = input("Kérem adjon meg egy virágot: ")
        for j in range(0,len(viragok)):
            if viragok[j] == bekertVirag:
                összeg = összeg + int(ar[j]) 
                #igen = True
        #if igen == False:
            #print("Nincs ilyen Virág")
            #bekertViragdb +=1
    print(f"{összeg} Ft")
    
    input('Tovább...')
