# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)
anos_restantes = 90 - age_as_int
dias_restantes = anos_restantes * 365
semanas_restantes = anos_restantes * 52
meses_restantes = anos_restantes * 12

print(f"You have {dias_restantes} days, {semanas_restantes} weeks, and {meses_restantes} months left.")