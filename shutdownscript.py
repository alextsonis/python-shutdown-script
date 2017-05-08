import datetime
import os
import time
import platform


#          _      _      _
#        >(.)__ <(.)__ =(.)__
#         (   /  (   /  (   / 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Get system platform and check for necessary permissions
machine=platform.system()
print "Platform is: ",machine,"\n"
if (machine=='Windows'):
    print "Windows detected - Proceed with Execution\n"
elif (machine=='Linux'):
    if not os.geteuid() == 0:#Check for root permission
        print "Script must be run as root (e.g. sudo python shutdownscript.py)"
        em=raw_input("Press the Enter key to exit...")
        exit()
    else:
        print "Linux detected - Executed as root - Proceed with Execution\n"
elif (machine==''):#Unknown OS, unknown commands
    print "OS could not be detected-Aborting"
    exit()

#Get the time in minutes
print "How many minutes do you want to wait before shutdown\n"
mins=int(input())
while (mins<=0):
    print "Input a valid time (Must be greater than 0)\n"
    mins=int(input())

startingtime=datetime.datetime.now()
deltatime=datetime.timedelta(minutes=mins)
endtime=startingtime+deltatime

print "System going down at "+str(endtime)
print "Press Ctrl+C to cancel"

mins=mins-1
deltatime=datetime.timedelta(minutes=mins)
endtime=startingtime+deltatime

#Wait for the time to pass
try:
    while (datetime.datetime.now()<endtime):
        time.sleep(1)
except KeyboardInterrupt:
    print "Keyboard Interupt -- Canceling"
    exit()

#Execute shutdown command and warn for last time
try:   
    if (machine=='Windows'):
        os.system('shutdown /s /t 60 -c "Planned shutdown of system in one minute"')
    elif (machine=='Linux'):
        os.system('shutdown +1 "Planned shutdown of system in one minute"')
    print "Shutdown sequence is initiated - 45 seconds left to cancel."
    print "Do not close this window if you want to cancel - Just press Ctrl+C."
    if (machine=='Windows'):
        print "If you close this window, open a cmd prompt (win+x)\nand type \"shutdown /a\""
    elif (machine=='Linux'):
        print "If you close this window, open the terminal (Ctrl+Alt+T)\nand type \"sudo shutdown -c\""
    startingtime=datetime.datetime.now()
    deltatime=datetime.timedelta(seconds=45)
    endtime=startingtime+deltatime
    while (datetime.datetime.now()<endtime):
        time.sleep(1)
        
except KeyboardInterrupt:
    print "Keyboard Interupt -- Canceling"
    if (machine=='Windows'):
        os.system('shutdown /a -c "Planned shutdown cancelled"')
    elif (machine=='Linux'):
        os.system('shutdown -c "Planned shutdown cancelled"')
    exit()

exit()
