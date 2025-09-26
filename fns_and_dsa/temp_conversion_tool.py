CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if _name_ == "_main_":
    print("Temperature Conversion Tool")
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2f}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
