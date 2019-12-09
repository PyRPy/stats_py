
# coding: utf-8

# In[1]:


# Chapter 4 Algebra and symbolic math with sympy - 2


# In[2]:


## solving a system of linear equations


# In[3]:


from sympy import Symbol, solve, pprint


# In[4]:


x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12

solve((expr1, expr2), dict=True)


# In[5]:


soln = solve((expr1, expr2), dict=True)
soln = soln[0]


# In[6]:


expr1.subs({x:soln[x], y:soln[y]})


# In[7]:


expr2.subs({x:soln[x], y:soln[y]})


# In[8]:


## plotting using sympy


# In[12]:


from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot(2*x + 3)


# In[11]:


plot((2*x + 3), (x, -5, 5))


# In[13]:


p = plot(2*x + 3, (x, -5, 5), title='a line', xlabel='x', ylabel='2x+3', show=False)


# In[14]:


p.save('line.png')


# In[15]:


## plotting expression input by the user


# In[ ]:


"""
plot the graph of an input expression
"""


# In[22]:


from sympy import Symbol, sympify, solve
from sympy.plotting import plot
from sympy.core.sympify import SympifyError


# In[30]:


def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)


# In[35]:


expr = input('enter your expression in terms of x and y: ')


# In[36]:


try:
    expr = sympify(expr)
except SympifyError:
    print('invalide input')
else:
    plot_expression(expr)


# In[37]:


plot(2*x - 1)


# In[38]:


from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
p = plot(2*x + 3, 3*x + 1, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()

