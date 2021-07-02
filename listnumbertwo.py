tophat = ["chocolate", "rice", "pizza", "macandcheese", "popcorn", "seeweed", "apples", "pizza", "zucchini",]

mouse = ["black", "blue", "purple", "red"]

numbers = [1, 2, 3, 4, 5, 6, 7,]

states = ["wa", "ca", "or"]

countries = ["us", "england", "france", "singapore"]

words = [mouse, "stuff", 78.9, "what", "okay"]

empty = []

nano = [0]

def get_number_of_elements(lst):
    return len(lst)

# fix
def get_last_element(lst):
    index = len(lst) - 1
    return lst[index]

def get_first_element(lst):
    if len(lst) == 0:
        return None
    return lst[0]

for list_name in ("words", "empty"):
    lst = globals()[list_name] # dont mind this
    print(list_name, " [count] ->", get_number_of_elements(lst))
    print(list_name, " [first] ->", get_first_element(lst))
    print(list_name, " [last]  ->", get_last_element(lst))
    print("--------------")    
