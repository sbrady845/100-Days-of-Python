#Operators
# **    Exponent
# *     Multiplicaiton
# +     Addition
# (-)   Subtraction
# /     Divide

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
actualBmi = float(weight) / float(height) ** 2
print(int(actualBmi))