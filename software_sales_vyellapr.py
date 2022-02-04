"""
Author: Venkata Yellapragada, vyellapr@purdue.edu
Assignment: 02.2 - Software Sales
Date: 01/31/2022

Description:
    Takes user input for number of packages purchase
    and identifies amount of discount received.

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
    packages = float(input("How many packages will be purchased: ")) #takes user input for number of packages

    discount = 0
    total = packages * 880 #calculates cost

    if (packages < 1):
        print(f"  Invalid Input!")
        discount = -1
    elif (1 <= packages <= 3):
        print(f"  No discount applied.")
    elif (4 <= packages <= 39):
        print(f"  10% discount applied.")
        discount = 0.1
    elif (40 <= packages <= 199):
        print(f"  15% discount applied.")
        discount = 0.15
    elif (200 <= packages <= 999):
        print(f"  30% discount applied.")
        discount = 0.3
    elif (1000 <= packages):
        print(f"  42% discount applied.")
        discount = 0.42

    total = total * (1 - discount)

    if (discount != -1):
        print(f"  The total price to purchase {packages:0.0f} packages is ${total:,.2f}.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
