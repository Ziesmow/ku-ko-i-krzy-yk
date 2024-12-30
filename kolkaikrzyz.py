plansza = {
    'a1' : 0, 'a2' : 0, 'a3' : 0,
    'b1' : 0, 'b2' : 0, 'b3' : 0,
    'c1' : 0, 'c2' : 0, 'c3' : 0,
    "zwycięstwo" : 5,
}
mozzwy = [
    ['a1', 'a2', 'a3'],
    ['a1', 'b1', 'c1'],
    ['a1', 'b2', 'c3'],
    ['a2', 'b2', 'c2'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['a3', 'b3', 'c3'],
    ['a3', 'b2', 'c1'],
]
lsabc = ['a', 'b', 'c',]
ls123 = ['1', '2', '3']
zajete = [1, 2]
lsosub = ["O", "X"]
tura = 1

def printkolka (plansza,):
        for key , value in plansza.items():
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

def ruchypl(plansza,tura):
    if tura % 2 == 0 :
        print("\n tura gracza który gra O")
    elif tura % 2 != 0 :
        print("\n tura gracza który gra X")
    pole = input("podaj pole na jakim hcesz postawić znak ")
    for abc in lsabc :
        for l123 in ls123 :
            if abc + l123 == pole:
                if plansza[abc + l123] != 0 :
                    print("skąd wziołeś to pole, tracisz ruch")
                    break
                if tura % 2 == 0 :
                    plansza[abc + l123] = 2
                elif tura % 2 != 0 :
                    plansza[abc + l123] = 1
                  
def wynix2(plansza, mozzwy):
    wynik = []
    if tura % 2 == 0 :
        jeddwa = 2
    else :
        jeddwa = 1
    for key, value in plansza.items() :
        if value == jeddwa :
            wynik.append(key)
    for listyzwy in mozzwy :
        wynik2 = []
        for zakre in wynik :
            if zakre in  listyzwy :
                wynik2.append(zakre)
         
        if wynik2 == listyzwy :
            if tura % 2 == 0:
                plansza["zwycięstwo"] = 6
            else :
                plansza["zwycięstwo"] = 6
        zera = []
        for key , value in plansza.items() :
            if key != "zwycięstwo" :
                if value == 0 :
                    zera.append(1)
                else :
                    pass
        if len(zera) > 0 :
            pass
        else :
            plansza["zwycięstwo"] = 7

printkolka(plansza)
while tura > 0:
    ruchypl(plansza,tura)
    printkolka(plansza)
    wynix2(plansza, mozzwy)
    if plansza["zwycięstwo"] == 6:
        print(f" \n wygrał gracz który grał {lsosub[tura % 2]}")
        break
    elif plansza["zwycięstwo"] == 7 :
        print("\n nikt nie wygrał")
        break
    tura +=1