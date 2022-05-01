print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")

min = 0
max = 1000
ans = ""
while not ans == "zgadłeś":
    # for i in range(10):
        guess = int((max-min) / 2) + min
        print("Zgaduję:", guess)
        ans = input("")
        if ans == "za":
            min = guess
        elif ans == "za dużo":
            max = guess
        elif ans == "zgadłeś":
            print("Wygrałem!")
            break
        else:
            print("Podaj: za mało, za dużo lub zgadłeś.")
    # else:
    #     print("Nie oszukuj!")
