import numpy as np, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyModule import consoleClear
from folder0404 import usecsv

discount = .05
cashflow = 100

def presentvalue(n):
    return (cashflow / ((1 + discount) ** n))

consoleClear.clear()

#print(presentvalue(1))
#print(presentvalue(2))

# np.npv(0.045, cashflow)
# np.irr()