def exponent(base, exp):
    x=pow(base,exp)
    return x
base=int(input("Enter base: "))
exp=int(input("Enter exponent: "))
y=exponent(base, exp)
print(base,"raises to the power of",exp,":",y)