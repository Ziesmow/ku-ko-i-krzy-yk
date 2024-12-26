
kolka = {
    'a1' : 0,
    'a2' : 0,
    'a3' : 0,
    'b1' : 0,
    'b2' : 0,
    'b3' : 0,
    'c1' : 0,
    'c2' : 0,
    'c3' : 0,
}

def printkolka (kolka):
        for key , value in kolka.items():
            if value == 0 :
                print("   |", end='')
            elif value == 1 :
                print(" x |", end='')
            elif value == 2 :
                print(" 0 |", end='') 
            if key == "a3" :
                print()
            elif key == "b3" :
                print()
            elif key == "a3" :
                print()
        
def ruchpla(kloka):
    wyb = input("gdzie chcesz postawić x:")
    if wyb == 'a1' :
        kolka['a1'] = 1
    elif wyb == 'a2' :
        kolka['a2'] = 1
    elif wyb == 'a3' :
        kolka['a3'] = 1
    elif wyb == 'b1' :
        kolka['b1'] = 1
    elif wyb == 'b2' :
        kolka['b2'] = 1
    elif wyb == 'b3' :
        kolka['b3'] = 1
    elif wyb == 'c1' :
        kolka['c1'] = 1
    elif wyb == 'c2' :
        kolka['c2'] = 1
    elif wyb == 'c3' :
        kolka['c3'] = 1
    else :
        print(f"nie ma takiego pola jak {wyb}")
        



while True :
    printkolka(kolka)
    print()
    ruchpla(kolka)









