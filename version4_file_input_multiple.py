import matplotlib.pyplot as plt
import numpy as np

# Read coefficients and time from file
# Predict temperatures from multiple sets of coefficients in a file
with open("inputs_multiple.txt.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = a * t**2 + b * t + c
        print(f"a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")

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
plt.savefig("file_input_weather2.png")
plt.close()

print("\nGraph saved as 'file_input_weather.png' in your repository.")
