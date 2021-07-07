import pandas as pd
import os
import sys

path = os.path.join(sys.path[0], "rooms.csv")
def addData(newData):
    data = pd.DataFrame(newData)
    data.to_csv(path, mode='a', encoding ='utf-8',index=False, header=False)

def getLenght():
    df = pd.read_csv(path)
    lenght = len(df)
    return lenght

def getInfo():
    df = pd.read_csv(path, converters={'passcode': lambda x: str(x)})
    room_name, roomcode, passcode, username, time= df["room_name"],df['roomcode'],df['passcode'],df['username'],df['time']
    return room_name, roomcode, passcode, username, time
