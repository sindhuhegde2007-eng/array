# Accept temperature input from the user
temperature = float(input("Enter the temperature in °C: "))

# Determine the condition
if temperature < 15:
    print("It's cold ❄️")
elif temperature > 30:
    print("It's hot 🔥")
else:
    print("It's normal 🌤️")