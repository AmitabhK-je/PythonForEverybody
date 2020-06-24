"""
Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""
#initialize the variable for count ,sum ,smallest ,largest.
count = 0
sum = 0
smallest = None
largest = None
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
    # to get largest num
    if largest is None or largest<num:
        largest = num
   # to get smallest num
    if smallest is None or smallest>num:
        smallest = num
print(sum,count,smallest,largest)
