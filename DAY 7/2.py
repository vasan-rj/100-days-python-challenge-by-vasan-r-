#sample i/o
#random word=banana
#word=_ _ _ _ _ _
#entered character='a'
#word=_ a _ a _ a 
stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / /
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
life=6

import random

word_list=["absence","abuse","account","accident","beneath","bend","benefit",
          "biology","bitter","candidate","campaign","camera","capacity","capture",
          "deaf","daughter","deal","decorate","dialogue","economy","finance","educate",
          "efficient","supportive","elderly","flight","folk","flame","frustration","garbage",
          "gather","gentle","global","hilarious","intelligence","jazz","knife","longevity",
          "momument","nonsense","nobody","turmeric","utilize","sashimi","reconfigure","wheat",
          "yellowish","zone"]
rand_word=random.choice(word_list).lower()

empty_list=[]

for w in range(len(rand_word)):
    empty_list+="_" 

print(empty_list) 

end_of_game=False

while not end_of_game:
    x=input("enter a letter: ").lower()
   

    for k in range(len(rand_word)):
        if x==rand_word[k]:
            empty_list[k]=x


    if x not in rand_word:
        life=life-1
        if life==0:
            print("you lost!!")
            end_of_game=True
        else:
            print(f'you have {life} lifes left!!')    

    print(empty_list)
    if "_" not in empty_list:
        end_of_game=True
        print("you win")
    
    print(stages[life])
