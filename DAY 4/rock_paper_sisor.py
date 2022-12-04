import random
user_choice=int(input("type 0(rock) 1(paper) 2(sissor)"))
comp_choice=random.randint(0,2)
print(f"computer choice is {comp_choice}")
if comp_choice==user_choice:
    print(" DRAW!! ")
elif user_choice==2 and comp_choice==0:
        print("YOU loose!!!")    
elif user_choice==0 and comp_choice==2:
        print("YOU won!!!")
elif comp_choice>user_choice:
    print("you lost!!")
elif user_choice>comp_choice and user_choice<3:
    print("you won!!")           

else:
    print("invalid input!!!")

