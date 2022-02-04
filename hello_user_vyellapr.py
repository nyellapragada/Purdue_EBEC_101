"""
Author: Venkata Yellapragada, vyellapr@purdue.edu
Assignment: 00.1 - Hello User
Date: 01/26/2022

Description:
    Outputs a greeting to the identified user thorough a user input.

Contributors:
    N/A

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
    inp1 = input("What is your name? ") #takes user input to the question and assigns it to variable inp1
    print("Hello " + inp1 + "!\n") #prints the user input in appropriately formatted output statement 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
