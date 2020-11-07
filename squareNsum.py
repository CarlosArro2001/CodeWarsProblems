'''
Question:
Complete the square sum function so that it squares each 
number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 
because 1^2 + 2^2 + 2^2 = 9.

Author : Carlos Raniel Arro

'''

# numbers to be pass

num = [1, 2, 2]
sum = 0


def CompleteSquareSum():
    x = 0
    for i in num:
        y = i ** 2
        x += y
        i += 1
    print(x)


CompleteSquareSum()
