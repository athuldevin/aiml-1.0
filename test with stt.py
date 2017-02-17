
import aiml
import sys
import pyttsx
import speech_recognition as sr

# Create a Kernel object.
kern = aiml.Kernel()
engine = pyttsx.init()
r = sr.Recognizer()
#r.pause_threshold = 4
IBM_USERNAME = "ca5c2b4a-90d6-4d37-b1af-f71eeeec5f9f"
WIT_AI_KEY = "K2UTALSITGNGNI6WTYTQJS4HJU7QXCWO"
IBM_PASSWORD = "CvJLlIgU5GiP"
voice="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice)
    
# When loading an AIML set, you have two options: load the original
# AIML files, or load a precompiled "brain" that was created from a
# previous run. If no brain file is available, we force a reload of
# the AIML files.
brainLoaded = False
forceReload = False
while not brainLoaded:
        if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
                # Use the Kernel's bootstrap() method to initialize the Kernel. The
                # optional learnFiles argument is a file (or list of files) to load.
                # The optional commands argument is a command (or list of commands)
                # to run after the files are loaded.
                kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
                brainLoaded = True
                # Now that we've loaded the brain, save it to speed things up for
                # next time.
                kern.saveBrain("angel.brn")
        else:
                # Attempt to load the brain file.  If it fails, fall back on the Reload
                # method.
                try:
                        # The optional branFile argument specifies a brain file to load.
                        kern.bootstrap(brainFile = "angel.brn")
                        brainLoaded = True
                except:
                        forceReload = True

# Enter the main input/output loop.
print("\nINTERACTIVE MODE (ctrl-c to exit)")
print("press enter key to start listening")
while(True):
        k=raw_input()
        with sr.Microphone() as source:
                #r.adjust_for_ambient_noise(source,duration = 1)
                print("Me>>> listening...")
                audio = r.listen(source)
                print ("     done...")
        try:
                inpt=r.recognize_google(audio)
        except sr.UnknownValueError:
                inpt="hgdjskxzxz"
        except sr.RequestError as e:
                try:
                        inpt=r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
                except sr.UnknownValueError:
                        inpt=("asdfghjk")
                except sr.RequestError as e:
                        try:
                                inpt=r.recognize_wit(audio, key=WIT_AI_KEY)
                        except sr.UnknownValueError:
                                inpt="kdsijfidf"
                        except sr.RequestError as e:
                                try:
                                        inpt=r.recognize_sphinx(audio)
                                except sr.UnknownValueError:
                                        inpt="kdsijfidf"
                                except sr.RequestError as e:
                                        inpt="kdsijfidf"
        #inpt = raw_input("DEVIN>>> ")
        print inpt
        out=kern.respond(inpt)
        print"ANGEL>>>",out
        engine.say(out)
        engine.runAndWait()
        
