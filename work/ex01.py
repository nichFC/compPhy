# Paris J. Huth: Gruppe 1
# Q inich Pakal Figueroa Coc: Gruppe 5

# imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Numerical Integration
#Task a)
def y_n(x,a,n):
    f = x**n/(x+a)
    return f
  
a = 5
r = np.array([1,5,10,30,50])
x_n = np.linspace(0,1,1000)
for i in r:
    F = np.array([])
    for y in x_n:
        I,dI = integrate.quad(y_n,0,y, args=(a,i))
        F = np.append(F, I)
    plt.plot(x_n,F, label = r'$y_{}$(x,{})'.format(a,i))
plt.grid()
plt.legend(loc= 'best' )
