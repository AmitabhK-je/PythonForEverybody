"""
Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
"""
#Ask the user for hours and rate in the command line and store in the name variable.
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

#change the value of hours & rates to float beacuse input function returns the stringvalue.
hours = float(hours)
rate = float(rate)
if hours > 40:
    #calculate the pay which is having more than 40 hours
    exrate = (hours-40)*rate*1.5
    paym = 40 * rate
    # adding with extra rate and the payment for 40 hrs.
    pay = exrate+paym
    print('Pay:',pay)
else:
    pay = hours*rate
    print('Pay:',pay)
