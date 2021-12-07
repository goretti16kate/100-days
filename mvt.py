'''
To satisfy the Mean Value Theory, a function must satisfy three conditions :
1 - The function Must be continous
2 - The function Must be differentiable
3 - The function must have a value c such that f'(c) = [f(b) - f(a)]/(b-a) 
'''

import math
from sympy import *
import random

x,y,z,a,b,c = symbols('x y z a b c')
init_printing(use_unicode=True)


#Part a
flagcontinuity = False
flagdifferentiability = False

def f(x):
   expr = 100*exp(-x/10) - (1/10)*(x)**2
   return expr
print(f(x)) 

print('Graph')
plot(f(x),(x,0,20))


#Part b
print('Condition 1')
inhdlimit_pos = limit(f(x),x,0,'+')
inhdlimit_neg = limit(f(x),x,0,'-')
print(inhdlimit_pos)
print(inhdlimit_neg)
jnhdlimit_pos = limit(f(x),x,20,'+')
jnhdlimit_neg = limit(f(x),x,20,'-')
print(jnhdlimit_pos)
print(jnhdlimit_neg)

if(inhdlimit_pos==inhdlimit_neg)and(inhdlimit_neg==f(0))and(jnhdlimit_pos==jnhdlimit_neg):
   print('The function is continous')
   flagcotinuity = True
else:
   print('The function is not continous')


print('Condition 2')

for i in range(0,30):
   j = random.uniform(0,20)
   diffinhd = diff(limit(f(x),x,j,'+'))
   diffjnhd = diff(limit(f(x),x,j,'-'))
print(diffinhd)
print(diffjnhd)

if (diffinhd == diffjnhd):
   print('The function is differentiable')
   flagdifferentiablity = True
else:
   print('The function is not differentiable')


if (flagcontinuity == True or flagdifferentiability == True):
   print('The theory is not applicable')
else:
   print('The theory is applicable')

print('Finding the derrivatives of the function')
d = diff(f(x),x)
print('The derrivative of "f(x)" is ', d)

print("This means that there's some constant c")

#a = float(input('Enter The Value Of a :'))
a = 0
#b = float(input('Enter The Value Of b :'))
b = 20
ratio = (f(b)-f(a))/(b-a)

print(ratio)


rd = round(ratio,2)

print('The ratio rounded to 2 decimal place : ', rd)

print('Condition 3')
print('Finding the value of c')
print(diff(f(c),c), '=' , rd)

z = diff(f(c),c)
simplify(diff(f(c),c))

print(solve((c*(c-2)+c*(c-1)+(c-2)*(c-1)-rd),c))
va = solve((c*(c-2)+c*(c+1)+(c-2)*(c-1)-rd),c)

print('Values of c ', va)
print('It lies between', a, b)

plot(f(x),(x,0,20),va[0],va[1])
