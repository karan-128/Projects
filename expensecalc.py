exp = -1
total = 0
maxexp = 0
minexp=1000
while exp!=0:
    exp = int(input("What is the expense? (Type 0 to Stop):"))
    total+=exp
    if exp>maxexp:
        maxexp=exp
    if exp<minexp:
        minexp=exp
print(f"Your Total Expenditure is Rs.{total}")
print(f"The maximum you spent is Rs.{maxexp} while the minimum you spent is Rs.{minexp}")