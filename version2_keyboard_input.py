import matplotlib.pyplot as plt
import numpy as np

# Take user input
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
c = float(input("Enter c value: "))
t = float(input("Enter t value: "))

# Calculate temperature at given t
temp = a * t**2 + b * t + c
print(f"Temperature at t={t}: {temp:.2f}°C")

# Range of time values (0–10 for clean graph)
times = np.arange(0, 11, 1)
temps = a * times**2 + b * times + c

# Plot graph
plt.figure(figsize=(8,5))
plt.plot(times, temps, marker='o', linestyle='-', color='b', label="Temperature Curve")
plt.scatter(t, temp, color='r', s=80, zorder=5, label=f"t={t}, T={temp:.2f}°C")
plt.title("Version 2: User Input Coefficients")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save PNG (for GitHub Codespaces)
plt.savefig("user_input_weather.png")
plt.close()

print("\nGraph saved as 'user_input_weather_v2.png' in your repository.")
