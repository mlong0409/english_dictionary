import json

with open("data.json") as file:
    data = json.load(file)

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "No such word exists. Please double check your input."

word = input("Please enter a word to translate: ")
print(translate(word))
