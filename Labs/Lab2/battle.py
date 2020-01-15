"""
A battle simulator program. Creates 2 characters and simulates a fight
printing results.
"""

import random
import time


class Character:
    """
    A class used to represent a Character in a battle.
    """

    def __init__(self, strength, health, name, chance_dodge, chance_critical):
        """
        Initialize a Character with their stats.
        :param health: an int, health, >0 to be alive
        :param strength: an int, how much damage character deals
        :param name: a string, character name
        :param chance_dodge: float between 0.0 - 1.0 representing a
        percentage
        :param chance_critical: float between 0.0 - 1.0 representing a
        percentage
        """
        self._health = health
        self.strength = strength
        self.name = name
        self.chance_dodge = chance_dodge
        self.chance_critical = chance_critical

    def get_health(self):
        """
        Return character health.
        :return: float characters health
        """
        if self._health > 0:
            return self._health
        return 0

    def set_health(self, health):
        """
        Set the Character health.
        :param health: float >0 to be alive
        """
        self._health = health

    def is_alive(self):
        """
        Return if the character is alive.
        :return: bool True if alive.
        """
        if self.health > 0:
            return True
        return False

    health = property(get_health, set_health)
    is_alive = property(is_alive)

    def take_damage(self, damage):
        """
        Takes incoming damage, the Character will attempt to dodge. If
        dodge fails damage will be deducted from Characters health.
        :param damage: Amount of damage character will take
        :return: Bool True if attack succeeded
        """
        if random.random() < self.chance_dodge:
            self.set_health(self.health - damage)
            return True
        return False

    def __str__(self):
        """
        Show Character current stats.
        :return: str current stats
        """
        return f'Character name: {self.name}\nhealth: {self.health}\n' \
               f'strength: {self.strength}\nchance dodge: ' \
               f'{round(self.chance_dodge, 2)}\nchance critical:' \
               f' {round(self.chance_critical, 2)} '


class BattleSimulator:
    """Takes 2 characters and makes them fight against each other."""

    def __init__(self, character_1, character_2):
        """
        Initialize a Battle Simulator object with the given two
        characters.
        :param character_1: a character object
        :param character_2: a character object
        """
        self.character_1 = character_1
        self.character_2 = character_2

    def turn(self, attacker, taker):
        """
        The attacker takes a turn attempting to damage the taker.
        :param attacker: a character object
        :param taker: a character object
        :return:
        """
        critical_multi = 1
        # checks if the attacker hits a critical
        if random.random() < attacker.chance_critical:
            critical_multi *= 2
            print(f'BIG HIT! critical multi at: {critical_multi}')
        print(f'{attacker.name} hits '
              f' {attacker.strength * critical_multi} hp!')
        # checks if the taker dodges the attack
        if taker.take_damage(attacker.strength * critical_multi):
            print(f'{taker.name} takes a hit! ouch.'
                  f' {taker.name} has '
                  f'{taker.health} health remaining')
        else:
            print(f'{taker.name} dodges the attack!!!')

    def simulate(self):
        """
        Simulates a battle between two characters.
        """
        while self.character_1.is_alive and self.character_2.is_alive:
            # flip a coin (0,1), if 1 player 1 attacks
            if random.randint(0, 1):
                self.turn(self.character_1, self.character_2)
            else:
                self.turn(self.character_2, self.character_1)

            print('_____-----<<            -*-            >>-----_____')
            time.sleep(.5)
        # if a character dies print final stats of winner
        if self.character_1.is_alive:
            print(f'{self.character_1.name} has won!! o.o7\nfinal stats:')
            print(self.character_1)
        else:
            print(f'{self.character_2.name} has won!! o.o7\nfinal stats:')
            print(self.character_2)


def generate_random_character(name, max_health, min_health, max_strength,
                              min_strength):
    """
    Uses random module to set all the character stats and returns a
    Character object.
    :param name: the name
    :param max_health: min health
    :param min_health: max health
    :param max_strength: max strength
    :param min_strength: min strength
    :return: a Character object
    """
    return Character(random.randint(min_strength, max_strength),
                     random.randint(min_health, max_health),
                     name, random.random(), random.random())


def main():
    """
    Creates two characters and simulates a battle.
    """
    character1 = generate_random_character("Dr. Bones", 100, 60, 15, 5)
    character2 = generate_random_character("zzzQuickScopeszzz", 100, 60, 15, 5)
    battle = BattleSimulator(character1, character2)
    battle.simulate()


if __name__ == '__main__':
    main()
