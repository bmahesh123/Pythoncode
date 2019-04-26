from datetime import date

# FD=int(input("Enter first date:"))
# LD=int(input("Enter second date:"))

f_date = date(2019, 4, 10)
l_date = date(2019, 4, 20)

delta = l_date - f_date

# print(delta)
# print(type(delta))
print(delta.days)
