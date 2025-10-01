# function called celsius_to_fahrenheit(celsius)
# converts a temperature from Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius=0):
    cal = celsius*(9/5)+32
    return cal

temp = celsius_to_fahrenheit(14)
print("Temperature:",temp)