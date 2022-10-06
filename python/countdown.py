
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


t = input("Enter the minutes: ")
s = input("Enter the seconds: ")


countdown(int(t)*int(r)+int(s))