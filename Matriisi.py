import numpy as np
from sympy import symbols, solve

print('Tehtävä 3')
# Tehtävänannon matriisi
A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])
print(f"A=\n{A}")
print(f"B=\n{B}")
# Kerrotaan matriisit
print(f'\n2A=\n{2*A}, \n3B=\n{3*B}')
# Ratkaistaan lause 2A+3B
print(f'\n2A+3B=\n{2*A+3*B}')

x, y, z = symbols('x, y, z')

a = solve([5*x+3*y+9, 2*x+y+4], [x, y])

b = solve([2*x+y+z+6, x+3*y+z+2, 2*x+y+2*z+9], [x, y, z])

c = solve([x+y+3*z-1, 3*x+y+z+5, 2*x+y+2*z+2], [x, y, z])

print(f'a){a}\nb){b}\nc){c}')
