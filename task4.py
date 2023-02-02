#gjenbruker funksjonen fra task2 igjen.
from task2 import jainsall
import sys

#lager feilmelding hvis tekstfilen er i feil format.
#som stopper resten av skriptet fra å kjøre
def fantFeil():
    print('Feil i listen; listen må ha dette oppsettet')
    print('eksempel')
    print('32 Gbps')
    sys.exit('stopper script')

#skal lese av en liste med tall og enheter, og sende disse tallene som om de var gitt i Mbps.
with open('andreTall') as tekstFil:
    #lager listen over tall vi skal sende til jainsall.
    tall = []

    #looper igjennom listen, og setter tallverdi i en liste i riktig størrelse i en liste.
    #hvis textfilen ikke er i riktig format printes feilmeldingen med noen instruksjoner.
    for line in tekstFil:
        #leser av linje for linje i tekstfilen.
        try:
            #sjekker om første del av listen er et tall.
            etTall = float(line.split()[0])
            enEnhet = line.split()[1]

            #konverterer tallverdier som ikke er gitt som Mbps
            if enEnhet[0] == 'K':
                etTall = etTall / 1000
            elif enEnhet[0] == 'G':
                etTall = etTall * 1000

            tall.append(etTall)
        except:
            fantFeil()

    #sender listen til jainsall fra task2
    print(jainsall(tall))