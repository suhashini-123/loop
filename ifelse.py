# a=int(input("enter the number"))
# b=int(input("enter the numbet"))
# c=input("enter the operator")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# else:
#     print("wrong")

# print("well come to sbi")
# print("insert your card")
# language=input("enter the language")
# current_balance=2500
# if language=="english":
#     password=int(input("enter the pin"))
#     pin=1234
#     if pin==password:
#         menu=input("enter the menu")
#         if menu=="current":
#             if current_balance>0:
#                 print(current_balance)
#             else:
#                 print("zero amount")
#         elif menu=="withdraw":
#             withdraw_amount=int(input("enter the amount"))
#             if withdraw_amount<=current_balance:
#                 print(current_balance-withdraw_amount)
#             else:
#                 print("in sufficient")
#         elif menu=="deposit":
#             deposit_amount=int(input("enter the menu"))
#             if deposit_amount>0:
#                 print(current_balance+deposit_amount)
#             else:
#                 print("current_balance")
#         else:
#             print("enter correct menu")
#     else:
#         print("enter the correct password")
# else:
#     print("enter the correct language")
                
                
# expected_date=int(input("enter the expected-date"))
# expected_month=int(input("enter the expected_month"))
# expected_year=int(input("enter the expected_year"))
# return_date=int(input("enter the return_date"))
# return_month=int(input("enter the return_month"))
# return_year=int(input("enter the return_year"))
# if return_date<expected_date and return_month==expected_month and return_year==expected_date:
#     print("no fine")
# if return_date>expected_date and return_month==expected_month and return_year==expected_year:
#     print((return_date-expected_date)*15)
# elif return_date>expected_date and return_month>expected_month and return_year==expected_year:
#     print((return_date-expected_date)*15)+((return_month-expected_month)*500)
# elif return_year-expected_year:
#     print("fixed fine 10000")
# else:
#     print("non")