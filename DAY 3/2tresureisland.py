direction=input("enter left or right? : ")
if direction=="left":
    x=input("swiw or wait? : ")
    if x=="swim":
        print("game over")
    else:
        door=input("enter which door?: red/ green/ black : ")
        if door=="red":
            print("you won")
        elif door=="green":
            print("you lost")
        else:
            print("you lost")       

elif direction=="right":
    print("game over")
    
else:
    print("incorrect choice")  
