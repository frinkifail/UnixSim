import time, rec, os

echo = True
serverName = "not started"
serverPort = "not started"
setup_done = None

try:
    os.system("C:")
    os.system("cd PythonUnixSim/UnixSim32")
    setup_done = True
except:
    setup_done = False


def command_line(commandLine):
    if commandLine == "exit":
        exit()
    elif commandLine == "about":
        print("UnixSim v0.2.1-nightly\nMade by Frinkifail & contributors")
    elif commandLine == "help":
        # here we create dict with all command to sort them alphabetically
        commands_list = {
            "about": "about UnixSim",
            "exit": "exit UnixSim",
            "help": "this command",
            "echo": "print text into console",
            "echoOff & echoOn": 'turn "echo:" prompt off/on',
            "rec create": "create recording",
            "rec view [names|contents]": "view names/contents of recordings",
            "ls/dir": "list files of directory (C:/PythonUnixSim/UnixSim32)",
            "cd <directory name>": "cycles through directories (C:/PythonUnixSim/UnixSim32)",
            "server": '"server help" for more info',
            "joke": "tells unfunny joke",
            "nuclear codes": "gets goverment nuclear codes",
            "credits": "shows list of contributors",
        }

        # find longest key to format properly
        saved = 0
        for i in commands_list.keys():
            if len(i) > saved:
                saved = len(i)
        saved += 3

        commands_strings = []
        for a, b in commands_list.items():
            commands_strings.append(a + " " * (saved - len(a)) + b)

        commands_strings.sort()

        print("Available commands are:\n\n" + "\n\n".join(commands_strings) + "\n")
    elif commandLine == "echo":
        echoInput = ""
        if echo:
            echoInput = "echo:\n"
        print(input(echoInput))
    elif commandLine.startswith("echo "):
        print(commandLine[5:])
    elif commandLine == "echoOff":
        echo = False
    elif commandLine == "echoOn":
        echo = True
    elif commandLine == "nuclear codes":
        # use pomf.lain.la for faster loading (and to get 69 line number)
        os.system("start https://pomf2.lain.la/f/9m0dp3yj.mp4")  # nice
        print("Loading nuclear codes...")
        time.sleep(10)
        for _ in range(0, 1000):
            print("NEVER GONNA GIVE YOU UP")
        exit()
    elif commandLine == "rec create":
        recName_ = input("Enter Rec Name: ")
        rec.createRec(None, recName_)
    elif commandLine.startswith("rec create"):
        rec.createRec(None, commandLine[11:])
    elif commandLine == "rec view names":
        rec.viewRecContent("name")
    elif commandLine == "rec view contents":
        rec.viewRecContent("content")
    elif commandLine == "ls" or commandLine == "dir":
        if setup_done == True:
            os.system("C:")
            os.system("cd PythonUnixSim/UnixSim32")
            os.system("dir")
        elif setup_done == False:
            print("run 'setup' command to show directory")
    elif commandLine == "cd sys":
        if setup_done == True:
            os.system("cd sys")
        elif setup_done == False:
            print("run 'setup' command to change directory")
    elif commandLine == "cd .":
        os.system("cd .")
        os.system("dir")
    elif commandLine == "cd ..":
        os.system("cd ..")
        os.system("dir")
    elif commandLine.startswith("mkdir ") or commandLine.startswith("md "):
        if setup_done == True:
            try:
                os.system("C:")
                os.system("cd PythonUnixSim/UnixSim32")
                os.system("mkdir " + str(commandLine[7:]))
            except Exception as e:
                print("An error occured while making this directory")
                print("Error Code:", e)
        elif setup_done == False:
            print("run 'setup' command to make directory")
    elif commandLine == "setup":
        os.system("C:")
        os.system("mkdir PythonUnixSim")
        os.system("cd PythonUnixSim")
        os.system("mkdir UnixSim32")
        os.system("cd UnixSim32")
        os.system("mkdir sys")
        print("Please put the files in assets/ to UnixSim32/")
    elif commandLine == "server help":
        print("Simulates a server")
        print("server start - Starts a fake server")
        print("server stop - Stops a fake server")
        print("server help - this page")
        print("test server start - starts a wip server")
    elif commandLine == "credits":
        print(
            'Frinkifail "unavailable-sudo" - Owner: https://youtube.com/c/UCsZztuT8RugSO13PT-N9g8w'
        )
        print('Milenakos "milena-kos" - Contributor: https://youtube.com/c/Milenakos')
    elif commandLine == "joke":
        try:
            import requests

            response = requests.get("https://v2.jokeapi.dev/joke/Any")
            joke = response.json()
            if joke["type"] == "twopart":
                print(joke["setup"])
                time.sleep(3)
                print(joke["delivery"])
            elif joke["type"] == "single":
                print(joke["joke"])
        except:
            print("Jokes api got an error, please try again later.")
    elif commandLine == "server start":
        serverName = input("Enter server name: ")
        serverPort = input("Enter server port: ")
        print("Now hosting server:", serverName, "\nOn port:", serverPort)
    elif commandLine == "server stop":
        serverNameStop = input("Enter server name: ")
        serverPortStop = input("Enter server port: ")
        if serverNameStop == serverName and serverPortStop == serverPort:
            print("closing server...")
            time.sleep(2.5)
        else:
            print("cannot find entered server (name or port did not match)")
    elif commandLine == "test server start":
        os.system("cd C:")
        os.system("mkdir PythonUnixSim")
        os.system("cd PythonUnixSim")
        os.system("mkdir HTTPServer")
        os.system("cd HTTPServer")
        os.system("python3 -m http.server 1275")
        print(r"Server Started in C:\PythonUnixSim\HTTPServer on localhost:1275")
        print("you can put anything there (e.g. HTML Files)")
    else:
        print("Unknown Command:", commandLine)


def main():
    while True:
        commandLine = input("python/unixSim> ")
        command_line(commandLine)


if __name__ == "__main__":
    main()
