sum=0
n=int(input("enter the num"))
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("the sum of the digits of the num is",sum)




# sum=0
# n=input("enter the num")
# for i in n:
#     sum=sum+int(i)
#     print("the sum of the digits of the num is",sum)