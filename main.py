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

# Capture screen
def capture_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    img_bgr = np.array(screenshot)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb


# Uses image detection to detect if a battle has been found
def detect_image(template, screen, threshold=0.9):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the threshold
    if max_val > threshold:
        print("Battle found!")
        return True
    

# Movement function for player
# Simulates the needed keystrokes to move
def move_character():
    print("Moving character...")
    pyautogui.keyDown('left')
    sleep(1)
    pyautogui.keyUp('left')

    pyautogui.keyDown('right')
    sleep(1)
    pyautogui.keyUp('right')

    print("Done.")


# Function exits the battle by simulating the keystrokes
# required to leave a battle
def exit_battle():
    print("Exiting battle...")
    sleep(3)

    print("Press 'x'")
    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(2)

    print("Press 'down'")
    pyautogui.keyDown('down')
    sleep(0.5)
    pyautogui.keyUp('down')
    sleep(1)

    print("Press 'right'")
    pyautogui.keyDown('right')
    sleep(0.5)
    pyautogui.keyUp('right')
    sleep(1)

    print("Press 'x'")
    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(1.5)

    print("Press 'x'")
    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(2)

    print("Battle has been exited.")


def main():
    encounters = 0
    # Read the battle_image
    battle_image = cv2.imread("battle_image.png", cv2.IMREAD_COLOR)
    rattata_image = cv2.imread("images/rattata.png", cv2.IMREAD_COLOR)
    pidgey_image = cv2.imread("images/pidgey.png", cv2.IMREAD_COLOR)

    while True:
        screen = capture_screen()
        found_battle = detect_image(battle_image, screen)


        # Moves character until the the encountered pokemon is not rattata or pidgey
        if found_battle:
            found_rattata = detect_image(rattata_image, screen)
            found_pidgey = detect_image(pidgey_image, screen)

            if not found_rattata and not found_pidgey:
                print("--------------------")
                print("Found other Pokemon!")
                print("Encounters: " + str(encounters))
                print("--------------------")
                break

            print("--------------------")
            print("Found battle.")
            print("--------------------")
            sleep(1)

            # Currently exits battle as soon as it enters one
            exit_battle()
            encounters += 1
            found_battle = False
        else:
            move_character()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping program.")
            break

    cv2.destroyAllWindows()


main()
