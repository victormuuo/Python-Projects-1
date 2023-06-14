def main():
    print("This program converts Dollars to Kenyan Shillings")
    print()

    dollars=eval(input("Enter amount in dollars: "))

    Kshs=convert_to_Kshs(dollars)
    print("That is"  +  " %.2f " % Kshs,"Kshs")

convert_to_Kshs=lambda dollars:dollars*137.45
main() 