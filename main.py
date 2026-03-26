print("Welcome to our dearest Tip Calculator!")
subtotal = float(input("How much was the total bill? \n$"))
tip_percentage = float(input("What percentage would you like to tip? 10, 12, or 15?\n"))
bill_splitters = int(input("How many people will be splitting the bill?\n"))

tip_decimal = tip_percentage / 100
tip_amount = subtotal * tip_decimal
total = subtotal + tip_amount
total_per_person = total / bill_splitters
rounded_amount = round(total_per_person, 2)

print(f"Each person should ideally pay: ${rounded_amount}")