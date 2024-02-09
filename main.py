import cv2
import pyautogui
import keyboard
import numpy as np
from time import time, sleep

# Once 's' is pressed, program starts
print("Press 'k' to start the program.")
print("After pressing 'k', press 'q' to stop the program.")
keyboard.wait('k')
print("Starting the program...")


def capture_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    img_bgr = np.array(screenshot)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

# Uses image detection to detect if a battle has been found


def detect_battle(template, screen, threshold=0.9):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the threshold
    if max_val > threshold:
        print("Battle found!")
        return True

# Movement function for player
# Currently not in use


def move_character():
    print("Moving character...")
    pyautogui.keyDown('left')
    sleep(1)
    pyautogui.keyUp('left')

    pyautogui.keyDown('right')
    sleep(1)
    pyautogui.keyUp('right')

    print("Done.")


def exit_battle():
    print("Exiting battle...")
    sleep(5)

    print("Press 'x'")
    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(2)

    print("Press 'down'")
    pyautogui.keyDown('down')
    sleep(0.5)
    pyautogui.keyUp('down')
    sleep(2)

    print("Press 'right'")
    pyautogui.keyDown('right')
    sleep(0.5)
    pyautogui.keyUp('right')
    sleep(2)

    print("Press 'x'")
    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(2)

    print("Press 'x'")
    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(2)

    print("Done, battle has been exited.")


def main():
    battle_image = cv2.imread("battle_image.png", cv2.IMREAD_COLOR)

    while True:
        screen = capture_screen()
        found_battle = detect_battle(battle_image, screen)

        if found_battle:
            print("Found battle, exiting program.")
            sleep(1)
            exit_battle()
            break
        else:
            move_character()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping program.")
            break

    cv2.destroyAllWindows()


main()
