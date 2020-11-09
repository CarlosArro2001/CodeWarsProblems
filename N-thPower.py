'''
You are given an array with positive numbers and a number N. 
You should find the N-th power of the element in the array with the index N.
If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:

array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Author : Carlos Raniel Ariate Arro

'''


'''
BASICALLY 
I have an array 
I need to find the N-th power of the element inside the array the index as the value of the N-th power
Then the result should be : <array_element>**<value of n>
'''

def  nthPower(array,n):
    #if the length of the array is greater or equal than n , obviously index n will be there 
    if(len(array)>=n):
        result = array[n]**n
        print(result)

#array with the elements
array = [1,2,3,4]
#N-th power
n = 2 
nthPower(array,n)



