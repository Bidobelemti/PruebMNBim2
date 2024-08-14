from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**5 - 6*x**4 + 2*x**3 + 20*x**2 - 27*x + 10

interval = np.linspace(-10, 10, 100)

roots = []
for i in range(len(interval) - 1):
    a, b = interval[i], interval[i + 1]
    if f(a) * f(b) < 0: 
        root = optimize.bisect(f, a, b, full_output = True)
        roots.append(root)

print("Raíces encontradas:", roots)

x = np.linspace(-10, 10, 400)
y = f(x)

plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title('Gráfico de f(x) y sus raíces')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()