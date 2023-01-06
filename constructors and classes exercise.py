class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')

borja = Person('Borja Sanchez')
borja.talk()

bob = Person('Bob Smith')
bob.talk()