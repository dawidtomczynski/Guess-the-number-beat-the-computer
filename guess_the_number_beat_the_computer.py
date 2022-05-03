print("Think about the number from 0 to 1000 and I will guess it in maximum of ten tries.")

min_num = 0
max_num = 1000
ans = ""
ans_list = []
while not ans == "you won":
    while not len(ans_list) == 10:
        guess = int((max_num-min_num) / 2) + min_num
        print("My guess:", guess)
        ans = input("")
        if ans == "too small":
            min_num = guess
            ans_list.append(ans)
        elif ans == "too big":
            max_num = guess
            ans_list.append(ans)
        elif ans == "you won":
            print("I won!")
            break
        else:
            print("Type: too small, too big, you win.")
    else:
        print("Don't cheat")
        break
