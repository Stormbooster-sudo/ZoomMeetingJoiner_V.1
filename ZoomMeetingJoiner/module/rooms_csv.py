import pandas as pd
import os
import sys

#Direct to file more percisely.
path = os.path.join(sys.path[0], "rooms.csv")

def addData(newData):
    df = pd.read_csv(path)
    data = pd.DataFrame(newData)
    data.to_csv(path, mode='a', encoding ='utf-8',index=False, header=False)
    print(df)

def deleteRow(i):
    df = pd.read_csv(path)
    df.drop(i,axis = 0, inplace=True)
    df.to_csv(path,index = False)
    print(df)

def updateData(i,data):
    df = pd.read_csv(path)
    df.loc[i] = data
    df.to_csv(path,encoding ='utf-8',index=False)

def getLenght():
    df = pd.read_csv(path)
    lenght = len(df)
    return lenght

def getInfo():
    df = pd.read_csv(path,dtype=str)
    room_name, roomcode, passcode, username, time= df["room_name"],df['roomcode'],df['passcode'],df['username'],df['time']
    return room_name, roomcode, passcode, username, time