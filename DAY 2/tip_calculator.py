amount=float(input("enter your total bill amount:"))
tip_percent=float(input("enter the tip percent(%):"))
if tip_percent<100:
    total_amount=amount*(1+(tip_percent/100))
    print(f'your tip amount is:{tip_percent}')
    print(f'your total amount is:{int(total_amount)}')
else:
    print("invalid tip percent!!!")    