#velger å gjenbruke koden fra task2
from task2 import jainsall

#åpner tekstfilen og leser av verdiene i den.
with open('noenTall') as tekstFil:
    #setter opp en liste med forhåpentligvis tall.
    tall = []
    for line in tekstFil:
        tall.append(line.split()[0])
    #siden jainsall funksjonen tar seg av feil i listen trenger vi ikke gjøre det her.
    print(jainsall(tall))