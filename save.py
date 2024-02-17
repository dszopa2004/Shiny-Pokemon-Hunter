import json
import main as app
import sys

# Gets the number of encounters that are in the json file
def __get_prev_encounters():
    file = open('encounters.json')
    data = json.load(file)

    prev_encounters = data["encounters"]
    file.close()

    return prev_encounters


# This function is used to display the total encounters
# That are stored in the json file in the CMD mode
def cmd_load_encounters():
    prev_encounters = __get_prev_encounters()
    print("--------------------------------------")
    print("Total Saved Encounters: " + str(prev_encounters))
    print("--------------------------------------")
