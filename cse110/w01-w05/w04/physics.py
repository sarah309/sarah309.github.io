# solve a physics problem
import math

print('Welcome to the velocity calculator. Please enter the following:')
print()

m = float(input('Please enter the Mass (in kg): '))
g = float(input('Please enter the Gravity (9.8m/s^2 for Earth, 24 m/s^2 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('What is the cross-sectional area of the projectile? (in m^2): '))
C = float(input('What is the drag constant? (0.5 for sphere, 1.1 for cylinder): '))

# adding the c
c = (1/2) * p * A * C

velocity = (math.sqrt((m * g) / c)) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print()
print(f'The inner value of c is: {c:.3f}.')
print(f'The velocity after {t} seconds is: {velocity:.3f} m/s.')