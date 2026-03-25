print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_percentage = tip / 100
tip_amount = bill * tip_percentage
total = bill + tip_amount
individual_contribution = total / people
rounded_individual_contribution = round(individual_contribution, 2)

print(f"Each person should ideally pay ${rounded_individual_contribution}")