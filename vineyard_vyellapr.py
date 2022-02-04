"""
Author: Venkata Yellapragada, vyellapr@purdue.edu
Assignment: 01.1 - Vineyard
Date: 01/26/2022

Description:
    Program that takes user input for amount of space used an end post
    assembly, amount of space between the vines, and length of the row
    and outputs the number of grapevines that will fit in the row.

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

    print("Enter each of the following quantities in meters.")
    E = float(input("  How wide is the end-post assembly? ")) #takes user input for assembly width and assigns it to E
    S = float(input("  How much space should be between the vines? ")) #takes user input for space between vines and assigns it to S
    R = float(input("  How long is this row? ")) #takes user input for length of row and assigns it to R

    output = int((R - 2 * E) / S) #calculates the number of grapevines that fit, converts to an integer, assigns to output

    print("\nThere is enough space for", output, "vine(s) in this row.") #outputs data in appropriate format

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
