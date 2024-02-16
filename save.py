import json
import main as app
import sys

# Gets the encounters from main
def __get_encounters():
    return app.encounters


# Gets the number of encounters that are in the json file
def __get_prev_encounters():
    file = open('encounters.json')
    data = json.load(file)

    prev_encounters = data["encounters"]
    file.close()

    return prev_encounters


# This function is used to display the total encounters 
# That are stored in the json file
def load_encounters(label):
    prev_encounters = __get_prev_encounters()
    label.config(text="Total Saved Encounters: " + str(prev_encounters))


# This function saves the current encounters to the json
# It also exits the program after saving
def save_encounters():
    prev_encounters = __get_prev_encounters()
    curr_encounters = __get_encounters()

    total_encounters = prev_encounters + curr_encounters

    dictionary = {
        "encounters": total_encounters
    }

    with open('encounters.json', 'w') as json_file:
        json.dump(dictionary, json_file)
    
    app.stop_flag = True
    print("Exiting Program.")
    sys.exit()