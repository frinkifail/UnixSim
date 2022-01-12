recNames = []
recCodeContents = []

def createRec(recType, recName):
    global recNames
    global recCodeContents
    recName_ = recName
    recNames.append(recName_)
    recCodeContent = input("New Rec File - %s (1 line limit):\n" % recName_)
    if recCodeContent == "puw oruoqeiwrunwioeu ounuwe uio ru orc uoqrweu ":
        print("funny")
    else:
        print("indevelopment kik")
    recCodeContents.append(recCodeContent)
    
def viewRecContent(recType):
    if recType == "name":
        print(recNames)
    elif recType == "content":
        print(recCodeContents)
    