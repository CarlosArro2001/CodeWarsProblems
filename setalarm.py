'''
L1:Set Alarm
Write a function named setAlarm which receives two parameters. 
The first parameter, employed, is true 
whenever you are employed and the second parameter, 
vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation 
(because these are the circumstances under which you need to set an alarm).
It should return false otherwise. Examples:

setAlarm(true, true) -> false
setAlarm(false, true) -> false
setAlarm(false, false) -> false
setAlarm(true, false) -> true
'''

#function called setAlarm
def setAlarm(employed,vacation):
    #simple if statement 
    if (employed == True and vacation == False) or (employed == False and vacation == True):
         return True
         #print(True) 
    else:
        return False
        #print(False)

#Parameters that would return to True
setAlarm(True,False)
setAlarm(False,True)
#Parameters that would return to False
setAlarm(False,False)
setAlarm(True,True)
