# Name
# Move
# Talk to a person
# Interact
# Inventory
# Abilities
# Stats
# Health
# Status
# Physique
# Description
# Dialogue
# Attack
# Take Damage
# Weapon


class Character(object):
    def __init__(self, name, description, health, attack, weakness):
        self.name = name
        self.description = description
        self.inventory = []
        self.health = health
        self.attack = attack
        self.interact = True
        self.weakness = weakness

        def Dammaged(self):
            print("You hurt your enemy")

        def kill(self):
            print("You killed the enemy or have been killed by the enemy")


you = Character("Savage", "Tall very athletic brave guy", 100, 100, 'rust')


