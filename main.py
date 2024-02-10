import cv2
import pyautogui
import keyboard
import numpy as np
from time import sleep
import threading

# Once 's' is pressed, program starts
print("Press 'k' to start the program.")
print("After pressing 'k', press 'q' to stop the program.")
keyboard.wait('k')
print("Starting the program...")

stop_flag = False
encounters = 0

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
        print("Image found.")
        return True
    

# Movement function for player
# Simulates the needed keystrokes to move
def move_character():
    pyautogui.keyDown('left')
    sleep(1)
    pyautogui.keyUp('left')

    pyautogui.keyDown('right')
    sleep(1)
    pyautogui.keyUp('right')


def exit_battle():
    print("Exiting battle...")
    sleep(1)

    pyautogui.keyDown('x')
    sleep(0.5)
    pyautogui.keyUp('x')
    sleep(2)

    pyautogui.keyDown('down')
    sleep(0.1)
    pyautogui.keyUp('down')
    sleep(0.5)

    pyautogui.keyDown('right')
    sleep(0.1)
    pyautogui.keyUp('right')
    sleep(0.2)

    pyautogui.keyDown('x')
    sleep(0.3)
    pyautogui.keyUp('x')
    sleep(0.5)

    pyautogui.keyDown('x')
    sleep(0.3)
    pyautogui.keyUp('x')
    sleep(1)

    print("Battle has been exited.")


def detect_shiny():
    global stop_flag
    shiny_image = cv2.imread("images/shiny_star.png", cv2.IMREAD_COLOR)

    while not stop_flag:
        screen = capture_screen()
        found_shiny = detect_image(shiny_image, screen)

        # Moves character until the the encountered pokemon is not rattata or pidgey
        if found_shiny:
            print("--------------------")
            print("Found shiny. Exiting...")
            print("Encounters: " + str(encounters + 1))
            print("--------------------")
            stop_flag = True

    cv2.destroyAllWindows()


def detect_battle():
    global encounters
    # Read the battle_image
    battle_image = cv2.imread("images/battle_image.png", cv2.IMREAD_COLOR)

    while not stop_flag:
        screen = capture_screen()
        found_battle = detect_image(battle_image, screen)

        # Moves character until the the encountered pokemon is not rattata or pidgey
        if found_battle:
            print("--------------------")
            print("Found battle.")
            print("--------------------")
            sleep(1)

            # Currently exits battle as soon as it enters one
            exit_battle()
            encounters += 1
            print("Encounters: " + str(encounters))
            found_battle = False
        else:
            move_character()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping program.")
            break

    cv2.destroyAllWindows()


def main():
    shiny_thread = threading.Thread(target=detect_shiny)
    battle_thread = threading.Thread(target=detect_battle)

    shiny_thread.start()
    battle_thread.start()

main()
