import subprocess
import pyautogui
import time
# from datetime import datetime #For automatic sign-in but now not available.
import os
import sys

def sign_in(meeting_id, pc, username):
    #open up the zoom app
    
    #Please path your zoom software
    subprocess.Popen(["/Users/acer/AppData/Roaming/Zoom/bin/zoom.exe"])
    time.sleep(10)

    join_meet_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "join_button.png"))
    #zoom bot
    #checking and click join meeting
    if  join_meet_btn == None:
        join_meet_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "join_meeting.png"))
        pyautogui.moveTo(join_meet_btn)
        pyautogui.click()
    else:
        pyautogui.moveTo(join_meet_btn)
        pyautogui.click()
        

    #Enter meeting id
    meeting_id_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "meeting_id.png"))
    pyautogui.moveTo(meeting_id_box)
    pyautogui.write(meeting_id)

    #Enter username
    username_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0],"username.png"))
    pyautogui.moveTo(username_box)
    pyautogui.write(username)

    #Tick box
    radio_box = pyautogui.locateAllOnScreen(os.path.join(sys.path[0], "radio_box.png"))#multiple index
    for btn in radio_box:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)

    #Click Join button
    join_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "join.png"))
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(5)#depend on your internet

    #Enter passcode
    passcode_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0],"passcode.png"))
    pyautogui.moveTo(passcode_box)
    pyautogui.write(pc)
    pyautogui.press('enter')
