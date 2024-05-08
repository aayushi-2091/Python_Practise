str=input("Enter a word")
l=len(str)
n=int(input("Enter upto which position you want to remove character: "))
for i in range((n+1),l):
    print(str[i],end="")