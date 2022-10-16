import random
ask = input("Do you want to roll the dice y or n? ")
while ask != "y" :
    ask = input("Do you want to roll the dice y or n? ")
no = random.randint(1,6)

if no == 1 : 
    print("[-------]")
    print("[       ]")
    print("[   O   ]")
    print("[       ]")
    print("[-------]")
elif no == 2 : 
    print("[-------]")
    print("[ O     ]")
    print("[       ]")
    print("[     O ]")
    print("[-------]")
elif no == 3 : 
    print("[-------]")
    print("[ O     ]")
    print("[   O   ]")
    print("[     O ]")
    print("[-------]")
elif no == 4 : 
    print("[-------]")
    print("[ O   O ]")
    print("[       ]")
    print("[ O   O ]")
    print("[-------]")
elif no == 5 : 
    print("[-------]")
    print("[ O   O ]")
    print("[   O   ]")
    print("[ O   O ]")
    print("[-------]")
elif no == 6 : 
    print("[-------]")
    print("[ O O O ]")
    print("[       ]")
    print("[ O O O ]")
    print("[-------]")