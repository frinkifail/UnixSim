# import time
import rec
echo = True

while True:
    commandLinePrompt = "python/unixSim> "
    user_command = input(commandLinePrompt)
    if user_command == "exit":
        exit()
    elif user_command == "about":
        print("UnixSim v0.1.8-nightly\nMade by Frinkifail & contributors")
    elif user_command == "help":
        print("Avalible commands are:\nabout - about\nexit - exit\nhelp - help\necho - say word\nechoOff & echoOn - turn \"echo:\" prompt off/on\nrec create - create rec\nrec view names - view names of recs\nrec view contents - view contents of recs")
        print("ls/dir - list fake (simulated) directory\ncd <directory name>- cycles through simulated directories")
        print("self-explainatory")
    elif user_command == "echo":
        if echo is True:
            echoMessage = input("echo:\n")
            print(echoMessage)
        elif echo is False:
            echoMessage = input("")
            print(echoMessage)
    elif user_command.startswith("echo "):
        print(user_command[5:])
    elif user_command == "echoOff":
        echo = False
    elif user_command == "echoOn":
        echo = True
    elif user_command == "" or user_command == " ":
        pass
    elif user_command == "rec create":
        recName_ = input("Enter Rec Name: ")
        rec.createRec(None, recName_)
    elif user_command.startswith("rec create"):
        rec.createRec(None, user_command[11:])
    elif user_command == "rec view names":
        rec.viewRecContent('name')
    elif user_command == "rec view contents":
        rec.viewRecContent('content')
    elif user_command == "test ctc":
        # !CATECOIN LIBRARY #HERE
        pass
    elif user_command == "ls" or user_command == "dir":
        print("DIRECTORY LIST:\nsys [system, dir]\nntpd.exe [app]\nwrdpd.exe [app]\nspaint.exe [sandbox, app]\n. [CURR DIR, system] (UnixSim32)\n.. [PREV DIR, system_const_protected] (???)")
    elif user_command == "cd sys":
        print("this is a system directory it is not safe to play around!")
    elif user_command == "cd .":
        pass
    elif user_command == "cd ..":
        print("system cannot find target")
    else:
        print("Unknown Command:", user_command)
