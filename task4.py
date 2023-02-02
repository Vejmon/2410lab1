#gjenbruker funksjonen fra task2 igjen.
from task2 import jainsall

#skal lese av en liste med tall og enheter, og sende disse tallene som om de var gitt i Mbps.
with open('andreTall') as tekstFil:
    #lager to lister, den ene skal holde verdien per linje, den andre enheten til verdien.
    tall = []
    enhet = []
    for line in tekstFil:
        tall.append(line.split()[0])
        enhet.append(line.split()[1])
    #looper igjennom listen, og gir tallverdien riktig mengde utifra enheten.
    teller = 0
    for i in tall:
        #hvis textfilen ikke er i riktig format printes feilmeldingen med noen instruksjoner.
        try:
            i = float(i)
        except:
            print('listen må ha dette oppsettet')
            print('tall enhet')
            print('32 Gbps')
        #konverterer tallverdier som ikke er gitt som Mbps
        if enhet[teller][0] == 'K':
            i = i / 1024
        elif enhet[teller][0] == 'G':
            i = i * 1024
    #sender listen til jainsall fra task2
    print(jainsall(tall))