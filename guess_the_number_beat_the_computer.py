print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")

min = 0
max = 1000

for i in range(10):
    guess = int((max-min) / 2) + min
    print("Zgaduję:", guess)
    ans = input("")
    if ans == "za malo":
        min = guess
    elif ans == "za duzo":
        max = guess
    elif ans == "zgadles":
        print("Wygrałem!")
        break
