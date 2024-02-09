import cv2
import pyautogui
import keyboard
from time import time, sleep

# Once 's' is pressed, program starts
print("Press 'k' to start the program.")
print("After pressing 'k', press 'q' to stop the program.")
keyboard.wait('k')
print("Starting the program...")

# Movement function for player
# Currently not in use


def move_character():
    sleep(1)
    pyautogui.keyDown('left')
    sleep(2)
    pyautogui.keyUp('left')

    pyautogui.keyDown('right')
    sleep(2)
    pyautogui.keyUp('right')


while True:
    sleep(1)
    pyautogui.keyDown('left')
    sleep(2)
    pyautogui.keyUp('left')

    pyautogui.keyDown('right')
    sleep(2)
    pyautogui.keyUp('right')

    if keyboard.is_pressed('q'):
        print("Stopping program.")
        break
