import numpy as np
import matplotlib.pyplot as plt
from scipy.special import yn, yn_zeros

# Define the range of x values
x = np.linspace(0.1, 20, 400)  # Starting from 0.1 to avoid singularity at x=0

# Define the orders of the Bessel functions to plot
orders = [0, 1, 2, 3]

# Number of zeros to compute for each order
num_zeros = 5

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each Bessel function and compute its zeros
for n in orders:
    # Plot the Bessel function of the second kind
    plt.plot(x, yn(n, x), label=f'Y_{n}(x)')
    
    # Compute the first few zeros of the Bessel function of the second kind
    zeros = yn_zeros(n, num_zeros)
    print(f'Zeros of Y_{n}(x): {zeros}')
    
    # Mark the zeros on the plot
    plt.scatter(zeros, np.zeros_like(zeros), color='red', zorder=5)

# Add labels and title
plt.title('Bessel Functions of the Second Kind with Zeros')
plt.xlabel('x')
plt.ylabel('Y_n(x)')
plt.grid()
plt.legend()
plt.xlim(0, 20)
plt.ylim(-2, 2)

# Show the plot
plt.show()
