def main():
    print("This program converts dollars to sterling pounds")
    print()

    dollars=eval(input("Enter amount in dollars: "))

    pounds=convert_to_pounds(dollars)
    print("That is"+ " %.2f " %pounds, "pounds")

convert_to_pounds=lambda dollars:dollars*0.82
main()    