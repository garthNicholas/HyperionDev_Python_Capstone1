#import the math library

import math

# This will ask user to select between two financial calculators, they will be asked to select between
# 'investment' or 'bond' - and there is a basic description of each displayed for the user to see and read
# before making their selection.

print("Choose either 'investment' or 'bond' from the menu below to proceed" + "\n\n" +
      "Investment - this will calculate the interest you will receive on an investment" + "\n" +
      "Bond - this will calculate the ammount you will have to pay on a home loan" + "\n")

# This will capture user input and convert all variables of how 'invetment' and 'bond' may be spelt and converts it to lower case 
user_calculator = input("Enter investment or bond : \n").lower()


# If the user does not enter any input an error message will be displayed
# If the user enters less than 4 characters, an error message will also be displayed.
if len(user_calculator) == 0:
    print("You have not entered anything")# Error message displayed if no characters are entered
if len(user_calculator) > 1:
    if len(user_calculator) <= 3:
        print("Please enter a valid selection") # Error message displayed if less than 4 characters are entered


# if user selects 'investment' from the choice above,
# they will be asked to confirm what type of interest they would be earning on this investment
# they will be asked to confirm either 'Simple' or 'Compound' and this will be converted to lower case
if user_calculator == "investment":
    interest_type = input("Please confirm the type of interest you would be earning ?: 'simple' or 'compound'  \n").lower()


# if user selects - compound interest, the following formula would apply and be executed
# user is asked to confirm 3 variables - intial investment, interest rate and investment age/duration

    if interest_type == "compound": # A = P* math.pow((1+r),t)
        initial_investment = float(input("Kindly confirm initial capital amount \n"))
        interest_rate = float(input("Kindly confirm interest rate number without the % sign   \n"))
        investment_age = int(input("Kindly confirm investment duration in years  \n"))

# print the compound interest formula        
        total_interest = initial_investment * math.pow((1 +(interest_rate/100)), (investment_age))
        total_interest = round(total_interest, 2)# round answer to two decimal places
        print(f"Your total interest earned on the initial capital amount accumulates to: R{total_interest}  \n")

# if user selects - simple interest, the following formula would apply and be executed
# user is asked to confirm 3 variables - intial investment, interest rate and investment age/duration

    if interest_type == "simple": #  A = P*(1+r*t)
        initial_investment = float(input("Kindly confirm initial capital amount  \n"))
        interest_rate = float(input("Kindly confirm interest rate number without the % sign  \n"))
        investment_age = int(input("Kindly confirm investment duration in years  \n"))

# print the simple interest formula        
        total_interest = initial_investment * (1 + (interest_rate/100) * investment_age)
        total_interest = round(total_interest, 2) # round answer to two decimal places
        print(f"Your total interest earned on the initial capital amount accumulates to: R{total_interest}  \n")


# if user selects 'bond' from the choice above,
# user will be asked to confirm 3 variables -  house value, interest rate and number of months to pay of the bond
# this will be calculated based on user input and printed out

elif user_calculator == "bond":
    house_value = int(input("Kindly confirm the present value of the house  \n"))
    interest_rate = int(input("Kindly confirm interest rate number without the % sign \n"))
    repayment_duration = int(input("Kindly confirm the number of months for repayment  \n"))

    interest_rate = interest_rate / 100
    interest_rate = interest_rate / 12
    
#BOND Repayment formula: x = (i.P)/(1 - (1+i)^(-n))

    monthly_repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-repayment_duration))
    monthly_repayment = round(monthly_repayment, 2)
    print(f"Your monthly repayment will be : R{monthly_repayment}  \n")
