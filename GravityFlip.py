'''
Question:
Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. 
The box is special because it has the ability to change gravity.

There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. 
At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, 
it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). 
Below is an example of what a box of cubes might look like before and after switching gravity.

+---+                                       +---+
|   |                                       |   |
+---+                                       +---+
+---++---+     +---+              +---++---++---+
|   ||   |     |   |   -->        |   ||   ||   |
+---++---+     +---+              +---++---++---+
+---++---++---++---+         +---++---++---++---+
|   ||   ||   ||   |         |   ||   ||   ||   |
+---++---++---++---+         +---++---++---++---+
Given the initial configuration of the cubes in the box, 
find out how many cubes are in each of the n 
columns after Bob switches the gravity.

Examples:

flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]

Author : Carlos Raniel Ariate Arro 

'''


def flip(letter, values):
    if(letter == "R"):
        # bubble sort algorithm
        n = len(values)
        #traverse through all array elements 
        for i in range(n):
            #Last element of i is already in place 
            for j in range( 0 , n-i-1):
                #swapping if one element is greater than the other 
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1] , values[j]
        print(values) #outputting the values
    if(letter == "L"):
        # reverse the bubble sort
        n = len(values)
        for i in range(n):
            for j in range(0 , n-i-1):
                if values[j+1]>values[j]:
                    values[j+1] , values[j] = values[j] , values[j+1]
        print(values) #outputting the values 


flip('L', [1, 4, 5, 3, 5])
flip('R', [3, 2, 1, 2])
