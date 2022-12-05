#finding max and min element in a list 
def find_max(list1):
    max=0
    for i in list1:
        if i>max:
            max=i
    print(f'the max element is the list {list1} is: {max}')

def find_min(list1):
    min=0
    for i in list1:
        if i<min:
            min=i
    print(f'the min element is the list {list1} is: {min}')

list1=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    list1.append(int(input(f'enter element {i+1}: ')))

find_max(list1)     
find_min(list1)     
