# indentation

# print("Hello World!")

# semicolon -> semocolons are optionl in python. you can write multiple statesments one one line by sepearating them with ; but this is rarely used because it makes it hard to read/

# print("hello");print("word");print("i'll learning a python")

# count the number

# n = 5873
# num = n
# count = 0

# while num > 0:
#     num = num // 10
#     count += 1

# print("Total number of digits:", num)

# Reverse the number

n = 1234
num = n
rev = 0

while num > 0:
    last_digit = num % 10
    rev = rev * 10 + last_digit
    num = num // 10

print("Reverse:", rev)
