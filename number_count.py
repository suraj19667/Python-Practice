from math import *

num = int(input("Enter a number: "))
def number_count(num):
    return int (log10(num))+1
print("Number of digits in", num, "is", number_count(num))