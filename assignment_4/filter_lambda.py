"""
    # Find the way with Maps
    Write a Python program to triple all numbers of a given list of integers. Use Python map.

    Sample list:
        [1, 2, 3, 4, 5, 6, 7]
    
    Triple of list numbers:
        [3, 6, 9, 12, 15, 18, 21]
    
    
    @Author: Rajakumar Gunti
    @Date: Dec 13, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1787/?type=assignment
"""
given_list = [1, 2, 3, 4, 5, 6, 7]
print(given_list)
excepted_list = map(lambda x: x + x + x, given_list)
print(list(excepted_list))