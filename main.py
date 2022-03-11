#If \the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
bill_amount = input("What was the toatal bill?$")
per_bill_amt = input("What percentage tip would you like to give 10,12 or 15 ?")
person_split = input("How many people to split the bill?")

#Logic Building
#tip calculation
tip_amt = (int(per_bill_amt)/100)
#total bill after tip addition at 12% rate
total_bill = float(bill_amount) + 18
#splitting of bill among 5 people
split_bill = (total_bill/int(person_split))
final_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay ${final_bill}")



