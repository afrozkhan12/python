# Formula Core = (P R T)
# SimpleInterest = (PxRxT) / 100
# CompoundInterest = P x ( 1 + rate / 100 ) ** time

Principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Interest rate (annual, %): "))
time = float(input("Enter Time in Years: "))

simple_interest = (Principal * rate * time )/ 100
compound_interest = Principal * (1 + rate / 100) ** time
print('')

print(simple_interest,"Simple Interest")
print('')
print(compound_interest, "Compound Interest")

print('')