import os,math
os.system("cls")

def func(lst: list):
    return math.ceil(lst)
lst = [12.4,23,5.2,23.6,1.2,3.5]
lst = list(map(func,lst))
print(lst)