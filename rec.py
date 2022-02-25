# This file contains utility functinos for reading and creating recs.

recNames = []
recCodeContents = []


def createRec(recLinesINDEV, recName):
    global recNames
    global recCodeContents
    recName_ = recName
    recNames.append(recName_)
    recCodeContent = input("New Rec File - %s (1 line limit):\n" % recName_)
    print("indevelopment kekw")
    recCodeContents.append(recCodeContent)


def viewRecContent(recType):
    if recType == "name":
        print(recNames)
    elif recType == "content":
        print(recCodeContents)
