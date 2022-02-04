"""
Author: Venkata Yellapragada, vyellapr@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 02/03/2022

Description:
    Outputs the kinematic viscosity based on user inputs
    for temperature, velocity, diameter. I have to calculate
    this by hand for AAE 333. 

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
    #user inputs
    T = float(input("Enter the temperature in °C as 5, 20, or 50: "))
    V = float(input("Enter the velocity of water in the pipe (m/s): "))
    d = float(input("Enter the pipe's diameter (m): "))

    if (T == 5): #assigns kinematic viscosity based on temperature
        v = 1.52 * 10.0 ** -6.0 #kinematic viscosity
    elif (T == 20):
        v = 1.0 * 10.0 ** -6.0
    elif (T == 50):
        v = 5.54 * 10.0 ** -7.0

    Re = (V * d) / v #calculates the relevant Reynolds number

    print(f"At {T}°C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {Re:,.2e}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
