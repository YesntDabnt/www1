import os

print( ("Funny thing \n"), 
"Enter Number of Seconds until the magic trick: ")
sec = int(input())

strOne = "shutdown /r /t "
strTwo = str(sec)
str = strOne+strTwo

os.system(str)


