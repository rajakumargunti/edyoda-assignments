"""
    Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
    from a given list of non-empty tuples
    
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    
    @Author: Rajakumar Gunti
    @Date: Dec 2, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1785/?type=assignment
"""

given_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]  # given list
# Way 1
second_ele_list = []
for i in given_list:
    second_ele_list.append(i[1])

second_ele_list.sort() 

sorted_list = []
for i in range(len(second_ele_list)):
    for j in  range(len(given_list)):
        if second_ele_list[i] == given_list[j][1]:
            element = second_ele_list.index(second_ele_list[i])
            sorted_list.insert(element, given_list[j])

print(sorted_list)

# Way 2
def second_element(element):
    return element[1]

sorted_list = sorted(given_list, key=second_element)
print(sorted_list)