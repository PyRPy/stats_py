
# coding: utf-8

# In[1]:


# Chapter 4 Algebra and symbolic math with sympy


# In[2]:


## working with expressions


# In[4]:


from sympy import Symbol
x = Symbol('x')
y = Symbol('y')


# In[7]:


from sympy import factor, expand
expr = x**2 - y**2
factor(expr)


# In[8]:


factors = factor(expr)
expand(factors)


# In[9]:


expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
factors


# In[10]:


expand(factors)


# In[11]:


expr = x + y + x*y
factor(expr)


# In[12]:


## Pretty printing


# In[13]:


from sympy import pprint
pprint(expr)


# In[14]:


expr = 1 + 2*x + 2*x**2
pprint(expr)


# In[15]:


from sympy import init_printing
init_printing(order = 'rev-lex')
pprint(expr)


# In[16]:


## substituting values


# In[17]:


x = Symbol('x')
y = Symbol('y')
expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2})
print(res)


# In[18]:


expr.subs({x:1-y})


# In[20]:


expr_subs = expr.subs({x:1-y})
from sympy import simplify
simplify(expr_subs)


# In[21]:


## calculating the value of a series


# In[24]:


from sympy import Symbol, pprint, init_printing
def print_series(n, x_value):
    
    # initialize printing system with reverse order
    init_printing(order = 'rev-lex')
    
    x = Symbol('x')
    series = x
    for i in range(2, n + 1):
        series = series + (x**i)/i
        
    pprint(series)
    
    # evaluate the series at x_value
    series_value = series.subs({x:x_value})
    print('value of the serires at {0}: {1}'.format(x_value, series_value))


# In[25]:


if __name__ == '__main__':
    n = input('enter the number of terms you want in the series')
    x_value = input('enter the value of x at which you want to evaluate the series')
    
    print_series(int(n), float(x_value))


# In[26]:


## converting strings to mathematical expressions


# In[30]:


from sympy import simplify # pay attenion to simplify and simpify...confusing
from sympy.core.sympify import SympifyError
expr = input('enter a mathematical expression: ')


# In[32]:


try:
    expr = simplify(expr)
except SympifyError:
    print('invalid input')


# In[33]:


## expression multiplier


# In[35]:


"""
product of two expressions
"""

from sympy import expand, simplify
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
    prod = expand(expr1*expr2)
    print(prod)


# In[36]:


expr1 = input('enter the first expressoin: ')


# In[37]:


expr2 = input('enter the second expression: ')


# In[38]:


try:
    expr1 = simplify(expr1)
    expr2 = simplify(expr2)
except SympifyError:
    print('invalid input')
else:
    product(expr1, expr2)


# In[39]:


## Solving equations


# In[40]:


from sympy import Symbol, solve
x = Symbol('x')
expr = x - 5 - 7
solve(expr)


# In[41]:


## solving quadratic equations


# In[42]:


from sympy import solve
x = Symbol('x')
expr = x**2 + 5*x + 4
solve(expr, dict=True)


# In[45]:


from sympy import solve
x = Symbol('x')
expr = x**2 + 1*x + 1
solve(expr, dict=True)


# In[46]:


## solving for one variable in terms of others


# In[47]:


x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expr = a*x*x + b*x + c
solve(expr, x, dict=True)


# In[48]:


s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')

expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr, t, dict=True)
pprint(t_expr)

