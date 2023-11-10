# Print the intro
print("Welcome to the tip-calculator")

# Get the total bill 
bill = float(input("What was the total bill? $ "))

# Get the tip percentage
tip = int(input("How much tip will you like to give? 10, 12, 15? "))

# Get the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Convert tip percentage to decimal
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including tip
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay
bill_per_person = total_bill / people

# Format the final amount to two decimal places
final_amount = "{:.2f}".format(bill_per_person)

# Print the final amount each person should pay
print(f"Each person should pay: ${final_amount}")
