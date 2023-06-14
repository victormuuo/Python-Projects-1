def main():
    print("This program converts Kenyan Shillings to Dollars")
    print()

    Kshs=eval(input("Enter amount in Kenyan Shillings: "))

    dollars=convert_to_dollars(Kshs)
    print("That is"  +  " %.2f " % dollars,"dollars")

convert_to_dollars=lambda Kshs:Kshs*0.0074
main() 