import math

# ask the user to select whether they would like to select investment or bond, use .lower to ensure the if argument is valid

user_selection = input("Please select 1 of the following 2 options you would like to calculate: \n\n Investment  - to calculate the amount of interest you'll earn on your investment \n Bond        - to calculate the amount you'll have to pay on a home loan \n\n Enter selection here: ").lower()  

#once selected, we need all the relevant data input by the user to calculate the investment/bond 

if user_selection == "investment":
    print("\n\n You have selected investment, please fill out the information below; \n")
    
    amount_money_deposit = int(input("Amount of money you wish to deposit: "))
    interest_rate = int(input("Interest rate: "))/100
    num_of_years = int(input("Number of years you plan to invest: "))
    interest_type = input("Simple or compound interest: ").lower()

# interest_type will change the calculation as below variables, I've added the rounding command so that the output is legible as a monetary figure

    simple_interest = amount_money_deposit*(1 + interest_rate*num_of_years)
    simple_interest = (round(simple_interest, 2))

    compound_interest = amount_money_deposit * math.pow((1+interest_rate),num_of_years)
    compound_interest = (round(compound_interest, 2))


# nested if statements to give different statement printed dependent on which interest type has been selected and calculated

    if interest_type == "simple":
        print(f"\n\nThe total the amount of interest you'll earn on your investment with simple interest is: £{simple_interest}")
        
    if interest_type == "compound":
        print(f"\n\nThe total the amount of interest you'll earn on your investment with compound interest is: £{compound_interest}")
        
# else if user selects bond, we ask for the relevant information to perform the calculation from the user, then turn the user input into an integer for the calculation. Again using the rounding command to display as a monetary value

elif user_selection == "bond":
    print("\n\n You have selected investment, please fill out the information below; \n")

    value_of_house = int(input("The current value of the house: "))
    interest_rate = int(input("The interest rate: "))/100/12
    num_months_repay = int(input("Number of months you plan to take to repay the bond: "))

    bond_repayment = (interest_rate * value_of_house)/(1 - (1 + interest_rate)**(-num_months_repay))
    bond_repayment = (round(bond_repayment, 2))
    bond_statement = f"\n\nBased on the information you have entered, your monthly repayments will be: £{bond_repayment}"
    print(bond_statement)

# Program asks the user to try again if correct repsonse is not entered

else:
    print("You have not entered the correct information, please try again by typing either investment or bond")
    





