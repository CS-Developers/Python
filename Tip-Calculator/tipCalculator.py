# Basic Printing Function
print("Welcome to the tip calculator.")

totalBill = input("What was the total bill? $")
totalPeople = input("How many people to split the bill? ")
percentChoice = input("What percentage tip would you like to give? 10, 12, or 15? ")


if percentChoice == "12":
   total = float(totalBill) * 0.12
   total = total + float(totalBill)
   total = total / float(totalPeople)
elif percentChoice == "10":
   total = float(totalBill) * 0.10
   total = total + float(totalBill)
   total = total / float(totalPeople)
elif percentChoice == "15":
   total = float(totalBill) * 0.15
   total = total + float(totalBill)
   total = total / float(totalPeople)

print("Each person should pay: ${:.2f}".format(total))

