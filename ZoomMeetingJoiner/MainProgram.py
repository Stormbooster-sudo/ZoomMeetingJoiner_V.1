
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from module.rooms_csv import *
from module.zoom_bot import sign_in
import os
import sys


path_file = open("zoom_path.txt"),'r+')
path = path_file.readline()
#Direct the path.
if path == "":
    pathWin = Tk()
    pathWin.title('File Explorer')
    pathWin.geometry("400x200+150+100")
    def browseFiles():
        def confirm():
            path_file.write(filename)
            print(path_file.readline()) 
            path_file.truncate()
            path_file.close()
            pathWin.destroy()
        #Explore the file
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Zoom","*.exe*"),("all files","*.*")))
        label_file_explorer.configure(text="Done!")
        Button(pathWin,text="Okay",command=confirm).place(x = 175,y = 150)
    label_file_explorer = Label(pathWin,text = "Path your zoom launcher.",font = ("",15))
    label_file_explorer.pack(pady=40)
    Button(pathWin,text = "Browse Files",command = browseFiles).place(x = 150,y = 100)
    pathWin.resizable(False,False)
    #Destroy all window, force user to direct the zoom launcher path.
    def close_window():
        root.destroy()
        pathWin.destroy()
    pathWin.protocol("WM_DELETE_WINDOW", close_window)


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
            messagebox.showerror("ERROR", "Please enter your room infomation.")
        program_ui()
    Button(topFrame,text="ADD",width=10,height=1,bd = 1,command=addRoom).grid(row = 0,column = 8,sticky=E,padx = 5)
    
    rn, rc, pc, un, t = getInfo()
    def roomWin(i):
        room_win = Toplevel(root)
        room_win.wm_title(rn[i])
        room_win.geometry("400x200+"+str(root.winfo_x()+50)+"+"+str(root.winfo_y()+100))
        room_win.resizable(False,False)

        roomName = Label(room_win, text=rn[i],font=("",15))
        roomName.place(x=200,y=30,anchor="center")
        userName = Label(room_win, text=F"Username: {un[i]}",font=("",10))
        userName.place(x=200,y=70,anchor="center")
        time = Label(room_win, text=F"Time: {t[i]}",font=("",10))
        time.place(x=200,y=90,anchor="center")

        def join_zoom():
            print("Call Sign in bot.")
            with open(os.path.join(sys.path[0], "zoom_path.txt"),'r+') as pathFile:
                path = pathFile.readline()
            sign_in(path,str(rc[i]),str(pc[i]),str(un[i]))
        
        def delete():
            print("Delete....")
            deleteRow(i)
            room_win.destroy()
            messagebox.showinfo("Deleted", "Delete complete.")
            frame.destroy()
            program_ui()
        
        def edit():
            #Show exist data in entry box
            roomcode.set(rc[i])
            passcode.set(pc[i])
            get_username.set(un[i])
            get_roomname.set(rn[i])
            get_time.set(t[i])
            room_win.destroy()
            
            def update():
                #Like Adding
                get_rc = roomcode.get()
                get_rc = get_rc.replace(" ","")
                get_pc = passcode.get()
                get_rn = get_roomname.get()
                get_un = get_username.get()
                get_t = get_time.get()
                data = {'room_name':get_rn,'roomcode':get_rc, 'passcode':get_pc, 'username':get_un,'time':get_t}
                updateData(i,data)
                roomcode.set("")
                passcode.set("")
                get_username.set("")
                get_roomname.set("")
                get_time.set("")   
                messagebox.showinfo("Updated", "Update complete.")
                frame.destroy()
                program_ui()
            Button(topFrame,text="UPDATE",width=10,height=1,bd = 1,command=update).grid(row = 1,column = 8,sticky=E,padx = 5)

        signin_b = Button(room_win, text="Sign In",command = join_zoom,bg = "blue",fg = "white",activebackground='#345',activeforeground='white', relief="ridge",borderwidth=1)
        signin_b.place(x=140,y=150,anchor="center")
        edit_b = Button(room_win, text="Edit",command = edit,bg = "skyblue",fg = "white",activebackground='#345',activeforeground='white', relief="ridge",borderwidth=1)
        edit_b.place(x=200,y=150,anchor="center")
        del_b = Button(room_win, text="Delete",command = delete,bg = "red",fg = "white",activebackground='#345',activeforeground='white', relief="ridge",borderwidth=1)
        del_b.place(x=260,y=150,anchor="center")

        
    btn = []
    for i in range(getLenght()):
        b = Button(myframe,text=F"{rn[i]}", fg="white", bg="skyblue",font="10",bd = 0,width=42,height=5,command=lambda i = i: roomWin(i)).pack(pady=2)
        btn.append(b)
    

    root.resizable(False,False)
    root.mainloop()

program_ui()
