# 1.and 2.or 3.and
name1=input("enter your name")
name2=input("enter your crush name")
name1_l=name1.lower()
name2_l=name2.lower()
y=name1_l+name2_l

t=y.count("t")
r=y.count("r")
u=y.count("u")
e=y.count("e")

true=t+r+u+e

l=y.count("l")
o=y.count("o")
v=y.count("v")
love=l+o+v

result=str(true)+str(love)+"%"
print(result)
