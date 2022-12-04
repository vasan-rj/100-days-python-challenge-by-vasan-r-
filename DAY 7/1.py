#randomly choose the word
#  take a character input,
#  print right if the character is matches with random word
#  print wrong if the character does not  matches with random word
import random
word_list=['ardvark','baboon','camel']
rand_word=random.choice(word_list)
x=input("enter a character: ")
x=x.lower()
print(f'the random word is {rand_word}')
for w in rand_word:
    if x==w:
        print("right")
    else:
        print("wrong")
           