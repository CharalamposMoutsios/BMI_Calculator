def calculate_bmi(weight, height):
    """Function to calculate BMI."""
    # Convert height to meters
    height_m = height / 100
    # Calculate BMI using the formula: BMI = weight / (height^2)
    bmi = weight / (height_m ** 2)
    return bmi

def get_health_category(bmi):
    """Function to determine health category based on BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        return "Normal weight"
    elif bmi >= 24.9 and bmi < 29.9:
        return "Overweight"
    elif bmi >= 29.9:
        return "Obese"

# Example usage
while True:
    try:
        weight = float(input("Enter weight (kg): "))
        if weight < 1 or weight > 500:
            raise ValueError("Weight must be between 1 and 500 kg.")
        break
    except ValueError as e:
        print(str(e))

while True:
    try:
        height = float(input("Enter height (cm): "))
        if height < 1 or height > 500:
            raise ValueError("Height must be between 1 and 500 cm.")
        break
    except ValueError as e:
        print(str(e))

bmi = calculate_bmi(weight, height)
health_category = get_health_category(bmi)
print(f"Your BMI: {bmi:.2f}")
print(f"Health category: {health_category}")

