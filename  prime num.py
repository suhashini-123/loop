count=0
n=int(input("enter the num"))
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime num")
else:
    print("not a prime num")





        