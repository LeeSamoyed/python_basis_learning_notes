class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "sit!")

    def roll_over(self):
        print(self.name.title() + "roll over!")

    def update_name(self, name):
        self.name = name


class Samoyed(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def roll_over(self):
        print(self.name.title() + "|||roll over!")


my_dog = Dog('willie', 6)

my_dog.name
my_dog.roll_over()

my_dog.name = 'dog'
my_dog.roll_over()

my_dog.update_name('dog_one')
my_dog.roll_over()

my_samoyed = Samoyed('samoyed', 20)
my_samoyed.roll_over()