print("Welcome to the tip calculator!😄")
total=float(input("What is the total bill?\n₹"))
tip=int(input("What percentage of tip would you like to give? 10%, 12%, or 15%?\n"))
person=int(input("How many people to split the bill?\n"))
per=tip/100
amount=total*per
total=total+amount
ans=round(total/person,2)
print(f"Each person should pay: ₹{ans} ")
