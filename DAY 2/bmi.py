#bmi claculator
#bmi =weight(in kg)/height^2(m^2)
choice=1
while choice==1:
    weight=float(input("enter your weight (in kg): "))
    height=float(input("enter your height (in m): "))
    
    bmi=weight/(height**2)
    if bmi<18.5:
        print("you are underweight")
    elif 18.5<bmi<25:
        print("you are normal weight")  
    elif 25<bmi<30:
        print("your are over weight ")

    elif bmi>30:
        print("you are obese!!")
    choice=int(input("enter 1 for bmi and 2 for break: "))

