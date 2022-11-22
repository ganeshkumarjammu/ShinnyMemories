
import serial                                      # add Serial library for serial communication
import pyautogui                                   # add pyautogui library for programmatically controlling the mouse and keyboard.
removal_list = ["'\n'", "'\r'",'b','\'']
Arduino_Serial = serial.Serial('/dev/ttyUSB0',115200)       # Initialize serial and Create Serial port object called Arduino_Serial
 
while 1:
    incoming_data = str (Arduino_Serial.readline()) # read the serial data and print it as line
    print("iNCOMINGDATA: "+incoming_data)                           # print the incoming Serial data
    incoming_data = incoming_data.strip("\'")
    incoming_data = incoming_data.strip("\'")
     
    for s in removal_list:
        incoming_data = incoming_data.replace(s, '')    
    print(incoming_data) 
    
    if "LEFT" in incoming_data:                    # if incoming data is 'next'
        pyautogui.hotkey('ctrl', 'pgdn')           # perform "ctrl+pgdn" operation which moves to the next tab
        print("LEFT")
        
    if "RIGHT" in incoming_data:                # if incoming data is 'previous'
        pyautogui.hotkey('ctrl', 'pgup')           # perform "ctrl+pgup" operation which moves to the previous tab
        print("RIGHT")

    if "DOWN" in incoming_data:                    # if incoming data is 'down'
        print("DOWN")
        pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        print("DOWN")
        #pyautogui.scroll(-100) 
         
    if "UP" in incoming_data:                      # if incoming data is 'up'
        pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        print("UP")
        #pyautogui.scroll(100)
        
    if 'change' in incoming_data:                  # if incoming data is 'change'
        pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    
        
    incoming_data = "";                            # clears the data
