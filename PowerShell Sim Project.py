# import time
import rec
echo = True

while True:
    commandLinePrompt = "python/unixSim> "
    commandLine = input(commandLinePrompt)
    if commandLine == "exit":
        exit()
    elif commandLine == "about":
        print("UnixSim v0.1.7-nightly\nMade by Frinkifail")
    elif commandLine == "help":
        print("Avalible commands are:\nabout - about\nexit - exit\nhelp - help\necho - say word\nechoOff & echoOn - turn \"echo:\" prompt off/on\nrec create - create rec\nrec view names - view names of recs\nrec view contents - view contents of recs")
        print("ls/dir - list fake directory (simulated directory)\ncd <directory name>- cycles through simulated directories")
        print("self-explainatory")
    elif commandLine == "echo":
        if echo is True:
            echoMessage = input("echo:\n")
            print(echoMessage)
        elif echo is False:
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
    elif commandLine == "ls":
        print("DIRECTORY LIST:\nsys [system, dir]\nntpd.exe [app]\nwrdpd.exe [app]\nspaint.exe [sandbox, app]\n. [CURR DIR, system] (UnixSim32)\n.. [PREV DIR, system_const_protected] (???)")
    elif commandLine == "dir":
        print("DIRECTORY LIST:\nsys [system, dir]\nntpd.exe [app]\nwrdpd.exe [app]\nspaint.exe [sandbox, app]\n. [CURR DIR, system] (UnixSim32)\n.. [PREV DIR, system_const_protected] (???)")
    elif commandLine == "cd sys":
        print("this is a system directory it is not safe to play around!")
    elif commandLine == "cd .":
        pass
    elif commandLine == "cd ..":
        print("system cannot find target")
    else:
        print("Unknown Command:", commandLine)
