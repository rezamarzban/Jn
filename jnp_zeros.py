import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jnp_zeros

# Define the range of x values
x = np.linspace(0, 20, 400)

# Define the orders of the Bessel functions to plot
orders = [0, 1, 2, 3]

# Number of zeros to compute for each order
num_zeros = 5

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the derivative of each Bessel function and compute its zeros
for n in orders:
    # Compute the derivative of the Bessel function using the recurrence relation
    j_prime = (jn(n - 1, x) - jn(n + 1, x)) / 2.0
    
    # Plot the derivative of the Bessel function
    plt.plot(x, j_prime, label=f"J'_{n}(x)")
    
    # Compute the first few zeros of the derivative of the Bessel function
    zeros = jnp_zeros(n, num_zeros)
    print(f"Zeros of J'_{n}(x): {zeros}")
    
    # Mark the zeros on the plot
    plt.scatter(zeros, np.zeros_like(zeros), color='red', zorder=5)

# Add labels and title
plt.title("Derivative of Bessel Functions of the First Kind with Zeros")
plt.xlabel("x")
plt.ylabel("J'_n(x)")
plt.grid()
plt.legend()
plt.xlim(0, 20)
plt.ylim(-0.5, 1)

# Show the plot
plt.show()
