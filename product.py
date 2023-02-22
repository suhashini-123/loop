

n=int(input("enter the num"))
pro=1
while n>0:
    pro=pro*(n%10)
    n=n//10
print("product of digits are",pro)


# n=int(input("enter the num"))
# rev=0
# while n>0:
#     rem=n%10
#     rev+rev*10+rem
#     n=n//10
# print(rev)    