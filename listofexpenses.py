exp = []
stopped = False

while not stopped:
    e = int(input("What is the expense? (Type 0 to Stop): "))
    if e!=0:
        exp.append(e)
    else:
        stopped = True
print(f"List of Expenses: {exp}")
print(f"Total value: Rs.{sum(exp)}")