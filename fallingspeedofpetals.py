'''
When it's spring Japanese cherries blossom,
it's called "sakura" and it's admired a lot.
 The petals start to fall in late April.

Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s),
and it takes 80 seconds for the petal to reach the ground from a certain branch.

Write a function that receives the speed (in cm/s) of a petal as input,
and returns the time it takes for that petal to reach the ground from 
the same branch.

Notes:

The movement of the petal is quite complicated, so in this case 
we can see the velocity as a constant during its falling.
Pay attention to the data types.
If the initial velocity is non-positive, the return value should be 0  

Author: Carlos Raniel Ariate Arro
'''


'''
Falling speed =  5cm/s
Time taken for petal to reach ground = 80 seconds
therefore according to distance = speed * time 
distance = 80 * 5 
distance = 400 
thus dividing 400 by speed (perhaps call it velocity since it's direction is to the ground) 
and then returning that value as the time.
function :
    - recieves speed as input (in cm/s)
    - returns time taken for petal to reach ground from same branch

'''

def PetalReachGround():
    speed = int(input("Enter a speed : "))
    #calculating time taken for petal to reach ground from the same branch
    #speed * distance = time 
    if speed<= 0:  
        return 0 
    else:
        time = 400 / speed
        print(time)
        return time 
    '''time = speed * 400
    if(speed < 0 ):
        time <= 0 
        
    return time 
    '''
PetalReachGround()


