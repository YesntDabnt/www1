money = input("How rich are you \n")
money = int(money)

if money > 100: 
    print(money-30, "No you not :P \n")
elif money > 90:
    print(money-15, "No you not :P \n")
multi = input("Again?")
multi = int(multi)
if money <=90:
    print(money*multi)
 