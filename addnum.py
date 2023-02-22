# year=int(input("enter the year"))
# month=int(input("enter the month"))
# date=int(input("enter the day"))
# if year>0:
#     if month<12:
#         if date<31:
#             print(year,"-",month,"-",date)
#         else:
#             print(year,"-",month,"-",date+1)
#     else:
#         print(year+1,"-","1","-","1")
# else:
# 	print(year+1,"-","1","-","1")
# a="Kavitha"
# b=[]
# i=0
# while i<len(a):
#     if i%2!=0:
#         c=c+a[i]
#     else:
#         b=+a[i]
#     i=i+1
# print(b,c)

# a=["Kavitha"]
# b=" "
# c=" "
# i=0
# while i<len(a):
#     if i%2!=0:
#         c=c+a[i]
#     else:
#         b=b+a[i]
#     i=i+1
# print(b,c)
# i=0
# while i<len(a):
#     if i%2!=0:
#         b=b+a[i]
#     else:
#         c=c+a[i]
# #     i=i+1
# # print(b,c)
        
    
# a="Kavitha"
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i].isupper():
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b,c)

# a="kavitha"
# b=[]
# i=0
# while i<len(a):
# #     r=a[i]*5
# #     b.append(r)
# #     i=i+1
# # print(b)
    
    
# a=[1,3,4,2,3,2,4,5,7,6]
# mean=0
# meadian=0
# # sum=0
# # i=0
# # while i<len(a):
# #     sum=sum+a[i]
# #     mean=sum/10
# #     median=len(a)+2//2
# #     i=i+1
# # print(mean,"median:",median)
# a=int(input("enter number"))
# b=int(input("enter"))
    
a=int(input("enter the num"))
i=0
while i<a:
    # l=a%100000
    tens=a%10000
    ones=a%1000
    # t=a%10
    h=a%100
    t=a%10
    i=i+1
print(tens-ones,"+",ones-h,"+",h-t,"+",t)


