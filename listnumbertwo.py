tophat = ["chocolate", "rice", "pizza", "macandcheese", "popcorn", "seeweed", "apples", "pizza", "zucchini",]

mouse = ["black", "blue", "purple", "red"]

numbers = [1, 2, 3, 4, 5, 6, 7,]

states = ["wa", "ca", "or"]

countries = ["us", "england", "france", "singapore"]

# homework 1
# print the last element of tophat using only len.
# test it with an empty list []
#
#


# for tomorrow, 7/1 write this function

def get_number_of_elements(lst):
    pass

def get_last_element(lst):
    return lst[9]

def get_first_element(lst):
    return lst[0]

for list_name in ("tophat", "mouse", "numbers", "states", "countries"):
    l = globals()[list_name]
    #print(list_name, "->", get_last_element(l))
    #print(list_name, "->", get_first_element(l))

