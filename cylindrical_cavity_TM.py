import numpy as np
from scipy.special import jn_zeros

def calculate_frequencies(radius, height, max_m, max_n, max_p):
    c = 3e8  # Speed of light in m/s
    frequencies = []
    
    for m in range(max_m + 1):  # Loop over m
        for n in range(1, max_n + 1):  # Loop over n (starting from 1)
            for p in range(max_p + 1):  # Loop over p
                freq = (c / (2 * np.pi)) * np.sqrt(
                    (jn_zeros(m, n)[n - 1] / radius) ** 2 + (p * np.pi / height) ** 2
                )
                frequencies.append((m, n, p, freq))
    
    return frequencies

# Cavity parameters
radius = 0.1  # meters
height = 0.2  # meters
max_m = 2     # Maximum m mode
max_n = 2     # Maximum n mode
max_p = 2     # Maximum p mode

# Calculate and print results
frequencies = calculate_frequencies(radius, height, max_m, max_n, max_p)

# Sort frequencies by the frequency value
frequencies.sort(key=lambda x: x[3])

print(f"{'Mode (m,n,p)':<15} {'Frequency (GHz)':<20}")
print("-" * 35)
for (m, n, p, freq) in frequencies:
    print(f"({m},{n},{p})          {freq / 1e9:.2f} GHz")
  
