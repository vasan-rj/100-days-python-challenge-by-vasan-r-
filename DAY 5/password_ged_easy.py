#by using strings

import random
letters=['a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
, 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
, 'w', 'x', 'y', 'z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['*','/','@','#','$','%','_']

n_letters=int(input("enter the numbers of letters: "))

n_numbers=int(input("enter the numbers of numbers: "))

n_symbols=int(input("enter the numbers of symbols: "))

x=""
for i in range(0,n_letters):
    l=random.randint(0,22)
    x=x+(letters[l])

for i in range(0,n_numbers):
    n=random.randint(0,9)
    x=x+(numbers[n])

for i in range(0,n_symbols):
    s=random.randint(0,6)
    x=x+(symbols[s]) 
print(x)
# y=(random.shuffle(x))
# print(y)


      