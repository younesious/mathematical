import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, xp):
    n = len(x)
    yp = 0
    
    for i in range(n):    
        p = 1
        
        for j in range(n):
            if i != j:
                p = p * (xp - x[j])/(x[i] - x[j])
        
        yp = yp + p * y[i]
    
    return yp

n = int(input('Enter number of data points: '))

x = np.zeros((n))
y = np.zeros((n))

print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input('x[' + str(i) + '] = '))
    y[i] = float(input('y[' + str(i) + '] = '))

xp = np.linspace(min(x), max(x), 1000)

yp = [lagrange_interpolation(x, y, point) for point in xp]

fig = plt.figure(figsize=(10, 8))
plt.plot(xp, yp, 'b', label='F(x)')
plt.scatter(x, y, color='red', label='Data Points')
plt.title('Lagrange Polynomial Interpolation')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
