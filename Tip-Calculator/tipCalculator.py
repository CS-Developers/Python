# Basic Printing Function
print("Welcome to the tip calculator.")

totalBill = input("What was the total bill? $")
totalPeople = input("How many people to split the bill? ")
percentChoice = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")

total = 0


def allInAll():
    global total
    total += float(totalBill)
    total /= float(totalPeople)


if percentChoice == "12":
    total = float(totalBill) * 0.12
    allInAll()
elif percentChoice == "10":
    total = float(totalBill) * 0.10
    allInAll()
elif percentChoice == "15":
    total = float(totalBill) * 0.15
    allInAll()

print("Each person should pay: ${:.2f}".format(total))
