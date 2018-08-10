from command import Command
import requests
import json
import random
import webbrowser

class RecipeFinder (Command):
    def do(self):
        URL = 'https://www.supercook.com/dyn/results'
        ingredients = ','.join(self.args)
        data = {
            'needsimage': 0,
            'kitchen': ingredients,
            'start': 0
        }

        results = requests.post(url=URL, data=data)
        meals = json.loads(results.text)['results']
        index = random.randint(0, len(meals))
        hash_url = meals[index]['hash']
        webbrowser.open(hash_url)
        return hash_url
