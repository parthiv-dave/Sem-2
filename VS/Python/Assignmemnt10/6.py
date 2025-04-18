import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at the endpoints.")
    
    history = []
    for _ in range(max_iter):
        c = (a + b) / 2
        history.append([a, b, c, f(c)])
        
        if abs(f(c)) < tol:
            break
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c, len(history), np.array(history)

def find_initial_interval(f, max_attempts=100, range_min=-10, range_max=10):
    for _ in range(max_attempts):
        a = np.random.uniform(range_min, range_max)
        b = np.random.uniform(range_min, range_max)
        if a > b:
            a, b = b, a
        if f(a) * f(b) < 0:
            return a, b
    raise ValueError("Could not find a suitable interval after max_attempts.")

if __name__ == "__main__":
    a, b = find_initial_interval(f)
    print(f"Initial interval: [{a}, {b}]")
    
    root, iterations, history = bisection_method(f, a, b)
    print(f"Approximate root: {root}")
    print(f"Iterations: {iterations}")
    
    x = np.linspace(a, b, 400)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter(history[:, 2], np.zeros_like(history[:, 2]), color='red', label='Midpoints')
    plt.scatter([root], [0], color='green', label='Root', zorder=5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method Root Finding')
    plt.legend()
    plt.grid(True)
    plt.show()