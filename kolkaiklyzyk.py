
kolka = {
    'a1' : 1,
    'a2' : 0,
    'a3' : 2,
    'b1' : 2,
    'b2' : 1,
    'b3' : 1,
    'c1' : 0,
    'c2' : 2,
    'c3' : 1,
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
        

        


printkolka(kolka)
print()






