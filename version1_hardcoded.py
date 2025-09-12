import matplotlib.pyplot as plt
import numpy as np

# Coefficients
a = 0.5
b = -2.0
c = 28.0

# Range of time values (0 to 10)
times = np.arange(0, 11, 1)
temps = a * times**2 + b * times + c

# Specific calculation for t = 5
t = 5
temperature = a * t**2 + b * t + c

print(f"Predicted temperature at time t:{t}: {temperature:.2f}°C")

# Plot graph
plt.figure(figsize=(8,5))
plt.plot(times, temps, marker='o', linestyle='-', color='b', label="Temperature Curve")
plt.scatter(t, temperature, color='r', s=60, zorder=5,
            label=f"t={t}, T={temperature:.2f}°C")
plt.title("Version 1: Hardcoded Coefficients")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG
plt.savefig("weather_prediction.png")
plt.close()

print("\nGraph saved as 'weather_prediction.png'")