import pyautogui 
import serial                               # add pyautogui library for programmatically controlling the mouse and keyboard.
print(serial.__file__)
ArduinoSerial = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData

while 1:

    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print (incoming)
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)
    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  
    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 
    if 'Vup' in incoming:
        pyautogui.press("volumeup")
    if 'Vdown' in incoming:
        pyautogui.press("volumedown")

    incoming="";