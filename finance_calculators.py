'''
Assume you have been approached by a small financial company and asked to
create a program that allows the user to access two different financial calculators:
an investment calculator and a home loan repayment calculator.

1. The user should be allowed to choose which calculation they want to do.

2. How the user capitalises their selection should not affect how the program
proceeds. i.e. 'Bond', 'bond', 'BOND' or 'Investment', 'investment', 'INVESTMENT',
etc., should all be recognised as valid entries. If the user doesn't type 
in a valid input, show an appropriate error message.

3. If the user selects 'investment', do the following:
   Ask the user to input:
   - The amount of money that they are depositing.
   - The interest rate (as a percentage). Only the number of the interest
     rate should be entered (e.g. the user should enter 8 and not 8%).
   - The number of years they plan on investing.
   - Then ask the user to input if they want "simple" or "compound" interest,
     and store this in a variable called "interest". Depending on whether or 
     not they typed "simple" or "compound", output the appropriate amount that 
     they will get back after the given period, at the specified interest rate.
   - Print out the answer.

4. If the user selects 'bond', do the following:
   Ask the user to input:
   - The present value of the house. e.g. 100000
   - The interest rate e.g. 7
   - The number of months they plan to take to repay the bond e.g. 120
   - Calculate how much money the user will have to repay each month and 
     output the answer.
'''

import math

print("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan")

option_selected = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if option_selected == "investment":
    deposit = int(input("Enter the amount of money you are depositing: "))
    interest_rate = int(input("Enter your interest rate (just the number): "))
    years_investing = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter if you want 'simple' or 'compound' interest: ").lower()
    simple_interest = deposit *(1 + (interest_rate/100) * years_investing )
    compound_interest = deposit* math.pow((1+(interest_rate/100)), years_investing)

    if interest_type == "simple":
        print(f"Your simple interest is: £{simple_interest:.2f}")
    
    else:
        print(f"Your compound interest is: £{compound_interest:.2f}")


elif option_selected == "bond":
    house_value = int(input("Enter the value of the house: "))
    interest_rate_bond = int(input("Enter your interest rate (just the number): "))/100
    interest_rate_bond = interest_rate_bond/12
    num_months = int(input("Enter the number of months needed to repay bond: "))
    bond_repay = ((interest_rate_bond) * house_value) / (1 - (1 + (interest_rate_bond))** (- num_months))
    print(f"Your bond repayment is: £{bond_repay:.2f}")
