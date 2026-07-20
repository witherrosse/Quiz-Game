import requests



parameters = {
    "amount":10,          ### Number of questions to get ###
    "type": "boolean"     ### True/False questions only###
}




response = requests.get("https://opentdb.com/api.php",params=parameters)

response.raise_for_status()    



data = response.json()



question_data = data["results"]
