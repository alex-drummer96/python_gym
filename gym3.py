class house ():
    '''opisanie doma'''
    def __init__(self, street, number):
        '''opisanie svoistv'''
        self.street = street
        self.number = number
        self.age = 25
    def build (self):
        '''opisanie metoda'''
        print('ulitsa'+' '+self.street+' '+'dom nomer'+' '+self.number)
house1 = house('Rabina', '18a')
print(house1.number)
house1.build()
class otherhouse(house):
    '''drugoe opisanie'''
    def __init__(self, prospekt, number):
        '''opisanie svoistv'''
        self.prospekt = prospekt
        super().__init__(self, number)
otherhouse1=otherhouse('blabla', 2)
print(otherhouse1.number)
