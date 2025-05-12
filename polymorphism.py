class Animal:
    """Base class for all animals"""
    
    def __init__(self, name):
        self.name = name
        
    def move(self):
        """Base move method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")
        
    def speak(self):
        """Base speak method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    """Dog class with specific movement"""
    
    def move(self):
        print(f"{self.name} the dog is running happily! 🐕")
        
    def speak(self):
        print(f"{self.name} says: Woof! Woof!")


class Fish(Animal):
    """Fish class with specific movement"""
    
    def move(self):
        print(f"{self.name} the fish is swimming gracefully! 🐟")
        
    def speak(self):
        print(f"{self.name} says: Blub blub...")


class Bird(Animal):
    """Bird class with specific movement"""
    
    def move(self):
        print(f"{self.name} the bird is flying high! 🦅")
        
    def speak(self):
        print(f"{self.name} says: Tweet tweet!")


class Snake(Animal):
    """Snake class with specific movement"""
    
    def move(self):
        print(f"{self.name} the snake is slithering silently! 🐍")
        
    def speak(self):
        print(f"{self.name} says: Hisssss...")


# Demonstration of polymorphism
def animal_showcase(animals):
    """Demonstrate polymorphism by having each animal move and speak"""
    print("\n=== Animal Showcase ===")
    for animal in animals:
        animal.move()
        animal.speak()
        print()


if __name__ == "__main__":
    # Create animals
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Sky"),
        Snake("Viper")
    ]
    
    # Demonstrate polymorphism
    animal_showcase(animals)
    
    # Individual animal demonstration
    print("\n=== Individual Demonstration ===")
    buddy = Dog("Buddy")
    buddy.move()
    buddy.speak()
