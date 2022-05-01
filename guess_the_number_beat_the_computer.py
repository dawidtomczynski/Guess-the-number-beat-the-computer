print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")

min_num = 0
max_num = 1000
ans = ""
ans_list = []
while not ans == "zgadłeś":
    while not len(ans_list) == 10:
        guess = int((max_num-min_num) / 2) + min_num
        print("Zgaduję:", guess)
        ans = input("")
        if ans == "za mało":
            min = guess
            ans_list.append(ans)
        elif ans == "za dużo":
            max = guess
            ans_list.append(ans)
        elif ans == "zgadłeś":
            print("Wygrałem!")
            break
        else:
            print("Podaj: za mało, za dużo lub zgadłeś.")
    else:
        print("Nie oszukuj!")
        break
