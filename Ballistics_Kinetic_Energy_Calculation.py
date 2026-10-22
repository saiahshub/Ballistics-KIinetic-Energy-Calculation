# BALLISTIC KINETIC ENERGY CALCULATION

# ASSIGNING BULLET MASS IN KILOGRAM

bullet_mass = float(input("Enter the bullet mass(Kg): "))

# ASSIGNING IMPACT VELOCITY 

impact_velocity = float(input("Enter the bullet velocity (m/s): ")) 

# USINGE THE FORMULAR KE = 0.5 * Mass * velocity ^ 2 

kinetic_energy = 0.5 * bullet_mass * impact_velocity ** 2

 
print (f"The calculated Kinetic energy of the bullet is {kinetic_energy} joules")
