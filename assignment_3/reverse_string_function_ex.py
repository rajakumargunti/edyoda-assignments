"""
    # String inside the function
    
    Write a Python program to reverse a string.

    Sample String :
        "1234abcd"

    Expected Output : 
        "dcba4321"
    
    @Author: Rajakumar Gunti
    @Date: Dec 5, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1786/?type=assignment
"""
sample_string = "1234abcd"

# Way 1
def reverse_a_string(value):
    ' This is function will convert given string to reverse a string '
    reverse = ""
    for i in value:
        reverse = i + reverse
    print(reverse)

reverse_a_string(sample_string)

# Way 2
def reverse_a_string_2(value):
    ' This is function will convert given string to reverse a string '
    print(value[::-1])

reverse_a_string_2(sample_string)

# Way 3
def reverse_a_string_3(value):
    ' This is function will return reverse a string '
    return value[::-1]

print(reverse_a_string_3(sample_string))
