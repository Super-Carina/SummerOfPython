water = ["kyle", 23, "violet", 15, "bella", 19]

#print(water) 

name = input("please enter a name:")

print("you typed : ", name)

if name == "kyle":
    print("kyle's age:", water[1])

elif name == "violet":
    print("violet's age:", water[3])

elif name == "bella":
    print("bella's age:", water[5])

else:
    print("i don't know this age yo!")