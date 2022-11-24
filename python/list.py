from copy import error
from re import I
import os


a = [0,1,2,3,4,5]




def main1(text) :
    print("\n1. lägg till sak i listan")
    print("2. ta bort första saken i listan")
    print("3. se listan")
    print("4. redigera sak i listan")
    print("5. ta bort specifik sak i listan")
    print("6. byt ordning på saker i listan")
    print("7. avsluta programmet")
    val = int(input("vilket val?\n"))
    

    if val == 1 :
        print(a)
        a.append(input(""))
        print(a)
    elif val == 2 :
        print(a)
        a.pop(0)
        print(a)
    elif val == 3 :
        print(a)
    elif val == 4 :
        print(a)
        b = int(input("Välj element att redigera \n"))
        c = int(input("Ny värde : \n"))
        a.insert(b,c)
        print(a)
    elif val == 5 :
        print(a)
        b = int(input("Välj element att ta bort \n"))
        a.remove(b)
        print(a)
    elif val == 6 :
        print(a)
        print("Välj två element att byta plats på ")
        b = int(input("Välj element 1 : \n"))
        c = int(input("Välj element 2 : \n"))
        a[b],a[c] = a[c],a[b]
        print(a)
    elif val == 7 :
        print("Bye Bye")
        os._exit(1)
    elif val > 7 :
        print("Fel tal, try again")
    


        



main1(1) 

