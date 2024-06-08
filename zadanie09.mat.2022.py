import random
def stworz_plansze(n,m):

    # n - liczba wierszy
    # m - liczba kolumn

    tabliczka = [['*']*m for i in range (n)]

    tabliczka[n-1][m-1] = None

    return tabliczka

def narysuj_plansze(tabliczka):

    pierwszy_wiersz = [i for i in range (len(tabliczka[0]))]

    print("  ", end="")

    for i in range (len(pierwszy_wiersz)):
        print(f"{pierwszy_wiersz[i]}", end=" ")
    print(" ")

    for i in range (len(tabliczka)): #6 #przechodzimy po tablicy wiersz po wierszu
        print(f"{i}", end = " ") #wyswietlamy numer wiersza
        for j in range (len(tabliczka[0])): #5 #przechodzimy po kolejnych elementach kazdego wiersza
            if tabliczka[i][j] == "*":
                print("*", end=" ")
            else:
                print (" ", end=" ")
        print("")

def czy_ruch_poprawny(wiersz, kolumna,tabliczka):

    if wiersz > len(tabliczka) or kolumna > len(tabliczka[0]):
        print("Błędne dane!")
        return False

    for i in range(len(tabliczka)): #przechodzimy po wierszach
        for j in range (len(tabliczka[0])): #przechodzimy po kolumnach
            if tabliczka[i][j]== None:
                if wiersz>=i and kolumna>=j:
                    print("Błędne dane!")
                    return False
                    break
            else:
                continue
    return True

def wykonaj_ruch(wiersz,kolumna,tabliczka):

    for i in range (wiersz,len(tabliczka)): #przechodzimy po wierszach
        for j in range (kolumna,len(tabliczka[0])): #przechodzimy po kolumnach
            tabliczka[i][j] = None

def main ():

    n = int(input("Podaj liczbe wierszy \n"))
    m = int(input("Podaj liczbe kolumn \n"))

    liczba_ludzkich = int(input("Podaj liczbe graczy ludzkich"))
    liczba_ai = 2-liczba_ludzkich

    tabliczka = stworz_plansze(n,m)

    narysuj_plansze(tabliczka)

    wiersz = n
    kolumna = m

    gracz = 1

    while True:
        if gracz == 1:
            print("Ruch gracza 1")
            gracz+=1
        else:
            print("Ruch gracza 2")
            gracz-=1

        while True:

            if liczba_ludzkich==2 or (liczba_ludzkich==1 and gracz == 2):
                wiersz = int(input("Podaj wiersz: \n"))
                kolumna = int(input("Podaj kolumne: \n"))
                if czy_ruch_poprawny(wiersz,kolumna,tabliczka) == True:
                    break
            elif liczba_ai==2 or (liczba_ludzkich==1 and gracz==1):
                wiersz = int(len(tabliczka))
                wiersz_ai = random.randint(0,wiersz)

                kolumna = int(len(tabliczka[0]))
                kolumna_ai = random.randint(0,kolumna)

                if czy_ruch_poprawny(wiersz, kolumna, tabliczka) == True:
                    print(f"Podaj wiersz:\n {wiersz_ai}")
                    print(f"Podaj kolumne: \n {kolumna_ai}")
                    break

        wykonaj_ruch(wiersz,kolumna,tabliczka)
        narysuj_plansze(tabliczka)

        if wiersz == 0 and kolumna == 0:
            print(f"Koniec gry, wygral gracz {gracz}!")
            break

if __name__=="__main__":
    main()