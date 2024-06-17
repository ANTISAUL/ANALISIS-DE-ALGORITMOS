import random

def estimate_pi(num_samples):
    points_inside_circle = 0
    
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # π is approximately 4 times the ratio of points inside the circle to the total points
    return 4 * points_inside_circle / num_samples

# Ejemplo de uso con 10 millones de puntos para una mejor aproximación
pi_approx = estimate_pi(10_000_000)
print(f"Aproximación de Pi: {pi_approx}")
