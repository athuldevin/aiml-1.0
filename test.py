
import aiml
import sys


kern = aiml.Kernel()


kern._addSession("athuldevin")
sessionID="athuldevin"
brainLoaded = False
forceReload = False
while not brainLoaded:
        if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
                kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
                brainLoaded = True
                kern.saveBrain("angel.brn")
        else:
                try:
                        kern.bootstrap(brainFile = "angel.brn")
                        brainLoaded = True
                except:
                        forceReload = True

print("\nINTERACTIVE MODE (ctrl-c to exit)")
kern.restoreSessionData("angel.dat",sessionID)
while(True):
        inpt = raw_input("ME>>> ")
        print
        kern.saveSessionData("angel.dat",sessionID)
        #try:
        out=kern.respond(inpt,sessionID)
        #except:
        #        out="oops, something went wrong.Try reload me."
        print"ANGEL>>>",out
        
        print
