import random
x=input("enter people names: ")
y=x.split(",")
# print(len(y))
print(f'{y[random.randint(0,len(y)-1)]} is the person who wants to pay the bill')
