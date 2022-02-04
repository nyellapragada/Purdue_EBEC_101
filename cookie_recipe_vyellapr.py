"""
Author: Venkata Yellapragada, vyellapr@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 01/26/2022

Description:
    Calculates required quantities of ingredients based
    on the number of cookies the user wants to bake.

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
    cookies = int(input("How many cookies do you want to make? "))

    ratio = cookies / 48 #ratio to help calculate ingredient quantities
    butter = ratio * 1.25
    sugar = ratio * 1.5
    flour = ratio * 2.5

    print(f"To make {cookies:,} cookies, you will need:") #outputs relevant quantities in appropriate format
    print(f"{butter:10,.2f} cups of butter")
    print(f"{sugar:10,.2f} cups of sugar")
    print(f"{flour:10,.2f} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
