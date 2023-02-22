# a=1234
# b=str(a)
# i=0
# while a<len(a):
#     print(b[i]**2,end=" ")
#     i=i+1
# n=int(input("enter the num"))
# i=0
# while n>0:
#     r=n%10
#     i=i*10+r
#     n=n//10
# k=i
# while k>0:
#     m=k%10
#     n=m**2
#     k=k//10
#     print(n,end="")   


# a=int(input("enter the num"))
# b=int(input("enter the num")) 
# sum=a+b
# print(sum)
# rev=0
# while sum>0:
#     r=sum%10
#     rev=rev*10+r
#     sum=sum//10
# print(rev)


# i=1
# k=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(k%2,end=" ")
#         k=k+1
#         j=j+1
#     i=i+1
#     print( )
            
i=1
while i<=5:
    j=1
    while j<=i:
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
        j=j+1
    i=i+1
    print()                       