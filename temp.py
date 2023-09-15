import numpy as np
import matplotlib.pyplot as plt

# Generate a noisy signal
np.random.seed(0)
t = np.linspace(0, 1, 100)  # Time vector
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(100)  # Sinusoidal signal with noise

# Define the window size for the moving average filter
window_size = 5

# Implement the moving average filter
filtered_signal = np.convolve(signal, np.ones(window_size) / window_size, mode='same')

# Plot the original and filtered signals
plt.figure(figsize=(10, 6))
plt.plot(t, signal, label='Original Signal', alpha=0.7)
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Moving Average Filter')
plt.grid(True)
plt.show()
