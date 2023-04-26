import unittest


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

class BMICalculatorTests(unittest.TestCase):
    """Unit tests for BMI calculator functions."""

    def test_calculate_bmi(self):
        """Test the calculate_bmi function."""
        self.assertAlmostEqual(calculate_bmi(70, 170), 24.22, places=2)
        self.assertAlmostEqual(calculate_bmi(50, 150), 22.22, places=2)
        self.assertAlmostEqual(calculate_bmi(90, 200), 22.50, places=2)

    def test_get_health_category(self):
        """Test the get_health_category function."""
        self.assertEqual(get_health_category(16.5), "Underweight")
        self.assertEqual(get_health_category(22.5), "Normal weight")
        self.assertEqual(get_health_category(27.5), "Overweight")
        self.assertEqual(get_health_category(35.0), "Obese")

if __name__ == '__main__':
    unittest.main()
