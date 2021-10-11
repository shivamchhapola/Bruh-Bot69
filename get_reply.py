import requests


def get_random_insult():
    data = requests.get(
        url='https://evilinsult.com/generate_insult.php?lang=en&type=json').json()
    return data['insult']
