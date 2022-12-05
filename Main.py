from Functions import *
from os import system

choice=''
while choice!='0':
    system('cls')
    choice=menu()
    if choice=='1':
        system('cls')
        viragokKiir()
    if choice=='2':
        system('cls')
        szinekKiir()
    if choice=='3':
        system('cls')
        legolcsobb()
    if choice=='4':
        system('cls')
        legdragabb()
    if choice=='5':
        pass