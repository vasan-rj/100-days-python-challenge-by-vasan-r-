#sum of element in a list
def sum_list(list1):
    k=0
    for i in range(len(list1)):
        k=k+list1[i]
    print(f'the sum the list {list1} is : {k}')    

list1=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    list1.append(int(input(f'enter element {i+1}: ')))
sum_list(list1)