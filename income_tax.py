n=int(input("Enter income: "))
tax=0
if n<=10000:
    tax=0
elif n<=20000:
    x=n-10000
    tax=x*10/100
else:
    tax=0
    tax=10000*10/100
    tax=tax+(n-20000)*20/100
print("Total tax: ",tax)