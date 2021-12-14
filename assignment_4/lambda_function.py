"""
    # Play with Lambda
    Write a Python program to create a lambda function that adds 25 to 
    a given number passed in as an argument.

    Sample input:
        10
    
    Sample output:
        35   

    @Author: Rajakumar Gunti
    @Date: Dec 13, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1787/?type=assignment
"""
given_number = 10
print(given_number)

excepted_result = lambda x, y : x + y
print(excepted_result(given_number, 25))
