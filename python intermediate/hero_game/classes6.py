

import random


N = 25
M = 25
K = 2
PROPORTION = 1


class Hero:
    def __init__(self, name: str) -> object:
        self.name = name
        self.level = 1
        self.damage = 2
        self.hp = 10
        self.coins = 0
        self.full_hp = 10 #in order to remember the full hp
        self.defend = False #is the defend option is on

    
    def heal(self) -> None:
        """
        this function heals the character by N percent
        """
        self.hp = self.hp * (N/100 + 1)        

    
    def level_up(self) -> bool: 
        """
        this function level up a character 
        """
        if self.level + 1 * K < self.coins:
            self.level += 1
            self.damage = self.damage * (M/100 + 1)
            self.full_hp = self.full_hp * (M/100 + 1)
            self.hp = self.full_hp
            return True
        
        return False


    def attack(self, monster) -> None:
        """
        attack monster function
        """
        monster.reduce_health(self)
        
        if monster.health <= 0:
            self.coins += self.level

    
    def is_defend(self) -> None:
        """
        activates the defend function
        """
        self.defend = True

    
    def reduce_health(self, monster) -> float:
        """
        the reduce health function
        """
        current_health = self.hp
        diff = current_health - (self.hp * 1.8) # help the logics of the game

        if self.defend:
            self.hp = self.hp * 1.8

        self.hp -= monster.damage

        if self.hp < 0:
            self.hp = 0

        if self.defend:
            if diff > monster.damage:
                self.hp = current_health
            else: 
                self.hp -= (diff - monster.damage)

            self.defend = False
        
        return self.hp

    
    def increase_coins(self, coins: int) -> None:
        """
        increases coins as the amount of coins
        """
        self.coins += coins

    
    def __str__(self) -> str:
        """
        """
        return f"hero: level - {self.level}, hp - {self.hp}, damage - {self.damage}"


class Monster:
    def __init__(self, name: str, level_hero: int) -> object:
        generate_level = random.randint(level_hero - 1, level_hero + 1)

        if generate_level == 0:
            generate_level = 1
        
        self.name = name 
        self.level = generate_level
        self.hp = generate_level * PROPORTION
        self.damage = generate_level * PROPORTION

    
    def attack(self, hero: Hero) -> None:
        """
        attack the hero
        """
        hero.reduce_health(self)

    
    def reduce_health(self, hero: Hero) -> float:
        """
        reduces the health of the hero 
        """
        self.hp -= hero.damage

        if self.hp < 0:
            self.hp = 0

        return self.hp
    

    def __str__(self) -> str:
        return f"monster: level - {self.level}, hp - {self.hp}, damage - {self.damage}"
    

def choose_action(hero: Hero, monster: Monster) -> float:
    """
    choose action of the player
    input: hero and monster
    """
    print("Choose an action")
    print("(1) attack")
    print("(2) level up")
    print("(3) regain health")
    print("(4) defend")
    selection = input("enter selection: ")

    while selection != "1" and selection != "2" and selection != "3" and selection != "4":
        selection = input("enter selection: ")

    if selection == "1":
        return monster.reduce_health(hero)

    if selection == "2":
        if not hero.level_up():
            print("you cant, choose other other action")
            choose_action(hero, monster)

    if selection == "3":
        hero.heal()

    if selection == "4":
        hero.is_defend()
    
    hero.coins += 1
    return -1


def main_function() -> None:
    """
    the main logic of the game
    """
    my_hero = Hero(input("enter name of your hero"))
    counter = 1

    while True: 
        monster = Monster(f"monster{counter}", my_hero.level)
        print(monster)
        print(my_hero)
        monster_hp = choose_action(my_hero, monster)
        my_hero.reduce_health(monster)

        if monster_hp == 0:
            monster = Monster(f"monster{counter + 1}", my_hero.level)

        if my_hero.hp == 0:
            print("you lost")
            break
        
        counter += 1


        
