plansza = {
    'a1' : 0, 'a2' : 0, 'a3' : 0,
    'b1' : 0, 'b2' : 0, 'b3' : 0,
    'c1' : 0, 'c2' : 0, 'c3' : 0,
    "zwycięstwo" : 5,
}
lsabc = ['a', 'b', 'c',]
ls123 = ['1', '2', '3']
zajete = [1, 2]
lsosub = ["O", "X"]
tura = 1
n = 2

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
        print("tura gracza który gra O")
    elif tura % 2 != 0 :
        print("tura gracza który gra X")
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
                  
def wynix(plansza):
    for i in zajete :
        if plansza["a1"] == i and plansza["a2"] == i and plansza["a3"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["a1"] == i and plansza["b1"] == i and plansza["c1"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["a1"] == i and plansza["b2"] == i and plansza["c3"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["a2"] == i and plansza["b2"] == i and plansza["c2"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["b1"] == i and plansza["b2"] == i and plansza["b3"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["c1"] == i and plansza["c2"] == i and plansza["c3"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["a3"] == i and plansza["b3"] == i and plansza["c3"] == i :
            plansza["zwycięstwo"] = 6
            break
        elif plansza["a3"] == i and plansza["b2"] == i and plansza["c1"] == i :
            plansza["zwycięstwo"] = 6
            break
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
    wynix(plansza)
    if plansza["zwycięstwo"] == 6:
        print(f"wygrał gracz który grał {lsosub[tura % 2]}")
        break
    elif plansza["zwycięstwo"] == 7 :
        print("nikt nie wygrał")
        break
    tura +=1