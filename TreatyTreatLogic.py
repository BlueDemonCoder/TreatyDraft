from TreatyMSG import *
import datetime

def dispenseTreat(x,y,petname):
    warning = f'{petName} is waiting for a treat. Please buy more treats!'
    treatCount = x
    treatsToDispense = y
    if x > y:
        print("Treat within limits")
        #drop y treats
        "-------INSERT SERVO MOTOR FUNCTION HERE-----------"
        ##LastTreat = Current time given a treat
        return True
    else:
        return False

def saveLog():
    'after dispense treat is run, save a log using date and time showing when the treat was given to the pet'
     #could also use SENDMSG function with the log at the end of the day
    SENDMSG(number, information)

def treatLimit(LastTreat,limit):
    'flag for treat'
    if LastTreat == 0:
        currentTime = datetime.datetime.now()
        currentTime = int(currentTime.strftime("%H"))
        if currentTime - LastTreat > limit:
            LastTreat = currentTime
            return True, LastTreat
