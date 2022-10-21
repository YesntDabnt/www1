# 1
import time

r = 60
def countdown(t) :

    while t > 0:

        mins, secs = divmod(t, 60)

        timer = '{:02d}:{:02d}'.format(mins, secs)

        print(timer, end="\r")

        time.sleep(1)

        t -= 1
        
    if t == 00:00

    print('And nothing happened...')


s = input("Enter the seconds: ")


countdown(int(s))

# 2
answer = input("")
first = answer[:1]
first_two = answer[:2]
def shyperson(shy) :
    print(first, "..." , first_two, ".." , answer)


shyperson(answer)

# 3
from msilib.schema import AppSearch


damage = input("Enter damage : \n")
damage = int(damage)
time = input("Enter time in seconds : \n")
time = int(time)
aps = input("Enter attacks per sec : \n")
aps = int(aps)
dps = damage * time * aps
dps = int(dps)
def attack(god) :
    print(dps)

attack(dps)

# 4
from tkinter import Y

x = str(input("Enter first number : \n"))
x = int(x)
y = str(input("Enter second number : \n"))
y = int(y)

sum = str( x + y )

print(sum)



