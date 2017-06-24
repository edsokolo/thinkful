import random

class Musician(object):
    def __init__(self,sounds,name):
        self.sounds = sounds
        self.name = name

    def solo(self,length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(["Twang", "Thrumb", "Bling"],name)
        self.instrument = "Bass"

class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(["Boink", "Bow", "Boom"],name)
        self.instrument = "Guitar"

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(["Bang", "Boom", "Chang"],name)
        self.instrument = "Drums"

    def count_off(self):
        print("One Two Three Four!")

    def explode(self):
        print("Kablaam\nThe {} spontaneously combusted".format(self.name))


class Band(object):
    def __init__(self,members,name):
        self.members = members
        self.name = name

    def hire_member(self,musician):
        if musician not in self.members:
            self.members.append(musician)
            print("{} is now in the band".format(musician.name))
        else:
            print("{} is already in the band".format(musician.name))

    def fire_member(self,musician):
        if musician in self.members:
            self.members.remove(musician)
            print("{} is fired".format(musician.name))
        else:
            print("{} is already not in the band".format(musician.name))

    def play_music(self,length):
        for member in self.members:
            if member.instrument == "Drums":
                member.count_off()
        for i in range(length):
            self.members[i % len(self.members)].solo(random.choice(range(10)))


    def intro(self):
        return print("Hello, we are the {}".format(self.name))

    def member_intro(self):
        for member in self.members:
            return print("{} on the {}".format(member.name,member.instrument))

dave = Bassist("Dave")
steve = Guitarist("Steve")
frank = Drummer("Frank")
bing = Band([dave,steve,frank], "The Bing Bongs")
bing.play_music(4)