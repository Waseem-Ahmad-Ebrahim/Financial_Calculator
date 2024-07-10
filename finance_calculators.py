import math

def investment_calculator():
    """
    Calculate the total amount after investing a principal sum of money
    for a specified number of years with a given interest rate.
    
    Inputs:
    - P (float): Principal amount (initial deposit).
    - r (float): Annual interest rate (as a decimal).
    - t (int): Number of years for the investment.
    - interest (str): Type of interest calculation ('simple' or 'compound').
    
    Output:
    - Prints the total amount after the investment period.
    """

    print("\nInvestment Calculator\n")
    
    P = None
    r = None
    t = None
    interest = None
    
    while True:
        if P is None:
            try:
                P = float(input("Enter the amount of money you are depositing: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue
        
        if r is None:
            try:
                r = float(input("Enter the interest rate (as a percentage): ")) / 100
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue
        
        if t is None:
            try:
                t = int(input("Enter the number of years you plan on investing for: "))
                if t == 0:
                    raise ZeroDivisionError
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue
            except ZeroDivisionError:
                print("Error: Please enter a non-zero value for the number of years.")
                continue
        
        if interest is None:
            interest = input("Do you want simple or compound interest? ").strip().lower()
            if interest not in ["simple", "compound"]:
                print("Invalid choice of interest type. Please choose 'simple' or 'compound'.")
                interest = None
                continue
        
        if P is not None and r is not None and t is not None and interest is not None:
            try:
                if interest == "simple":
                    A = P * (1 + r * t)
                elif interest == "compound":
                    A = P * math.pow((1 + r), t)
                
                print(f"\nThe total amount after {t} years at an interest rate of {r*100}% will be: R {A:.2f}")
                break  # Exit the loop if calculations are successful
            
            except Exception as e:
                print(f"An error occurred during calculation: {str(e)}")
                P = None
                r = None
                t = None
                interest = None
                continue


def bond_calculator():
    """
    Calculate the monthly repayment amount for a bond given the present
    value of the house, annual interest rate, and number of months for repayment.
    
    Inputs:
    - P (float): Present value of the house.
    - i (float): Monthly interest rate (annual rate divided by 12).
    - n (int): Number of months to repay the bond.
    
    Output:
    - Prints the monthly repayment amount for the bond.
    """

    print("\nBond Repayment Calculator\n")
    
    P = None
    i = None
    n = None
    
    while True:
        if P is None:
            try:
                P = float(input("Enter the present value of the house: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue
        
        if i is None:
            try:
                i = float(input("Enter the annual interest rate: ")) / 100 / 12
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue
        
        if n is None:
            try:
                n = int(input("Enter the number of months to repay the bond: "))
                if n == 0:
                    raise ZeroDivisionError
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue
            except ZeroDivisionError:
                print("Error: Please enter a non-zero value for the number of months.")
                continue
        
        # If all inputs are valid, calculate and print the result
        if P is not None and i is not None and n is not None:
            try:
                repayment = (i * P) / (1 - math.pow((1 + i), -n))
                
                print(f"\nThe monthly repayment amount for the bond will be: R {repayment:.2f}")
                break  # Exit the loop if calculations are successful
            
            except Exception as e:
                print(f"An error occurred during calculation: {str(e)}")
                P = None
                i = None
                n = None
                continue


def finance_calculators():
    """
    Main function to run the Finance Calculator program. Allows users to choose
    between the investment and bond calculators or exit the program.
    """

    print("\n-------------------------------------------------------------")
    print("            Welcome to the Finance Calculator!")
    print("-------------------------------------------------------------")
    
    while True:
        print("\nChoose either 'investment' or 'bond' from the menu below to proceed:\n")
        print("1. investment      -  to calculate the amount of interest you'll earn on interest")
        print("2. bond            -  to calculate the amount you'll have to pay on a home loan")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3) or ('investment'/'bond'/'exit'): ").strip()
        
        if choice == "1" or choice.lower() == "investment":
            investment_calculator()
        elif choice == "2" or choice.lower() == "bond":
            bond_calculator()
        elif choice == "3" or choice.lower() == "exit":
            print("\nExiting Finance Calculator. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    finance_calculators()
