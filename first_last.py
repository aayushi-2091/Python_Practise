list=[]
n=int(input("enter no. of elements: "))
print("Enter elements:")
for i in range (0,n):
    element=int(input())
    list.append(element)
print("Given list: ",list, end="")
print()
if(list[0]==list[n-1]):
    print ("result is True")
else:
    print ("result is False")