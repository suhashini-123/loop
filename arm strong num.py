num=int(input("enter the num"))
sum=0
original=num
while num>0:
    digit =num%10
    sum=sum+digit**3
    num=num//10
if sum==original:
    print("arm strong num")
else:
    print("not a arm strong num")
    