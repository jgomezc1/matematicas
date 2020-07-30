# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:08:54 2020

@author: AX201 GMRS
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(z , x ):
    """

    """
    y = z[0]

    dydt = -2*x*y
    dzdt = [dydt ]
    
    return dzdt

plt.figure(2)
x_min = -1.5
x_max = +1.5
y_min = -3.0
y_max = +4.0
y0 = [0.40]                              
x  = np.linspace(x_min , x_max , 101)    
#------Integrate---------
#
sol  = odeint(model , y0 , x )
#
#------Plot---------
#
plt.show()
plt.xlim(x_min , x_max)
plt.ylim(y_min , y_max)
plt.plot(x , sol)