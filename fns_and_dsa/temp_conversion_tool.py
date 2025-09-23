# temp_conversion_tool.py

# ===== Global Conversion Factors =====
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# ===== Conversion Functions =====
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using
    the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using
    the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# ===== Main Function =====
def main():
    try:
        # Prompt user for temperature
        temp_input = input("Enter the temperature to convert: ").strip()
        
        # Validate numeric input
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Ask user for the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


# Run the program
if __name__ == "__main__":
    main()
