from random import randint
import matplotlib.pyplot as plt
from statistics import mean

def roll_d12():  # roll 1d12
    return randint(1,12)

def advantage():  # roll 2d12, return largest result
    a = roll_d12()
    b = roll_d12()
    return(max([a,b]))

def savage_attacker():  # savage attacker greataxe attack
    return advantage() + 4

def regular_attack():  # regular ol' greataxe attack
    return roll_d12() + 4

def large_dmg():  # big boi
    return randint(1,4)

def regular_attack_great_weapon(): # regular attack with 1 and 2 increased to 3
    die = roll_d12()
    if die in [1,2]:
        die = 3
    return die + 4

def large_damage_great_weapon():  # large damage with 1 and 2 increased to 3
    die = large_dmg()
    if die in [1,2]:
        die = 3
    return die

def cleave():
    return roll_d12()+1

def cleave_great_weapon():
    die = roll_d12()
    if die in [1,2]:
        die = 3
    return die+1

def savage_round():
    first_attack = savage_attacker()
    second_attack = regular_attack()
    first_large = large_dmg()
    second_large = large_dmg()
    cleave_attack = cleave()
    cleave_large = large_dmg()
    return (first_attack+second_attack+first_large+second_large+cleave_attack+cleave_large)

def great_weapon_round():
    first_attack = regular_attack_great_weapon()
    second_attack = regular_attack_great_weapon()
    first_large = large_damage_great_weapon()
    second_large = large_damage_great_weapon()
    cleave_attack = cleave_great_weapon()
    cleave_large = large_dmg()
    return (first_attack+second_attack+first_large+second_large+cleave_attack+cleave_large)

if __name__ == '__main__':
    savage_attacker_turns = []
    great_weapon_turns = []
    for _ in range(1_000_000):
        savage_attacker_turns.append(savage_round())
        great_weapon_turns.append(great_weapon_round())
    print(mean(savage_attacker_turns))
    print(mean(great_weapon_turns))
    plt.hist([savage_attacker_turns,great_weapon_turns],bins=50,label=['Savage Attacker','Great Weapon Fighting'])
    plt.legend()
    plt.show()