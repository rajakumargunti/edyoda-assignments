"""
    Write a Python program to count the number of even and odd numbers
    from a series of numbers.
        Sample numbers : 
            numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
        
        Expected Output :
            Number of even numbers : 4
            Number of odd numbers : 5

    @Author: Rajakumar Gunti
    @Date: Nov 19, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1784/?type=assignment
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
print("Given numbers : ", numbers)
even_count = 0
odd_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers : ", even_count) 
print("Number of odd numbers : ", odd_count) 

