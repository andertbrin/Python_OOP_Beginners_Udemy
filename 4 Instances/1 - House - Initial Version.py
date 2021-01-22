class House:
    
    def __init__(self, price):
        self.price = price
        

h1 = House(5000)
print(h1.price)

h1.price = 2000
print(h1.price)