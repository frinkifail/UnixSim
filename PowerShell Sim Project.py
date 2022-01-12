import time
import rec
echo = True

while True:
    commandLine = input("python/unixSim> ")
    if commandLine == "exit":
        exit()
    elif commandLine == "about":
        print("UnixSim v0.0.1\nMade by Frinkifail")
    elif commandLine == "help":
        print("Avalible commands are:\nabout - about\nexit - exit\nhelp - help\necho - say word\nechoOff & echoOn - turn \"echo:\" prompt off/on\nrec create - create rec\nrec view names - view names of recs\nrec view contents - view contents of recs\nself-explainatory")
    elif commandLine == "echo":
        if echo == True:
            echoMessage = input("echo:\n")
            print(echoMessage)
        elif echo == False:
            echoMessage = input("")
            print(echoMessage)
    elif commandLine == "echoOff":
        echo = False
    elif commandLine == "echoOn":
        echo = True
    elif commandLine == "":
        pass
    elif commandLine == " ":
        pass
    elif commandLine == "rec create":
        recName_ = input("Enter Rec Name: ")
        rec.createRec(None, recName_)
    elif commandLine == "rec view names":
        rec.viewRecContent('name')
    elif commandLine == "rec view contents":
        rec.viewRecContent('content')
    elif commandLine == "test ctc":
        # !CATECOIN LIBRARY #HERE
        pass
    else:
        print("Unknown Command:", commandLine)