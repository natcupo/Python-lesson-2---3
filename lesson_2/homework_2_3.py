# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

print('Hello this is my first program. It will convert Fahrenheit into Celsius')
temperature = input("What is your current temperature in celsius")
temperature_fahrenheit = '78'
result_temperature = (int(temperature_fahrenheit) - 32) * 5/9
result_temperature_celsius = round(result_temperature, 0)
print(result_temperature_celsius)
print(f'Well, celsius temperature for 78 degrees is {result_temperature_celsius}')
