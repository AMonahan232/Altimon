import random

class Altimon:
    """
    Represents a single Altimon instance owned by the player or an enemy.
    Combines base species data with individual personality and level scaling.
    """

    def __init__(self, data, level=5):
        # Identity
        self.id = data["id"]
        self.name = data["name"]
        self.types = data["type"]
        self.description = data["description"]

        # Assign a random personality from the species pool
        self.personality = random.choice(data["personality_pool"])

        # Level
        self.level = level

        # Calculate stats scaled to level
        self.base_stats = data["base_stats"]
        self.stats = self.calculate_stats()

        # Set current HP to max HP
        self.current_hp = self.stats["hp"]

        # Moves
        self.moves = data["moves"]

        # Evolution data
        self.evolution = data.get("evolution", None)

    def calculate_stats(self):
        """
        Scale base stats to the current level.
        Formula: stat = (base_stat * level) // 50 + 5
        HP gets a bonus to make it feel more substantial.
        """
        stats = {}
        for stat_name, base_value in self.base_stats.items():
            if stat_name == "hp":
                stats[stat_name] = (base_value * self.level) // 50 + self.level + 10
            else:
                stats[stat_name] = (base_value * self.level) // 50 + 5
        return stats

    def is_fainted(self):
        """Return True if this Altimon has no HP remaining."""
        return self.current_hp <= 0

    def take_damage(self, amount):
        """Reduce HP by amount, floored at 0."""
        self.current_hp = max(0, self.current_hp - amount)

    def heal(self, amount):
        """Restore HP by amount, capped at max HP."""
        self.current_hp = min(self.stats["hp"], self.current_hp + amount)

    def get_status(self):
        """Return a readable summary of this Altimon's current state."""
        return (
            f"{self.name} (Lv.{self.level}) | "
            f"HP: {self.current_hp}/{self.stats['hp']} | "
            f"Personality: {self.personality}"
        )