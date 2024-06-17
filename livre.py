import random
enemies = ['imgs/fire1.png', 'imgs/fire2.png', 'imgs/fire3.png', 'imgs/rat.png', 'imgs/mike.png']
obstacle = [random.choice(enemies), random.choice(enemies), random.choice(enemies)]
print(obstacle)
obstacle = [random.choice(enemies)*3]
print(obstacle)
#
y = [random.randint(190, 410), random.randint(190, 410), random.randint(190, 410)]
print(y[0], y[1], y[2])
