from operator import attrgetter

class Bicycle(object):
    def __init__(self,name,weight,cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getCost(self):
        return self.cost


class Shop(object):
    def __init__(self, name, margin, inventory={}, spend=0,revenue=0):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.spend = spend
        self.revenue = revenue
        self.profit = revenue - spend

    def buyCycle(self,cycle):
        if cycle in self.inventory:
            self.inventory[cycle] += 1
        else:
            self.inventory[cycle] = 1
        self.spend += cycle.getCost()

    def sellCycle(self,cycle):
        if self.inventory[cycle] > 0:
            self.inventory[cycle] -= 1
            self.revenue += cycle.getCost()*(1+self.margin)

    def sales(self,customer):
        print("Hello, {}, I would like to recommend the following bicyles to you:".format(customer.name))
        for bike in self.inventory.keys():
            if bike.cost <= customer.funds:
                print(bike.name)

    def realSell(self,customer):
        saleFinished = False
        possibleBikes = []
        print("Hello, {}, I would like to recommend the following bicyles to you:".format(customer.name))
        for bike in self.inventory.keys():
            if bike.cost*(1+self.margin) <= customer.funds and self.inventory[bike] > 0:
                possibleBikes.append(bike.name)
                print(bike.name)
        while not saleFinished:
            answer = input("Which bike would you like?\n")
            if answer in possibleBikes:
                saleFinished = True
                for bike in self.inventory:
                    if bike.name == answer:
                        bikeSold = bike
            else:
                print("I'm sorry I didn't get that. Please choose from the following bikes")
                for bike in possibleBikes:
                    print (bike)
        print("Thank you, {} costs ${}".format(bikeSold.name,bikeSold.cost*(1+self.margin)))
        self.sellCycle(bikeSold)
        customer.buyCycle(bikeSold,self)


    def inventoryCheck(self):
        print("Our current inventory is")
        for bike in self.inventory.keys():
                print("{}: {}".format(bike.name, self.inventory[bike]))

    def upSell(self,customer):
        possibleBikes = []
        print("Hello, {}, I would like to recommend the following bicyle to you:".format(customer.name))
        for bike in self.inventory.keys():
            if bike.cost <= customer.funds:
                possibleBikes.append(bike)
        print(max(possibleBikes, key = attrgetter('cost')).name)

    def cashFlows(self):
        print("Our current revenue is {}, our current costs are {}, and our profit is {}".format(self.revenue,self.spend,self.revenue-self.spend))


class Customer(object):
    def __init__(self,name, funds, cycles=[]):
        self.name = name
        self.funds = funds
        self.cycles = cycles

    def buyCycle(self,cycle,shop):
        if self.funds >= cycle.getCost():
            self.cycles.append(cycle)
            self.funds -= cycle.getCost()*(1+shop.margin)