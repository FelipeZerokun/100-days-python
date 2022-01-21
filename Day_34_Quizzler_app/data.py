import requests

url = 'https://opentdb.com/api.php'
trivia_params = {
    'amount': 10,
    'category': 15,
    'difficulty': 'easy',
    'type': 'boolean'
}
response = requests.get(url, params=trivia_params)
question_data = response.json()["results"]
