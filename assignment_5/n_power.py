"""
    # Create You own built-in class method
    Write a Python class to implement pow(x, n)

    Explanation:
    Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)

    You must implement it using Class

    Sample Input:
        x: 10
        n: 2

    Sample Output:
        100

    @Author: Rajakumar Gunti
    @Date: Dec 20, 2021
    @Links: https://classroom.edyoda.com/program-modules/DS291021/Python/1788
"""
class power:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def pow(self):
        
        if self.x == 0 or self.x == 1 or self.n == 1:
            return self.x
        
        if self.n == 0:
            return 1
        
        return self.x ** self.n

result = power(0, 1)
print(result.pow())

result = power(1, 2)
print(result.pow())

result = power(100, 1)
print(result.pow())

result = power(100, 0)
print(result.pow())

result = power(2, 3)
print(result.pow())
