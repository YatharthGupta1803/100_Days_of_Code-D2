#Tip Calculator Day 2

print("Welcome to the Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much TIP would you like to give? 10% | 12% | 15% "))
split=int(input("How many people to split the bill"))
if tip==10:
    tb=0.1*bill
if tip==12:
    tb=0.12*bill
if tip==15:
    tb=0.15*bill
final=int((tb+bill)/split)
print("Each person should pay $",final)


