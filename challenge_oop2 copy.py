import sys
from challenge_oop import Barrel


self.amount_remove= int(input('How much to remove\n >'))
        
        if self.fruit_type == fruit:
            self.barrel2.fruit_count -= self.amount_remove
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.barrel2.fruit_count -= self.amount_remov
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'{self.name}'




class Menu2:
    def __init__(self):
        self.barrel2 = Barrel()
        self.choices = {
            '1': self.add_fruit2,
            '2': self.get_fruit_type,
            '3': self.remove,
            '4': self.empty_barrel,
            '5': exit,
        }
    def display_barrel(self):
        print(
       '''
    Fruit Menu:
    1. Add to barrel
    2. Get the type of fruit in the barrel
    3. Remove fruit from a barrel
    4. Reset the barrel
    5. Exit
    '''
        )

    def run(self):
        while True:
            self.display_barrel()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)  
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')
    def add_fruit2(self):
        message = input('Enter a message: ')
        self.barrel2.add_fruit(message)
        print('Your fruit has been added.')
    
    def get_fruit_type(self):
        print (self.barrel2.fruit_type)
    
    def remove(self, fruit):
        message = input('how much would you like to remove?')
        self.barrel2.remove_item(message)
    def empty_barrel(self, fruit):
        while self.barrel2.fruit_count >0:
            self.fruit_type == fruit
            self.barrel2.fruit_count -=1
            self.fruit_type = None
        







if __name__ == '__main__':
    menu = Menu2()
    menu.run()
# not sure what this means


