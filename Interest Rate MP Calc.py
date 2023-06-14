#collect the inputs: principal,apr,year
#calculate the monthly payments
#show the user

def MP_Calc():
    print("This is a Monthly Payment loan calculator: ")
    print("")

    principal=float(input("Input the loan amount: "))
    apr=float(input("Input the annual interest rate: "))
    years=int(input("Input amount of years: "))

    monthly_interest_rate=apr/1200
    months=years*12
    monthly_payment=principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-months))

    print("The monthly payment for this loan is: Ksh "+ "%.2f " % monthly_payment)

MP_Calc()    





