code = input("Please enter customer code: ")  # D, W, B
rentPeriod = int(input("Please enter number: "))
rentStart = int(input("Enter odometer reading  at the start: "))
rentEnd = int(input("Enter odometer reading  at the end: "))
milesDriven = int(rentEnd - rentStart)
budgetDaily = 40
mileDaily = 0.25
mileWeek = 1.90
cost1 = 40*rentPeriod + 0.25 * milesDriven
# budget
# if more than 100 miles driven
cost3 = 390*rentPeriod + 0.25 * milesDriven
# if more than 1500 miles per week

if code == "B":
    print("Your budget cost is:", cost1, "$")

if code == "D":
    extra = milesDriven - 100*rentPeriod
    if extra > 0:
        cost2 = extra * 0.25 + 60 * rentPeriod
    else:
        cost2 = 60 * rentPeriod
    print("Your daily cost for more than 100 miles driven is: ", cost2, "$")

if code == "W" and milesDriven < 900:
    print("For less than 900 miles your weekly cost is: ", 190*rentPeriod, "$")
if code == "W" and 900 < milesDriven < 1500:
    print("For miles between 900 and 1500 your weekly cost is: ", 290*rentPeriod, "$")
if code == "W" and milesDriven > 1500:
    print("For more than 1500 miles driven your weekly cost is: ", cost3, "$")
