print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
split_bill = int(input("How many people to split the bill?\n"))
tip = tip/100 + 1
bill_person = round(total_bill * tip / split_bill,2)
bill_person = "{:.2f}".format(bill_person)
print(f"Each person should pay: ${bill_person}")