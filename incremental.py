# incremental_mode.py
import matplotlib.pyplot as plt

# Quadratic weather function
def quadratic_weather_model(time, a, b, c):
    """Predict temperature using quadratic equation T(t) = at² + bt + c"""
    return a * (time ** 2) + b * time + c

print("\n=== INCREMENTAL MODEL ===")
a, b, c = -0.1, 1.3, 21   # coefficients (different from others for variation)

increments = []

# Increment 1: basic start
inc1 = [quadratic_weather_model(t, a, b, c) for t in [0, 12, 24]]
print("Increment 1 (basic prediction at 0, 12, 24 hrs):", [f"{x:.2f}" for x in inc1])
increments.append((["0", "12", "24"], inc1))

# Increment 2: add more detail
inc2 = [quadratic_weather_model(t, a, b, c) for t in [0, 6, 12, 18, 24]]
print("Increment 2 (detailed at every 6 hrs):", [f"{x:.2f}" for x in inc2])
increments.append((["0", "6", "12", "18", "24"], inc2))

# Increment 3: full hourly data
inc3 = [quadratic_weather_model(t, a, b, c) for t in range(0, 25, 3)]
print("Increment 3 (every 3 hrs):", [f"{x:.2f}" for x in inc3])
increments.append(([str(t) for t in range(0, 25, 3)], inc3))

# 📊 Plot each increment
plt.figure(figsize=(8, 5))
for i, (hours, temps) in enumerate(increments):
    plt.plot(hours, temps, marker='o', linestyle='-', label=f"Increment {i+1}")

plt.title("Weather Prediction (Incremental Model)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

# Save graph as PNG
plt.savefig("incremental_weather.png", dpi=300)

# Show graph
plt.show()
