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
		print("UnixSim v0.1.9-nightly\nMade by Frinkifail & contributors")
	elif commandLine == "help":
		# here we create dict with all command to sort them alphabetically
		commands_list = {"about": "about UnixSim", "exit": "exit UnixSim", "help": "this command", "echo": "print text into console", "echoOff & echoOn": "turn \"echo:\" prompt off/on",
		"rec create": "create recording", "rec view [names|contents]": "view names/contents of recordings", "ls/dir": "list files of fake (simulated) directory",
		"cd <directory name>": "cycles through simulated directories", "server": "\"server help\" for more info", "joke": "tells unfunny joke"}

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

		print("Avalible commands are:\n\n" + "\n\n".join(commands_strings) + "\n")
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

