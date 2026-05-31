import requests

### Settings for the trivia questions ###

parameters = {
    "amount":10,          ### Number of questions to get ###
    "type": "boolean"     ### True/False questions only###
}


### Send request to the Open Trivia Database API ###

response = requests.get("https://opentdb.com/api.php",params=parameters)

response.raise_for_status()    ### Stop if there is an error ###

### Get the JSON data from the response ###

data = response.json()

### Extract only the questions part ###

question_data = data["results"]
