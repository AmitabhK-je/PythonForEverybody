"""
Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
"""
#initialize the variable for count and sum.
count = 0
sum = 0
#iteration with whil loop to ask user to enter the value till 'done'.
while True:
    #try and except used to get the int value in command prompt.
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        num = int(num)

    except:
        print('Invalid input')
        continue
    # get count in every iteration.
    count = count + 1
    #get sum for every iteration.
    sum = sum + num
#get average between total sum and total count.
average = sum/count
# print total values for sum,count,average.
print(sum,count,average)
