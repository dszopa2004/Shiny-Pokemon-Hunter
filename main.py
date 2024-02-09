import cv2
import pyautogui
import keyboard
from time import time, sleep

# Once 's' is pressed, program starts
print("Press 's'' to start the program.")
print("After pressing 's', press 'q' to stop the program.")
keyboard.wait('s')

while True:
    if keyboard.is_pressed('q'):
        break
