import PySimpleGUI as sg
import sys,webbrowser
sys.path.append("C:/Users/HP/AppData/Local/Programs/Python/Python38/Lib/site-packages/mediapipe/python")
sys.path.append("C:/Users/HP/AppData/Local/Programs/Python/Python38/Lib/site-packages/mediapipe/python/solutions")
def privacy_mode():
    import serial                                      # add Serial library for serial communication
    import pyautogui                                   # add pyautogui library for programmatically controlling the mouse and keyboard.
    print(serial.__file__)
    Arduino_Serial = serial.Serial('com4',9600)       # Initialize serial and Create Serial port object called Arduino_Serial
    
    while 1:
        incoming_data = str (Arduino_Serial.readline()) # read the serial data and print it as line
        print(incoming_data)                            # print the incoming Serial data

        if 'next' in incoming_data:                    # if incoming data is 'next'
            pyautogui.hotkey('ctrl', 'pgdn')           # perform "ctrl+pgdn" operation which moves to the next tab
            
        if 'previous' in incoming_data:                # if incoming data is 'previous'
            pyautogui.hotkey('ctrl', 'pgup')           # perform "ctrl+pgup" operation which moves to the previous tab

        if 'Down' in incoming_data:                    # if incoming data is 'down'
            #pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
            pyautogui.scroll(-100)
            pyautogui.press('volumedownl',presses=30) 
            
            
        if 'up' in incoming_data:                      # if incoming data is 'up'
            #pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
            pyautogui.scroll(100)
            
        if 'change' in incoming_data:                  # if incoming data is 'change'
            pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
        if 'Play/Pause' in incoming_data:
            pyautogui.press('space')
        if 'Mute' in incoming_data:
            pyautogui.press('volumemute')
        if 'Exit' in incoming_data:
            exit()
        incoming_data = "";
def non_privacy_mode():
    from math import degrees
    from turtle import pos,position
    import cv2
    import mediapipe as mp
    import pyautogui


    # let's Start Our webcam to capture my hand 
    cap= cv2.VideoCapture(0)
    # Make a hand detector using mediapipe
    detector  = mp.solutions.hands.Hands()
    # Draw landmarks
    draw = mp.solutions.drawing_utils

    indexY= 0

    while True :
        _, img = cap.read()
        # convert the image in rgb 
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # let's detect 
        detected = detector.process(imgRgb)
        #find hands 
        hands = detected.multi_hand_landmarks
        if hands:
            # draw a media pipe 
            for items in hands:
                landmarks = items.landmark
                for postion,landmark in enumerate(landmarks):
                    if postion == 8 :
                        indexY = landmark.y
                    elif postion == 5:
                        BottomIndexY = landmark.y
                        # 1 - when the index y value e (punch) thincreasen decrease the volume 
                        if indexY > BottomIndexY :
                            # lets down the volume 
                            pyautogui.press("volumedown")
                        elif indexY < BottomIndexY:
                            # lets upthe volume 
                            pyautogui.press("volumeup")
        cv2.imshow("Press Q to exit",img)
        if cv2.waitKey(1) == ord('q'):#press q to exit
            exit()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [  [sg.Text('Choose privacy mode or non privacy mode',key = '_title_',visible = True)],
            [sg.Text('',key='_t_')],
            [sg.Button('Privacy Mode',key='_pvm_'),
            sg.Button('Non Privacy Mode',key='_npvm_'),
            sg.Button('ChatGpt',key='_gpt_'),
            sg.Button('Exit',key='_exit_')],
            [sg.Text()],
            ]
# Create the Window
window = sg.Window('Hand Gesture Control Application', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '_exit_': # if user closes window or clicks cancel
        break
    if event == '_pvm_':
        window['_title_'].Update('\t\tPrivacy Mode\t\t')
        window['_pvm_'].Update(visible=False)
        window['_npvm_'].Update(visible=False)
        window['_gpt_'].Update(visible=False)
        privacy_mode()
    if event == '_npvm_':
        window['_title_'].Update('\t\tNon Privacy Mode\t\t')
        window['_pvm_'].Update(visible=False)
        window['_npvm_'].Update(visible=False)
        window['_gpt_'].Update(visible=False)
        non_privacy_mode()
    if event == '_gpt_':
        window['_title_'].Update('\t\tChatGPT\t\t\t')
        window['_pvm_'].Update(visible=False)
        window['_npvm_'].Update(visible=False)
        window['_gpt_'].Update(visible=False)
        webbrowser.open("https://chat.openai.com/")

window.close()
