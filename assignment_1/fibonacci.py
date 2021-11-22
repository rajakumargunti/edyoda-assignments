"""
    Write a Python program to get the Fibonacci series between 0 to 50
    Note : 
        The Fibonacci Sequence is the series of numbers :
        0, 1, 1, 2, 3, 5, 8, 13, 21, ....
        
        Every next number is found by adding up the two numbers before it.

        Expected Output :
            1 1 2 3 5 8 13 21 34

    @Author: Rajakumar Gunti
    @Date: Nov 19, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1784/?type=assignment
"""
number1, number2, temp_number = 1, 1, 0

print("Output : ")
for i in range(0, 15):
    if number1 > 50:
        break
    print(number1, end = ' ')
    temp_number =  number1 + number2
    number1 = number2
    number2 = temp_number

print("\n")