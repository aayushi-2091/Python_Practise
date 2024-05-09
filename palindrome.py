n=int(input("Enter a number: "))
print("orignal number ",n)
x=n
s=0
while n>0:
    p=n%10
    s=(s*10)+p
    n=n//10
n=x
if n==s:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")