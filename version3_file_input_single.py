import matplotlib.pyplot as plt
import numpy as np

# Read coefficients and time from file
with open("inputs_single.txt.txt", "r") as f:
    lines = f.readlines()

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

# Calculate temperature at given t
T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")

# Range of time values (0–24 hours)
times = np.arange(0, 25, 1)
temps = a * times**2 + b * times + c

# Plot graph
plt.figure(figsize=(8,5))
plt.plot(times, temps, marker='o', linestyle='-', color='b', label="Temperature Curve")
plt.scatter(t, T, color='r', s=100, zorder=5, label=f"t={t}, Temp={T:.2f}°C")  # highlight point
plt.title("Quadratic Weather Prediction (File Input)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG (for GitHub Codespaces)
plt.savefig("file_input_weather.png")
plt.close()

print("\nGraph saved as 'file_input_weather.png' in your repository.")
