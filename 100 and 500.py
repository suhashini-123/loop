i=int(input("enter the num"))
j=int(input("enter the num"))
a=0
sum=0
while i<=j:
    if i%2==0:
        a=a+i
    else:
        sum=sum+i
    i=i+1
print(a)
print(sum)