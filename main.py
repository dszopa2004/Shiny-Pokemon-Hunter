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


def find_and_click(template, screen, threshold=0.9):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the threshold
    if max_val > threshold:
        # Calculate the center of the template match location
        center_x = max_loc[0] + template.shape[1] // 2
        center_y = max_loc[1] + template.shape[0] // 2
        pyautogui.click(center_x, center_y)
        print(center_x)
        print(center_y)

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


def main():
    battle_image = cv2.imread("battle_image.png", cv2.IMREAD_COLOR)

    while True:
        screen = capture_screen()
        find_and_click(battle_image, screen)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping program.")
            break

    cv2.destroyAllWindows()


main()
