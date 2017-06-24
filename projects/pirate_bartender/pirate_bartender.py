import random
drinks_ordered = 5

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

def drinking():
    can_drink = True
    while can_drink:
        if drinks_ordered < 1:
            n = input("Welcome to the pirate bar. Can I get ye somethin' to drink?\n")
            while n not in ("yes", "no"):
                n = input("Yes or no answers only\n").lower()
            if n == "yes":
                n = True
            else:
                n = False
        elif drinks_ordered < 6:
            n = input("Would ye like somethin' else to drink?\n")
            while n not in ("yes", "no"):
                n = input("Yes or no answers only\n").lower()
            if n == "yes":
                n = True
            else:
                n = False
        else:
            print("I think ye've had enough. Go walk the plank.")
            can_drink = False

    return n

def create_drink(answers):
    drink = []

    for answer in answers:
        if answers[answer] == True:
            drink.append(random.choice(ingredients[answer]))
    if len(drink) == 0:
        drink.append("Ye didn't order nothin'")
    return drink

def name_drink(answers):
    name = ''
    count = 0
    for answer in answers:
        if answers[answer] == True and count < 1:
            name += (answer + " n' ")
            count += 1
        elif answers[answer] == True and count < 2:
            name += (answer + " ")
            count += 1
    return (name + "Dog")

if __name__ == '__main__':
    if drinks_ordered < 6:
        while drinking():
            bartender_ask(questions)
            drink = create_drink(answers)
            name = name_drink(answers)
            print ("You ordered a {} -- the ingreients are {}".format(name,drink))
            drinks_ordered += 1
        print("Take care, see ye again soon.")