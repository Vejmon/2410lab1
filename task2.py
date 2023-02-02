#skal ta inn en liste med tall, utføre en beregning av Jains Fairness Index
#hvor et tall mellom 0->1 sier hvor rettferdig fordelingen av systemets resurser
def jainsall (tall):
    #setter variablene for over og under brøkstreken, sørger også for at disse er float.
    totOver = 0.0
    totUnder = 0.0
    for i in tall:
        #oversetter listen til float, hvis ikke sender vi feilmelding og slutter.
        try:
            i = float(i)
        except:
            print("listen kan bare inneholde tall")
            return
        #summerer listens innhold over brøken.
        totOver += i
        #summerer listen innhold opphøyd i annen under brøken.
        totUnder += (i ** 2)
    #opphøyer totalsummen over brøken, og ganger totalsummen under brøken med antall element i listen.
    totOver = totOver ** 2
    totUnder = totUnder * len(tall)
    return totOver / totUnder