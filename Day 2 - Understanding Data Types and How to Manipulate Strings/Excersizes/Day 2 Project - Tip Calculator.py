#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
totalBill = float(input ("What was your total bill? $"))
totalTip = int(input("What percentage would you like to give?  10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

billWithTip = totalTip/ 100 * totalBill + totalBill
billPerPerson = billWithTip / people
finalAmount = round(billPerPerson, 2)
finalAmount = "{:.2f}".format(billPerPerson)
print(f"Each person should pay ${finalAmount}")