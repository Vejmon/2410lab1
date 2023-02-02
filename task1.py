#jains skal utføre Jains Fariness Index for to gitte tall.
def jains (v1, v2):
    #sender feilmelding hvis funksjonen ikke får to tall.
    if not (isinstance(v1, int) or isinstance(v1,float)) and (isinstance(v2, int) or isinstance(v2, float)):
        print("må være tall")
        return

    #utfører beregningen over og under brøken.
    over = (v1 + v2)**2
    under = 2 * (v1 ** 2 + v2 ** 2)
    return over / under
