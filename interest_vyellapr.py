"""
Author: Venkata Yellapragada, vyellapr@purdue.edu
Assignment: 01.2 - Interest
Date: 01/26/2022

Description:
    Performs the amount of money after a certain time given principal,
    interest rate, number of years, and compounding frequency.

Contributors:
    NA

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""

def main():
    print("Enter the following parameters.")
    P = float(input("  The initial deposit? ")) #takes inputs and assigns them to relevant variables
    r = (float(input("  The annual interest rate in percent? ")))/100
    t = float(input("  The number of years the account earn interest? "))
    n = float(input("  The number of times interest is compounded each year: "))

    final = P * (1 + r / n) ** (n * t) #calculates future value based on given inputs

    print(f"The balance of this account will be ${final:,.2f} after {t:0.1f} years.") #outputs future values in appropraite format

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
