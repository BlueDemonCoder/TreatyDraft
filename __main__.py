from TreatyGui import *
##from TreatyMSG import *
##from TreatyTreatLogic import *
##from TreatyScan import *

#current treat time 0 everyday
currTT = 0

#Runs Treaty GUI
makeWindows()
x = Petname.get()
print(x)



treatDispensed = "{petname} has been given a treat at {datetime.datetime.now()}."
warning = "WARNING\nYou are low on treats. {petname} is waiting for some treats!"

#After GUI is run, set scan to run every {x} amount of time
while True:
    flag = scanPet()
    #rest state for x amount of time after scanning
    
#if scan detects movement --> TreatyTreatLogic will be notified, if within time --> give treat
if flag:
     check,currTT = treatLimit(currTT,HoursPerDisp)
     if check:
         option = dispenseTreat(TreatAmount,TreatsPerDisp,petname)
         if option:
             sendMSG(number,treatDispensed)
         else:
             sendMSG(number, warning)
#if treat given --> msg owner


