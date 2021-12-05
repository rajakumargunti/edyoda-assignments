"""
    # Calculate the Upper and The lower Case
    
    Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

    Sample String : 
        'The quick Brow Fox'

    Expected Output :
        No. of Upper case characters : 3
        No. of Lower case Characters : 12
    
    @Author: Rajakumar Gunti
    @Date: Dec 5, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1786/?type=assignment
"""

sample_string = 'The quick Brow Fox'
# Way 1
def calculate_char_count(value):
    """ 
        This is function will calucate the
        No. of Upper case characters
        No. of Lower case Characters
    """
    upper_count = 0
    lower_cout = 0
    for i in value:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_cout += 1
        else:
            pass
    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_cout}")

calculate_char_count(sample_string)

# Way 2
count_dict = {
    "upper_count" : 0,
    "lower_cout" : 0
}

def calculate_char_count_2(value):
    """ 
        This is function will calucate the
        No. of Upper case characters
        No. of Lower case Characters
    """
    global count_dict
    for i in value:
        if i.isupper():
            count_dict["upper_count"] += 1
        elif i.islower():
            count_dict["lower_cout"] += 1
        else:
            pass

calculate_char_count_2(sample_string)

print(f'No. of Upper case characters : {count_dict["upper_count"]}')
print(f'No. of Lower case Characters : {count_dict["lower_cout"]}')
