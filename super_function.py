class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the __init__ method of the parent class (Animal)
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Call the speak method of the parent class (Animal) and extend it
        return f"{super().speak()} {self.name} is a {self.breed} and barks."

# Create an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Call the speak method
print(my_dog.speak())