def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    temp_value = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(temp_value)
        kelvin = celsius_to_kelvin(temp_value)
        print(f"{temp_value}°C is {fahrenheit}°F and {kelvin}K.")
    elif unit == "F":
        celsius = fahrenheit_to_celsius(temp_value)
        kelvin = fahrenheit_to_kelvin(temp_value)
        print(f"{temp_value}°F is {celsius}°C and {kelvin}K.")
    elif unit == "K":
        celsius = kelvin_to_celsius(temp_value)
        fahrenheit = kelvin_to_fahrenheit(temp_value)
        print(f"{temp_value}K is {celsius}°C and {fahrenheit}°F.")
    else:
        print("Invalid unit entered. Please enter C, F, or K.")

if __name__ == "__main__":
    convert_temperature()