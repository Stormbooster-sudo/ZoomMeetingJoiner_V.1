import subprocess
import pyautogui
import time
# from datetime import datetime
import os
import sys

def sign_in(meeting_id, pc):
    #open up the zoom app

    #Please path your zoom software
    subprocess.call(["/Users/acer/AppData/Roaming/Zoom/bin/zoom.exe"])
    # webbrowser.open('https://zoom.us/')
    time.sleep(5)

    #zoom bot
    #click join meeting
    join_meet_btn = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "join_button.png"))
    pyautogui.moveTo(join_meet_btn)
    pyautogui.click()

    #Enter meeting id
    meeting_id_box = pyautogui.locateCenterOnScreen(os.path.join(sys.path[0], "meeting_id.png"))
    pyautogui.moveTo(meeting_id_box)
    pyautogui.write(meeting_id)

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
