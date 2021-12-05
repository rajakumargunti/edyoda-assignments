"""
    # Game of "Functions"

    Write a Python function to sum all the numbers in a list.
    
    Sample List :
        (8, 2, 3, 0, 7)
    
    Expected Output :
        20

    Explanation:
    Summation should like 8+2+3+0+7 = 20
    
    @Author: Rajakumar Gunti
    @Date: Dec 5, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1786/?type=assignment
"""
sample_list = (8, 2, 3, 0, 7)

# Way 1
def sum_of_list(list):
    ' This is function will calucate the sum of all the numbers in a list '
    sum = 0
    for i in list:
        sum += i
    print(sum)

sum_of_list(sample_list)

# Way 2
sum = 0
def sum_of_list_2(list):
    ' This is function will calucate the sum of all the numbers in a list '
    for i in list:
        global sum
        sum += i

sum_of_list_2(sample_list)
print(sum)

# Way 3
def sum_of_list_3(*arg):
    sum = 0
    for i in arg:
        sum += i
    print(sum)

sum_of_list_3(*sample_list);
