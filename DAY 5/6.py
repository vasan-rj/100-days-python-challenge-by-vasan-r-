# 3,6,9...=fizz
# 5,10,15...=buzz
#15,30,45,...=fizzbuzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)            