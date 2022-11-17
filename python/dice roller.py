import random


x = "y"

while x == "y":
	
	dab = random.randint(1,6)
	
	if dab == 1:
		print("[-----]")
		print("[     ]")
		print("[  0  ]")
		print("[     ]")
		print("[-----] \n 1")

	if dab == 2:
		print("[-----]")
		print("[  0  ]")
		print("[     ]")
		print("[  0  ]")
		print("[-----] \n 2")

	if dab == 3:
		print("[-----]")
		print("[     ]")
		print("[0 0 0]")
		print("[     ]")
		print("[-----] \n 3")

	if dab == 4:
		print("[-----]")
		print("[ 0 0 ]")
		print("[     ]")
		print("[ 0 0 ]")
		print("[-----] \n 4")

	if dab == 5:
		print("[-----]")
		print("[ 0 0 ]")
		print("[  0  ]")
		print("[ 0 0 ]")
		print("[-----] \n 5")

	if dab == 6:
		print("[-----]")
		print("[0 0 0]")
		print("[     ]")
		print("[0 0 0]")
		print("[-----] \n 6")
		
	x=input("press y to roll again and n to exit: " )
	print("\n")
