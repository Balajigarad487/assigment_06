# Define the base class 'Dog'
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")

# Define a child class 'JackRussellTerrier' inheriting from 'Dog'
class JackRussellTerrier(Dog):
    def hunt_rats(self):
        print(f"{self.name} is hunting rats.")

    def bark_loudly(self):
        print(f"{self.name} is barking loudly.")

# Define another child class 'Bulldog' inheriting from 'Dog'
class Bulldog(Dog):
    def snore_loudly(self):
        print(f"{self.name} is snoring loudly.")

    def protect_home(self):
        print(f"{self.name} is protecting the home.")

# Create instances of 'JackRussellTerrier' and 'Bulldog'
jack = JackRussellTerrier("Jack", 3, "White")
rocky = Bulldog("Rocky", 5, "Brown")

# Demonstrate the functionality of the classes
print("JackRussellTerrier:")
jack.description()
jack.get_info()
jack.hunt_rats()
jack.bark_loudly()

print("\nBulldog:")
rocky.description()
rocky.get_info()
rocky.snore_loudly()
rocky.protect_home()
