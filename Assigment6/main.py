'''
    Spirit Animal: generousIbex
    Date:          19/10/16
    Challenge #:   6
    Sources:
            - Dr. Jones Lecture
            - http://www.cs.olemiss.edu/~jones/doku.php?id=csci343_polynomial_regression
'''

import matplotlib.pyplot as mplot
import numpy as np


raw_data = []
x = []
y = []
x_structure = []
y_structure = []
with open('generousIbex_ch6.csv', 'r') as file:
    for line in file:
        raw_data.append(list(map(float,line.strip().split(','))))
        x.append(raw_data[-1][0])
        y.append(raw_data[-1][1])
        if float(raw_data[-1][2]) ==  24.782597:
            x_structure.append(x[-1])
            y_structure.append(y[-1])


degree = 16
model_params = np.polyfit(x_structure, y_structure, degree )
y_predict = np.polyval(model_params, x_structure)

mplot.scatter(x_structure, y_structure, color='b')
mplot.plot(x_structure, y_predict, color='r', linewidth=3)
mplot.show()
