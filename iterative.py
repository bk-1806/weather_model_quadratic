# iterative_mode.py
import matplotlib.pyplot as plt

# Quadratic model coefficients (different from Waterfall mode for variation)
a = -0.12
b = 1.4
c = 20

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

print("\n=== ITERATIVE MODE ===")
iterations = 3
all_hours = []
all_temps = []

for iteration in range(1, iterations + 1):
    print(f"Iteration {iteration}:")
    hours = list(range(0, 25, 12))  # every 12 hours
    temps = []

    for hour in hours:
        temp = quadratic_weather_model(hour)
        temps.append(temp)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")

    print("---")

    # Save results for plotting
    all_hours.append(hours)
    all_temps.append(temps)

# 📊 Plot graph for each iteration
plt.figure(figsize=(8, 5))
for i in range(iterations):
    plt.plot(all_hours[i], all_temps[i], marker='o', linestyle='-', label=f"Iteration {i+1}")

plt.title("Weather Prediction (Iterative Mode)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

# Save as PNG
plt.savefig("iterative_weather.png", dpi=300)

# Show graph
plt.show()
