# Predict temperature using hardcoded coefficients
a = 0.5
b = -3
c = 28
t = 5  # Time (e.g., 5 th hour or 5 th day)

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")
