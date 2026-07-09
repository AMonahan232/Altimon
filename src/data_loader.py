import json
import os

class DataLoader:
    """
    Handles loading and accessing all game data from JSON files.
    Acts as a central registry for creature and move data.
    """

    def __init__(self, data_path):
        self.data_path = data_path
        self.creatures = {}
        self.load_creatures()

    def load_creatures(self):
        """Load all creature data from creatures.json."""
        filepath = os.path.join(self.data_path, "creatures.json")
        with open(filepath, "r", encoding="utf-8-sig") as file:
            raw = json.load(file)
            for creature in raw["altimon"]:
                self.creatures[creature["id"]] = creature

    def get_creature(self, creature_id):
        """Return raw data dict for a creature by ID."""
        return self.creatures.get(creature_id, None)

    def get_all_creatures(self):
        """Return all creature data."""
        return self.creatures