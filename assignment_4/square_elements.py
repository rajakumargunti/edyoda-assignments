"""
    # Find the Squares from the given List
    Write a Python program to square the elements of a list using map() function.
    
    Sample List:  
        [4, 5, 2, 9]
    
    Square the elements of the list:
        [16, 25, 4, 81]

    @Author: Rajakumar Gunti
    @Date: Dec 13, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1787/?type=assignment
"""
given_list = [4, 5, 2, 9]
print(given_list)

excepted_list = map(lambda x: x * x, given_list)
print(list(excepted_list))
