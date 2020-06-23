"""
Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two parameters
(hours and rate).
"""
try:
    hours = input('Enter Hours: ')
    hours = float(hours)
    rate = input('Enter Rate: ')
    rate = float(rate)
    if hours<0:
        print("Error, please enter numeric input")
    elif rate <0:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")
    exit()

def computepay(hours,rate):
    if hours > 40:
        pay = (40*rate)+((hours-40)*rate*1.5)
        print('Pay:',pay)
    else:
        pay = hours * rate
        print('Pay:',pay)

computepay(hours,rate)
