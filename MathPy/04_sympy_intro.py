from sympy import Symbol
# ------------------Defining Symbols and Symbolic Operations -------------------
x = Symbol('x')
print(x + x + 1)

a = Symbol('x')
print(a + a + 1)

# find the original symbol object
print(a.name)

# define multiple symbols
from sympy import symbols
x, y, z = symbols('x, y, z')
s = x*(x + y) + x*(y + z)

print(s)

print(x*x*(1 + x))
