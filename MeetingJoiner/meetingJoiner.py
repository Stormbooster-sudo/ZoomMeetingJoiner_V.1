
from tkinter import *
from rooms_csv import *
from zoom_bot import sign_in

 
root = Tk()
root.title("Meeting Joiner")
root.geometry("520x480+100+100")
topFrame = LabelFrame(root)
topFrame.pack(fill="both", expand="yes",padx=10,pady=10)

#entry box
Label(topFrame,text="Meeting Code").grid(row = 0,column= 0,sticky = W)
Label(topFrame,text="Password").grid(row = 1,column= 0, sticky = W)
Label(topFrame,text="Room Name").grid(row = 2,column= 0, sticky = W)
Label(topFrame,text="Time").grid(row = 3,column= 0, sticky = W)
Label(topFrame,text="Username").grid(row = 4,column= 0, sticky = W)

#setting up variable
roomcode = StringVar()
passcode = StringVar()
get_roomname = StringVar()
get_username = StringVar()
get_time = StringVar()
roomcode.set("")
passcode.set("")
get_username.set("")
get_roomname.set("")
get_time.set("")

roomCode = Entry(topFrame,textvariable=roomcode)
roomCode.grid(row=0,column=1)
passCode = Entry(topFrame,textvariable=passcode)
passCode.grid(row=1,column=1,pady = 3)
roomname = Entry(topFrame,textvariable=get_roomname)
roomname.grid(row=2,column=1,pady = 3)
getTime = Entry(topFrame,textvariable=get_time)
getTime.grid(row=3,column=1,pady = 3)
username = Entry(topFrame,textvariable=get_username)
username.grid(row=4,column=1,pady = 3)

def program_ui():
    #create canvas
    frame = LabelFrame(root)
    frame.pack(fill="both", expand="yes",padx=10,pady=10)   
    mycanvas = Canvas(frame)
    mycanvas.pack(side=LEFT, fill="both", expand="yes")
    yscroll = Scrollbar(frame,orient="vertical",command=mycanvas.yview)
    yscroll.pack(side=RIGHT, fill="y")
    mycanvas.configure(yscrollcommand=yscroll.set)
    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    myframe = Frame(mycanvas,bg="white")
    mycanvas.create_window((0,0),window=myframe, anchor="nw")
    
    def addRoom():
        get_rc = roomcode.get()
        get_rc = get_rc.replace(" ","")    #Remove space in meeting id (If it has.)
        get_pc = passcode.get()
        get_rn = get_roomname.get()
        get_un = get_username.get()
        get_t = get_time.get()
        if get_rc or get_pc or get_rn or get_un or get_t != "":
            newData = {'room_name':[get_rn],'roomcode':[get_rc], 'passcode':get_pc, 'username':[get_un],'time':[get_t]}
            # print(newData)
            addData(newData)
            roomcode.set("")
            passcode.set("")
            get_username.set("")
            get_roomname.set("")
            get_time.set("")   
            frame.destroy()
        else:
            frame.destroy()
            print("Please enter your room")
        program_ui()
    Button(topFrame,text="ADD",width=10,height=1,bd = 1,command=addRoom).grid(row = 0,column = 8,sticky=E,padx = 5)
    
    rn, rc, pc, un, t = getInfo()
    def call_sign_in(i):
        print("signing in ............")
        sign_in(str(rc[i]),str(pc[i]))
        
    btn = []
    for i in range(getLenght()):
        b = Button(myframe,text=F"{rn[i]}", fg="white", bg="skyblue",font="10",bd = 0,width=42,height=5,command=lambda i = i: call_sign_in(i)).pack(pady=2)
        btn.append(b)
    

    root.resizable(False,False)
    root.mainloop()

program_ui()
