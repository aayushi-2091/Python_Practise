print("Printing current and previous number sum in a range of 1 to 10")
for i in range(0,10):
    if i==0:
        current=i
        previous=0
    else:
        current=i
        previous=i-1
    sum= current+previous
    print("Current Number ",current," Previous Number ",previous," Sum: ",sum)