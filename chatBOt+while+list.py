from datetime import datetime
import webbrowser
import os,glob
helloList=["hello","hi","hey"]
byeList = ["bye","see you later"]
dateIntent=["date","show me date","date please"]
timeIntent=["time","show me time","time please"]
musicIntent = ["music","play music"]
chat = True
while chat:
    msg = input("Enter Message").lower()
    if msg in helloList:
        print("Hello Sir...")
    elif msg in dateIntent:
        dt = datetime.now()
        print(dt.strftime("%d/%m/%y,%a"))

    elif msg in dateIntent:
        dt = datetime.now()
        print(dt.strftime("%H/%M/%S,%p"))

    elif msg.startswith("open"):
        msg=msg.split()[-1]+".com"
        webbrowser.open(msg)

    elif msg in musicIntent:
        os.chdir(r"C:\Users\sahil\Downloads")#change directory
        dataList=glob.glob("*.mp3")
        print("*******PlayList*******")
        for i in range(len(dataList)):
            print(f"{i}---> {dataList[i]}")
        choice = int(input("enter choice :"))
        os.startfile(dataList[choice])



    elif msg in byeList:
        print("Good Bye...")
        chat =False
