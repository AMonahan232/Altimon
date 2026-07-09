from data_loader import DataLoader
from altimon import Altimon

# Load data
loader = DataLoader("../data")

# Create one of each starter
ignarok_data = loader.get_creature(1)
tidalyx_data = loader.get_creature(2)
sporven_data = loader.get_creature(3)

# Instantiate them at level 5
ignarok = Altimon(ignarok_data, level=5)
tidalyx = Altimon(tidalyx_data, level=5)
sporven = Altimon(sporven_data, level=5)

# Print their status
print(ignarok.get_status())
print(tidalyx.get_status())
print(sporven.get_status())

# Test damage and healing
print("\nTesting damage and healing on Ignarok...")
ignarok.take_damage(10)
print(f"After 10 damage: HP {ignarok.current_hp}/{ignarok.stats['hp']}")
ignarok.heal(5)
print(f"After 5 heal: HP {ignarok.current_hp}/{ignarok.stats['hp']}")

# Test faint
ignarok.take_damage(999)
print(f"After 999 damage: Fainted = {ignarok.is_fainted()}")