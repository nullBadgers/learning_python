import random

hp = 50
difficulty = 2

health_potion = int(random.randint(25, 50) / difficulty)

hp = hp + health_potion

print(f'Your health is now: {hp}')

#original print
print(f'Your health is now: {hp}, while at level: {difficulty}')   

#working with difficulty thanks to josh
print("Your health is now {hp}, while at level: {difficulty}".format(hp=hp, difficulty=difficulty))
