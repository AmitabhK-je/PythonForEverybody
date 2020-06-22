"""
Write a program to prompt the user for hours and rate per
hour to compute gross pay.
"""
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

#change the value of hours & rates to float beacuse input function returns the stringvalue.
hours = float(hours)
rate = float(rate)

#calculate pay.
pay = hours*rate
print('Pay:',pay)
