import time
import rec
echo = True
serverName = "not started"
serverPort = "not started"

def command_line():
    commandLinePrompt = "python/unixSim> "
    commandLine = input(commandLinePrompt)
    if commandLine == "exit":
        exit()
    elif commandLine == "about":
        print("UnixSim v0.1.8-nightly\nMade by Frinkifail & contributors")
    elif commandLine == "help":
        print("Avalible commands are:\nabout - about\nexit - exit\nhelp - help\necho - say word\nechoOff & echoOn - turn \"echo:\" prompt off/on\nrec create - create rec\nrec view names - view names of recs\nrec view contents - view contents of recs")
        print("ls/dir - list fake (simulated) directory\ncd <directory name>- cycles through simulated directories\nserver - \"server help\" for more info")
    elif commandLine == "echo":
        if echo is True:
            echoMessage = input("echo:\n")
            print(echoMessage)
        elif echo is False:
            echoMessage = input("")
            print(echoMessage)
    elif commandLine.startswith("echo "):
        print(commandLine[5:])
    elif commandLine == "echoOff":
        echo = False
    elif commandLine == "echoOn":
        echo = True
    elif commandLine == "":
        pass
    elif commandLine == "rec create":
        recName_ = input("Enter Rec Name: ")
        rec.createRec(None, recName_)
    elif commandLine.startswith("rec create"):
        rec.createRec(None, commandLine[11:])
    elif commandLine == "rec view names":
        rec.viewRecContent('name')
    elif commandLine == "rec view contents":
        rec.viewRecContent('content')
    elif commandLine == "test ctc":
        # CATECOIN LIBRARY HERE
        pass
    elif commandLine == "ls" or commandLine == "dir":
        print("DIRECTORY LIST:\nsys [system, dir]\nntpd.exe [app]\nwrdpd.exe [app]\nspaint.exe [sandbox, app]\n. [CURR DIR, system] (UnixSim32)\n.. [PREV DIR, system_const_protected] (???)")
    elif commandLine == "cd sys":
        print("this is a system directory it is not safe to play around!")
    elif commandLine == "cd .":
        pass
    elif commandLine == "cd ..":
        print("system cannot find target")
    elif commandLine == "mkdir":
        print("indevelopment kik")
    elif commandLine == "server help":
        print("Simulates a server (fake server duh I don't know how to code)")
        print("server start - Starts a fake server")
        print("server stop - Stops a fake server")
        print("server help - this page")
    elif commandLine == "server start":
        serverName = input("Enter server name: ")
        serverPort = input("Enter server port: ")
        print("Now hosting server:", serverName,"\nOn port:", serverPort)
    elif commandLine == "server stop":
        serverNameStop = input("Enter server name: ")
        serverPortStop = input("Enter server port: ")
        if serverNameStop == serverName and serverPortStop == serverPort:
            print("closing server...")
            time.sleep(2.5)
        else:
            print("cannot find entered server (name or port did not match)")
    else:
        print("Unknown Command:", commandLine)

def main():
    while True:
        command_line()

if __name__ == "__main__":
    main()
