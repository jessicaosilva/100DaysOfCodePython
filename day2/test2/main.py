# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
altura  = float(height)
peso  = float(weight)
imc = int(peso /(altura**2))
print(imc)