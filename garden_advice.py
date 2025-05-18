# Get user input for season and plant type
season = input("Enter the current season: ")
plant_type = input("Enter the plant type (flower/vegetable): ")

# Functions to return gardening advice
def get_season_advice(season):
    """
    Returns advice based on the provided season.
    """
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n"
    }
    return season_advice.get(season.lower(), "No advice for this season.\n")

def get_plant_advice(plant_type):
    """
    Returns advice based on the provided plant type.
    """
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    }
    return plant_advice.get(plant_type.lower(), "No advice for this type of plant.")

# Variable to hold gardening advice
advice = ""

# Append season and plant advice to the advice string
advice += get_season_advice(season)
advice += get_plant_advice(plant_type)

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
