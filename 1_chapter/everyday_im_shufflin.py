import random

def shuffle_list(lst: list):
    for i in range(len(lst)):
        random_swap = random.randint(0, len(lst) - 1)
        lst[i], lst[random_swap] = lst[random_swap], lst[i]

my_lst = [1, 2, 3, 4, 5, 6, 7,  8]

shuffle_list(my_lst)
print(my_lst)