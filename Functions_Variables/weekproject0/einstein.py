def main():
    mass = int(input("Enter mass: "))
    e = energy(mass)
    print(f"The energy equivqlent of {mass} kg is {e} J.")

def energy(mass):
    #Solve for the energy equivalent of a given mass.
    speed_of_light_squared = 9 * pow(10,16)
    calculated_energy = mass * speed_of_light_squared
    return calculated_energy

main()
