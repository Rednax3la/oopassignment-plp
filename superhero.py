class Superhero:
    """A class representing a superhero"""
    
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        """Initialize superhero attributes"""
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # List of powers
        self.weakness = weakness
        self.origin_story = origin_story
        self.energy_level = 100
        
    def use_power(self, power_index):
        """Use one of the superhero's powers"""
        if power_index < len(self.powers):
            print(f"{self.name} uses {self.powers[power_index]}!")
            self.energy_level -= 10
        else:
            print("Power not available!")
            
    def recover(self, hours):
        """Recover energy by resting"""
        self.energy_level = min(100, self.energy_level + hours * 15)
        print(f"{self.name} rested for {hours} hours. Energy level: {self.energy_level}")
        
    def reveal_secret(self):
        """Reveal the superhero's secret identity"""
        print(f"{self.name}'s secret identity is {self.secret_identity}!")
        
    def __str__(self):
        """String representation of the superhero"""
        return f"{self.name} - Powers: {', '.join(self.powers)} | Weakness: {self.weakness}"


class Sidekick(Superhero):
    """A class representing a sidekick that inherits from Superhero"""
    
    def __init__(self, name, secret_identity, powers, weakness, origin_story, mentor):
        """Initialize sidekick attributes"""
        super().__init__(name, secret_identity, powers, weakness, origin_story)
        self.mentor = mentor
        self.training_level = 0
        
    def train(self, hours):
        """Sidekick-specific training method"""
        self.training_level += hours * 2
        print(f"{self.name} trained for {hours} hours with {self.mentor}. Training level: {self.training_level}")
        
    def use_power(self, power_index):
        """Override power usage with less energy consumption"""
        if power_index < len(self.powers):
            print(f"{self.name} carefully uses {self.powers[power_index]}!")
            self.energy_level -= 5
        else:
            print("Power not available!")


# Example usage
if __name__ == "__main__":
    # Create a superhero
    superman = Superhero(
        name="Superman",
        secret_identity="Clark Kent",
        powers=["Super strength", "Heat vision", "Flight", "Freeze breath"],
        weakness="Kryptonite",
        origin_story="Last son of Krypton"
    )
    
    # Create a sidekick
    robin = Sidekick(
        name="Robin",
        secret_identity="Dick Grayson",
        powers=["Acrobatics", "Martial arts", "Detective skills"],
        weakness="Overconfidence",
        origin_story="Former circus acrobat",
        mentor="Batman"
    )
    
    # Demonstrate functionality
    print(superman)
    superman.use_power(1)  # Heat vision
    superman.recover(2)
    
    print("\n")
    
    print(robin)
    robin.use_power(0)  # Acrobatics
    robin.train(3)
    robin.reveal_secret()
