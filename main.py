class Animal:
    def speak(self):
        print("Ovoz chiqardi")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()
