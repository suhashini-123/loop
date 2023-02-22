# i=1
# while i<=5:
#     j=1
    # while j<=i:
    #     if i%2==0:
    #         print(i)
    #         print(i,i*"*")
    #     j=j+1
    # i=i+1
# #     # print()            
# n=int(input("enter the num"))                    
# i=1
# sum=0
# while i<=n:
#     rem=n%10
#     sum=sum+rem
#     n=n//10
#     n=sum
# if sum%2==0:
#     print("yes")
# else:
#     print("no")        
    
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i*j,end=" ")
#         j=j+1
#     i=i+1
#     print() 

# i=89
# p=(89)
# while i>=65:
#     j=65
#     while j<=i:
#         print(chr(p),end="")
#         j=j+1
#     i=i+1
#     print()


# n=int(input("enter the num"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     i=i+1
#     print() 

# n=int(input("enter the num"))
# k=84+1
# i=1
# while i<=n:
#     j=1
    # while j<=n:
    #     print(chr(k),end=" ")
    #     j=j+1
    #     k=k+1
    # k=k-10
    # i=i+1
    # print() 
    
# n=int(input("enter the num"))
# s=n
# sum=0
# i=1
# while i<=n:
#     rem=n%10
#     sum=sum+rem
#     n=n//10
#     k=sum*sum
# if s==k:
#     print("character")
# else:
#     print("not charecter")        
             
               
# n=int(input("enter the num"))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count=count+i
#     i=i+1 
# if count%2==0:
#     print("true")
# else:
#     print("false")

# year=int(input("enter the year"))
# month=int(input("enter the month"))
# date=int(input("enter the date"))
# hour=int(input("enter the hour"))
# min=int(input("enter the min"))
# sec=int(input("enter the sec"))
# if month>=1 and month<=12:
#     if date>=1 and date<=31:
#         if hour>=1 and hour<=24:
#             if min>=1 and min<=60:
#                 if sec>=1 and sec<=60:
#                     print(year,"-",month,"-",date,"-",hour,"-",min,"-",sec)
#                 else:
#                         print("you missed sec")
#             else:
#                 print("you missed min") 
#         else:
#             print("you missed hour") 
#     else:
#         print("you missed date")  
# else:
    # print("enter valid numbe")
    
    
    
    
date=int(input("enter the date"))
month=int(input("enter the month"))
year=int(input("enter the year"))
if month==4 or month==6 or month==9 or month==11:
    if date<30:
        print(date+1,month,year)
    else:
        print("1", month+1,year)
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
    if date<31:
        print(date+1,month,year)
    else:
        print("1",month+1,year)
elif month==12:
    if date<31:
        print(date+1,month,year)
    else:
        print("1","1",year+1)
elif year%4==0:
    if month==2:
        if date<29:
            print(date+1,month,year)
        else:
            print("1",month+1,year)
elif year%4!=0:
    if month==2:
        if date<28:
            print(date+1,month,year)
        else:
            print("1",month+1,year)
    else:
        print("enter valid data")
    
                        














 

       
           
    
    
    
           
            
        
    
    
                            
           