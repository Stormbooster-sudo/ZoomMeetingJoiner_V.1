import subprocess
import pyautogui
import time
# from datetime import datetime #For automatic sign-in but now not available.
import os
import sys

def sign_in(p,meeting_id, pc, username):
    #open up the zoom app
    path = p
    #Please path your zoom software
    subprocess.Popen([path])
    print("Call Zoom.")
    time.sleep(5)
    print("Signing In ............")
    time.sleep(5)

    join_meet_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "image/join_button.png"))
    #zoom bot
    #checking and click join meeting
    if  join_meet_btn == None:
        print("Your didn't sign in via acount.")
        join_meet_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "image/join_meeting.png"))
        pyautogui.moveTo(join_meet_btn)
        pyautogui.click()
    else:
        pyautogui.moveTo(join_meet_btn)
        pyautogui.click()
        

    #Enter meeting id
    meeting_id_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "image/meeting_id.png"))
    pyautogui.moveTo(meeting_id_box)
    pyautogui.write(meeting_id)

    #Enter username
    username_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0],"image/username.png"))
    if  username_box != None:
        pyautogui.moveTo(username_box)
        pyautogui.click()
        pyautogui.write(username)
    else:
        pass

    #Tick box
    radio_box = pyautogui.locateAllOnScreen(os.path.join(sys.path[0], "image/radio_box.png"))#multiple index
    for btn in radio_box:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)

    #Click Join button
    join_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "image/join.png"))
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(5)#depend on your internet

    #Enter passcode
    passcode_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0],"image/passcode.png"))
    pyautogui.moveTo(passcode_box)
    pyautogui.write(pc)
    # pyautogui.press('enter')
    print("Signed In.")
