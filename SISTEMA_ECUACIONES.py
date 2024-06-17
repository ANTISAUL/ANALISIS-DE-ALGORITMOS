import numpy as np
# Coefficients of the system of equations
A = np.array([
    [1, 2, -1, 3],
    [2, 0, 2, -1],
    [-1, 1, 1, 0],
    [3, 3, -2, 2]
])
# Constants on the right-hand side
b = np.array([-8, 13, 8, -1])
# Function to calculate the residual (difference between the left-hand side and right-hand side)
def calculate_residual(x):
    return np.linalg.norm(np.dot(A, x) - b)
# Parameters
max_iterations = 10_000_000
best_x = None
best_residual = float('inf')
# Random search
for i in range(max_iterations):
    # Generate random integer values for x, y, z, t between -5 and 5
    random_solution = np.random.randint(-5, 6, size=4)
    residual = calculate_residual(random_solution)
    # Update the best solution found so far
    if residual < best_residual:
        best_x = random_solution
        best_residual = residual
        # If the residual is 0, we have found an exact solution
        if best_residual == 0:
            break

# Output the best solution found
print(f"Mejor solucion: {best_x} con residual: {best_residual}")
