# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# totalDays = 32650
# totalWeeks = 4680
# totalMonths = 1080
# calculatedDays = int((totalDays) - (int(age)*365))
# calculatedWeeks = int(totalWeeks) - (int(age)*52)
# calculatedMonths = int(totalMonths) - (int(age)*12)
# print(f"You have {calculatedDays} days, {calculatedWeeks} weeks, and {calculatedMonths} months left")

#Solution
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} left.")
print(message)

