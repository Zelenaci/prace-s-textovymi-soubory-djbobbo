
#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum: -
# Autor: Bohous Steier 
############################################################################
from random import randint, choice

############################################################################


def prevody(soubor1, soubor2):   # Převod vybrané line v souboru na malá písmena (soubor2.write(line.lower())
    for line in soubor1:
        soubor2.write(line.lower())



def nahrada(soubor1, soubor2, znak1, znak2):  # nahrazení znaku jiným znakem (v souboru)
     while True:
        pismeno = soubor1.read(1)
        if pismeno == '':
            soubor1.seek(0)
            break
        else:
            if pismeno.upper() == znak1.upper(): 
                soubor2.write(znak2)
            else:
                soubor2.write(pismeno) 



def statistika (soubor1): # statistika pro soubor1 vybraný soubor, seek slouží ke změně file handle na danou konkrétní pozici 
    znaky = {}
    while True:
        pismeno = soubor1.read(1)
        if pismeno == '':
            soubor1.seek(0)
            break
        else:
            if pismeno not in znaky.keys(): # not in - není v
                znaky[pismeno] = 1
            else:
                znaky[pismeno] += 1
    for key in sorted(znaky.keys()):
        if key == '\n':
            print(f'(\\n) --- {znaky[key]}')
        else:
            print(f'({key}) --- {znaky[key]}')



def generator_slov (minchars = 2, maxchars = 7):  # generátor slov o minimálně 2 a maximálně 7mi znacích , zadefinujeme so a sa a využijeme random 
    
    souhlasky = 'q w r t p s d f g h j k l z x c v b n m'
    samohlasky = 'a e i y o u'
    
    pocet = random.randint(minchars, maxchars)
    output = ''
    input = random.randint(0, 1)                           
    for i in range(pocet):
        if i % 2 == input:
            output += random.choice(samohlasky)
        else:
            output += random.choice(souhlasky)
    return output


def generator2_vet (maxwords, soubor2) : # generátor celých vět se slovy daného rozměru, spojíme to s generátorem slov co už máme nad tim ( output += generator_slov() + ' ')
    output = ''
    for i in range(maxwords):
        output += generator_slov() + ' '
    output = output.capitalize()[0:-1] + '.\n'
    for line in output:
        soubor2.write(line)      


def menu():    #menu na zadávání souborů, zadefinujeme volby 1 az 4 a kazdá volba neco dela ,popsané 
    try:
        s1 = open(input('Zadej  soubor > '), 'read')
        s2 = open(input('Zadej soubor dalsi > '), 'write')
    except FileNotFoundError:
        print('Zadal jsi spatny soubor')
        exit(1)

    run = True
    while run:
        print('''
        1 - Prevod daneho souboru na mala pismena
        2 - Nahrazeni nami vybranym znakem jinym znakem
        3 - Statistika pro soubor
        4 - Generovani nahodnych slov a vet
        ''')
        volba = input('Jakou funkci chcete vybrat? > ')
        if volba == '1':
            prevody(s1, s2)
        elif volba == '2':
            nahrada(s1, s2, input('Zadej znak1 > '), input('Zadej znak 2 > '))
        elif volba == '3':
            statistika(s1)
        elif volba == '4':
            maxwords = int(input('Zadej max pocet slov > '))
            while maxwords < 1:
                print('Neplatny pocet slov')
                maxwords = int(input('Zadej max pocet slov > '))
            generator2_vet(maxwords, s2)
        else:
            run = False
            s1.close()
            s2.close()   


if __name__ == "__main__":   # nevim proc to tu je 
    menu()