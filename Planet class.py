class Planet:
    def __init__(self, name, planet_type, star):
        # Type check
        if not all(isinstance(i, str) for i in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        
        # Empty string check
        if not all(len(i) > 0 for i in [name, planet_type, star]):
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

# Create instances
planet_1 = Planet("Earth", "Terrestrial", "The Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "The Sun")
planet_3 = Planet("Proxima Centauri b", "Super Earth", "Proxima Centauri")

# Print objects (__str__)
print(planet_1)
print(planet_2)
print(planet_3)

# Call orbit method
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
