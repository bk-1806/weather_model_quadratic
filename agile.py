# agile_mode.py
import matplotlib.pyplot as plt

# Quadratic model function
def quadratic_weather_model(time, a, b, c):
    """Predict temperature using quadratic equation T(t) = at² + bt + c"""
    return a * (time ** 2) + b * time + c

print("\n=== AGILE MODE ===")
# Coefficients (unique for Agile mode, so graph looks different)
a, b, c = -0.08, 1.0, 23

times_to_check = [0, 6, 12, 18, 24]
all_sprints = []

for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    temps = []
    for t in times_to_check:
        temp = quadratic_weather_model(t, a, b, c)
        temps.append(temp)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
    all_sprints.append(temps)

# 📊 Plot graph for both sprints
plt.figure(figsize=(8, 5))
for i, temps in enumerate(all_sprints):
    plt.plot(times_to_check, temps, marker='o', linestyle='-', label=f"Sprint {i+1}")

plt.title("Weather Prediction (Agile Mode)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

# Save graph as PNG
plt.savefig("agile_weather.png", dpi=300)

# Show graph
plt.show()
