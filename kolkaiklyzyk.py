
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

wyniki = [1 , 2]
lsaosud = ["X", "O"]
n = 0


def printkolka (kolka):
        for key , value in kolka.items():

            if value == 0 :
                print("   |", end='')
            elif value == 1 :
                print(" X |", end='')
            elif value == 2 :
                print(" O |", end='') 
            if key == "a3" :
                print()
            elif key == "b3" :
                print()
            elif key == "a3" :
                print()
        
def ruchplax(kloka):
    wyb = input("gdzie chcesz postawić X:")
    if wyb == 'a1' :
        if kolka["a1"] == 0:
            kolka['a1'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'a2' :
        if kolka["a2"] == 0:
            kolka['a2'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'a3' :
        if kolka["a3"] == 0:
            kolka['a3'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'b1' :
        if kolka["b1"] == 0:
            kolka['b1'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'b2' :
        if kolka["b2"] == 0:
            kolka['b2'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'b3' :
        if kolka["b3"] == 0:
            kolka['b3'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'c1' :
        if kolka["c1"] == 0:
            kolka['c1'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'c2' :
        if kolka["c2"] == 0:
            kolka['c2'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'c3' :
        if kolka["c3"] == 0:
            kolka['c3'] = 1
        else :
            print("njie możesz postawić tu Znaku")
    else :
        print(f"nie ma takiego pola jak {wyb}")

def ruchplao(kloka):
    wyb = input("gdzie chcesz postawić O:")
    if wyb == 'a1' :
        if kolka["a1"] == 0:
            kolka['a1'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'a2' :
        if kolka["a2"] == 0:
            kolka['a2'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'a3' :
        if kolka["a3"] == 0:
            kolka['a3'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'b1' :
        if kolka["b1"] == 0:
            kolka['b1'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'b2' :
        if kolka["b2"] == 0:
            kolka['b2'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'b3' :
        if kolka["b3"] == 0:
            kolka['b3'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'c1' :
        if kolka["c1"] == 0:
            kolka['c1'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'c2' :
        if kolka["c2"] == 0:
            kolka['c2'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    elif wyb == 'c3' :
        if kolka["c3"] == 0:
            kolka['c3'] = 2
        else :
            print("njie możesz postawić tu Znaku")
    else :
        print(f"nie ma takiego pola jak {wyb}")

def wynikx(kolka):
    for i in wyniki:
        if kolka["a1"] == i and  kolka["a2"] == i and  kolka["a3"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["a1"] == i and  kolka["b1"] == i and  kolka["c1"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["a1"] == i and  kolka["b2"] == i and  kolka["c3"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["a2"] == i and  kolka["b2"] == i and  kolka["c2"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["b1"] == i and  kolka["b2"] == i and  kolka["b3"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["c1"] == i and  kolka["c2"] == i and  kolka["c3"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["a3"] == i and  kolka["b3"] == i and  kolka["c3"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
        elif kolka["a3"] == i and  kolka["b2"] == i and  kolka["c1"] == i:
            print(f"wygrałeś {lsaosud[i-1]}")
            kolka["wynik"] = 6
    zera = []
    for i , j in kolka.items():
        if i != "wynik" :
            if j == 0 :
                zera.append(j + 23)
            else:
                pass

    if len(zera) > 0 :
        pass 
    if len(zera) == 0:
        print("nikt nie wygrał")
        kolka["wynik"] = 6
            
        
            
        

while n < 1 :
    printkolka(kolka)
    wynikx(kolka)
    if kolka["wynik"] == 6:
        break
    print()
    ruchplao(kolka)
    printkolka(kolka)
    print()
    wynikx(kolka)
    if kolka["wynik"] == 6:
        break
    print()
    ruchplax(kolka)
print()








