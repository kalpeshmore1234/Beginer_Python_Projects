convert_to_rupees = lambda dollars: dollars * 81.63

def main():
    print("This program converts US dollars to Indian rupees")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    rupees = convert_to_rupees(dollars)

    print("That is",rupees,"rupees.")


main()