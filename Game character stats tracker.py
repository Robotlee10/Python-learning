class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    # 3. Read-only name property
    @property
    def name(self):
        return self._name

    # 4. Health property with getter and setter
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    # 5. Mana property with getter and setter
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    # 6. Level getter
    @property
    def level(self):
        return self._level

    # 7. Level up method
    def level_up(self):
        self._level += 1
        self.health = 100  # Uses setter
        self.mana = 50    # Uses setter
        print(f"{self.name} leveled up to {self.level}!")

    # 8. String representation
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Mana: {self.mana}")

# --- Usage Example ---
hero = GameCharacter('Kratos')
print(hero)

hero.health -= 30
hero.mana -= 10
print("\n--- After Damage ---")
print(hero)

print("\n--- Leveling Up ---")
hero.level_up()
print(hero)