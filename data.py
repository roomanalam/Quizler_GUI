import  requests

perameters = {
    "amount":10,
    "category":18,
    "difficulty":"medium",
    "type":"boolean"

}

reponse = requests.get("https://opentdb.com/api.php",params=perameters)
reponse.raise_for_status()
data = reponse.json()
question_data = data["results"]









