
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
    "wynik" : 5,
}

n = 0
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
        
def wynikx(kolka):
    if kolka["a1"] == 1 and  kolka["a2"] == 1 and  kolka["a3"] == 1:
        print("wygrałeś x")
        kolka["wynik"] = 6
    elif kolka["a1"] == 1 and  kolka["b1"] == 1 and  kolka["c1"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    elif kolka["a1"] == 1 and  kolka["b2"] == 1 and  kolka["c3"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    elif kolka["a2"] == 1 and  kolka["b2"] == 1 and  kolka["c2"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    elif kolka["b1"] == 1 and  kolka["b2"] == 1 and  kolka["b3"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    elif kolka["c1"] == 1 and  kolka["c2"] == 1 and  kolka["c3"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    elif kolka["a3"] == 1 and  kolka["b3"] == 1 and  kolka["c3"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    elif kolka["a3"] == 1 and  kolka["b2"] == 1 and  kolka["c1"] == 1:
        print("wygrałeś x")
        wynik = 1
        return wynik
    




while n < 1 :
    wynikx(kolka)
    printkolka(kolka)
    if kolka["wynik"] == 6:
        break
    print()
    ruchpla(kolka)










