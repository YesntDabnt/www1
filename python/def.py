

from ast import IfExp, Num
from random import randint


#code 1
def thething () :
    print("I want the thing!")

Num = 3
for x in range(Num):
    thething()

#code 2
#t = [1,2,3,4,5,6,7,8,9,10]
#x = t[randint(0,9)]
#y = t[randint(0,9)]
#z = x - y 
#c = y - x

tal1 = input("Ange tal1 : \n")
tal1 = int(tal1)
tal2 = input("Ange tal2 : \n")
tal2 = int(tal2)
tal3 = input("Ange tal1 igen \n")
tal3 = int(tal3)
tal4 = input("Ange tal2 igen : \n")
tal4 = int(tal4)


def maths(text,text2, text3, text4 ):
    if tal1 > 5 :
        print(tal3-tal4)
    elif tal1 < 5 :
        print(tal1-tal2) 
    else :
        if tal1 < 5 :
            print(tal2-tal1)



maths(tal1, tal2, tal3, tal4)





