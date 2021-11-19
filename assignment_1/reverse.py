"""
    Write a Python program that accepts a word from the user and reverse it.
        Sample Test Case
        Input :
            Edyoda
        Output:
            adoydE

    @Author: Rajakumar Gunti
    @Date: Nov 19, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1784/?type=assignment
"""
input_str = "Edyoda"  #input string 
print("The given string : ", input_str)
output_str = "";

for i in input_str:
    output_str = i + output_str

print("Reverse of a given string : ", output_str) # it will print the output like "adoydE"
