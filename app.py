import json
from difflib import get_close_matches

with open("data.json") as file:
    data = json.load(file)

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        closest = get_close_matches(word, data.keys())
        if closest:
            choice = input("Did you mean " + closest[0] + "? [Y]es or [N]o? ")
            if choice.lower() in ['y', 'yes']:
                return data[closest[0]]
            else:
                return "Please try again."
        else:
            return "No such word exists. Please double check your input."

word = input("Please enter a word to translate: ")
output = translate(word)
if type(output) is list:
    for definition in output:
        print(definition)
else:
    print(output)
