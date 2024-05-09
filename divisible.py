list=[]
n=int(input("enter no. of elements: "))
print("Enter elements:")
for i in range (0,n):
    element=int(input())
    list.append(element)
print("Given list is ",list, end="")
print()
print("Divisible by 5")
for i in range(0,n):
    if(list[i]%5==0):
        print(list[i])