n=int(input("enter the num"))
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+r**2
        x=x//10
    x=sum
if x==1:
    print(n,"is a happy num")
else:
    print(n,"is not a happy num")