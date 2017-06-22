import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

answers = {}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

name = ''

def bartender_ask(qs):
    for q in qs:
        print (qs[q])
        n = input("Yes or no\n").lower()
        while n not in ("yes","no"):
            n = input("Yes or no answers only\n").lower()
        if n == "yes":
            n = True
        else:
            n = False
        answers[q] = n

def create_drink(answers):
    drink = []

    for answer in answers:
        if answers[answer] == True:
            drink.append(random.choice(ingredients[answer]))
    if len(drink) == 0:
        drink.append("Ye didn't order nothin'")
    return drink

if __name__ == '__main__':
    bartender_ask(questions)
    drink = create_drink(answers)
    print (drink)