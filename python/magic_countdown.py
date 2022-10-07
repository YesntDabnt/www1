import os

print( ("*THE TRICK IS NOT PLEASANT* *USE AT OWN RISK* \n"), 
"Enter Number of Seconds until the magic trick: ")
sec = int(input())

strOne = "shutdown /s /t "
strTwo = str(sec)
str = strOne+strTwo

os.system(str)