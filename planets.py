def mercury(w):
    return w * 0.1

def earth(weight_on_earth):
    return weight_on_earth * 1

def venus(weight_on_earth):
    return weight_on_earth * 0.91

planet = input("""
Choose a planet to find your weight: 
  1) Mercury
  2) Venus

""")

earth = input("Now enter your weight on Earth: ")

if planet == "1":
    print(mercury)

#
# your weight on:
# 1) mercury
# 2) venus
#  ....

# enter your weight>
# your weight on "mercury" is 3094820

