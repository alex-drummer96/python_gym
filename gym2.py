class House():
    """ house description """
    def __init__(self):
        """house properties"""
        self.year = 2022
    def age (self, data):
        """How old"""
        self.year -= data
house1 = House()
house1.age(int(input("введите сегодняшний год")))
print(-1*int(house1.year))
