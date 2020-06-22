"""
Write a program which prompts the user for a Celsius tem-
perature, convert the temperature to Fahrenheit, and print out the
converted temperature.
"""
celTemp = input("Enter the Celsius temperature: ")
celTemp = float(celTemp)

#calculation of Fahrenheit.

fortemp = (celTemp*9/5)+32

print('Temperature to Fahrenheit is :',fortemp)
