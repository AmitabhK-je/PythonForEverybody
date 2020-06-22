"""
Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
"""
try:
    hours = input("Enter Hours: ")
    hours = float(hours)

    rate = input("Enter Rate: ")
    rate = float(rate)
    if hours < 0:
        print("Error, please enter numeric input")
    elif rate < 0:
        print("Error, please enter numeric input")
    elif hours > 40:
        #calculate the pay which is having more than 40 hours
        exrate = (hours-40)*rate*1.5
        paym = 40 * rate
        # adding with extra rate and the payment for 40 hrs.
        pay = exrate+paym
        print('Pay:',pay)
    else:
        pay = hours*rate
        print('Pay:',pay)
except:
    print("Error, please enter numeric input")
    exit()
