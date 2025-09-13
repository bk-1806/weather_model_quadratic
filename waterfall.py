# weather_model.py
import matplotlib.pyplot as plt

# Quadratic model coefficients (different for variation)
a = -0.15
b = 1.2
c = 22

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

print("=== WATERFALL MODE ===")
hours = list(range(0, 25, 6))  # every 6 hours
temps = []

for hour in hours:
    temp = quadratic_weather_model(hour)
    temps.append(temp)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

# 📊 Plot graph
plt.plot(hours, temps, marker='o', linestyle='-', color="blue", label="Waterfall Prediction")
plt.title("Weather Prediction (Waterfall Mode)")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

# Save as PNG
plt.savefig("waterfall_prediction.png", dpi=300)

# Show on screen too (optional)
plt.show()
