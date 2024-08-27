FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def conver_to_fahrenheit(celsius):
    global fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

def main():
    temperature = input("Enter the temperature to convert: ")
    while not temperature.isdigit():
        print("Invalid temperature. Please enter a numeric value.")
        temperature = input("Enter the temperature to convert: ")
    temperature = float(temperature)
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    while type != "C" and type != "F":
        print("Invalid type. Try again")
        type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if type == "C":
        conver_to_fahrenheit(temperature)
    elif type == "F":
        convert_to_celsius(temperature)


if __name__ == "__main__":
    main()
