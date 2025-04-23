import random

def objective_function(x):
    return -x**2 + 4*x

def hill_climb(start, step_size=0.1, max_iterations=1000):
    current = start
    current_value = objective_function(current)

    for _ in range(max_iterations):
        # Look at two neighbors: left and right
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        # Pick the better direction
        if left_value > current_value:
            current, current_value = left, left_value
        elif right_value > current_value:
            current, current_value = right, right_value
        else:
            # No better neighbor — local maximum
            break

    return current, current_value

# Start at a random point between 0 and 4
start_point = random.uniform(0, 4)
solution, value = hill_climb(start_point)

print(f"Start at: {start_point:.2f}")
print(f"Found maximum at x = {solution:.4f}, value = {value:.4f}")
