import cv2
import pyautogui
import keyboard
import numpy as np
from time import sleep
import threading
import save as save
import json
import sys

# Once 'k' is pressed, program starts
print("Press 'k' to start the program.")
keyboard.wait('k')
print("Starting the program...")
print("Program started. Press 'q' to stop the program. Press 'i' to view controls.")

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


# This function performs the necessary
# Keystrokes to exit a battle quickly
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


# This function looks for the sparkles of a shiny Pokemon appearing
def detect_shiny():
    global stop_flag # This allows the program to stop when a shiny is detected
    shiny_image = cv2.imread("images/shiny_star.png", cv2.IMREAD_COLOR)

    while not stop_flag:
        screen = capture_screen()
        found_shiny = detect_image(shiny_image, screen)

        # If a shiny is found, exit program and print encounters
        if found_shiny:
            print("--------------------")
            print("Found shiny. Exiting...")
            print("Encounters: " + str(encounters + 1))
            print("--------------------")
            stop_flag = True # Set stop flag to true to exit program

    cv2.destroyAllWindows()


# This function detects and exits the battles
# It also moves the character until a battle is found
def detect_battle():
    global encounters
    battle_image = cv2.imread("images/battle_image.png", cv2.IMREAD_COLOR)

    while not stop_flag:
        screen = capture_screen()
        found_battle = detect_image(battle_image, screen)

        # Moves character until battle is entered
        if found_battle:
            print("--------------------")
            print("Found battle.")
            print("--------------------")
            sleep(1)

            # Exit the battle and print the encounters
            exit_battle()
            encounters += 1
            print("Encounters: " + str(encounters))
            found_battle = False
        else:
            move_character()

    cv2.destroyAllWindows()


# Print the saved encounters in JSON
def print_saved_encounters(e):
    save.cmd_load_encounters()


# Exit function for program
def exit_program(e):
    global stop_flag
    prev_encounters = save.__get_prev_encounters()
    curr_encounters = encounters

    total_encounters = prev_encounters + curr_encounters

    dictionary = {
        "encounters": total_encounters
    }

    with open('encounters.json', 'w') as json_file:
        json.dump(dictionary, json_file)
    
    stop_flag = True
    print("Exiting Program.")



# Print the controls
def print_controls(e):
    print("Press 'q' to save & exit.")
    print("Press 'j' to view saved encounters.")

# Set the callback for 'q' key
keyboard.on_press_key('q', exit_program)
keyboard.on_press_key('i', print_controls)
keyboard.on_press_key('j', print_saved_encounters)


# Create threads so that the shiny sparkles can be detected as soon as possible
# This way, the character can be constantly moving and exiting battles
# Without worrying about the program missing the sparkle animation
# This also allows the program to hunt any shiny wild encounter in the game
def main():
    shiny_thread = threading.Thread(target=detect_shiny)
    battle_thread = threading.Thread(target=detect_battle)

    shiny_thread.start()
    battle_thread.start()


main()
