if __name__ == '__main__':
    from bicycles import *

    bike1 = Bicycle("Crazy Bike", 10, 100)
    bike2 = Bicycle("Regular Bike", 15, 250)
    bike3 = Bicycle("Nice Bike", 20, 350)
    bike4 = Bicycle("Premium Bike", 18, 500)
    bike5 = Bicycle("Supreme Bike", 15, 750)
    bike6 = Bicycle("Impossible Bike", 0, 1000)
    bikes = [bike1,bike2,bike3,bike4,bike5,bike6]

    shop1 = Shop("Tim's Bikes",.2,{})

    for bike in bikes:
        shop1.buyCycle(bike)

    steve = Customer("Steve",200)
    frank = Customer("Frank",500)
    bob = Customer("Bob",1000)
    customers = [steve,frank,bob]

#    for customer in customers:
#        shop1.sales(customer)

#    for customer in customers:
#        shop1.upSell(customer)

    shop1.inventoryCheck()

    for customer in customers:
        shop1.realSell(customer)
        print("{} has ${} in remaining funds".format(customer.name,customer.funds))

    shop1.inventoryCheck()
    shop1.cashFlows()