import random


class Toyota:
    color_auto = 'Red'
    price_auto = 1000000
    max_speed = 200
    current_speed = 0


Camry = Toyota()
Prius = Toyota()
Prado = Toyota()
Camry.current_speed = random.randint(0, 200)
Prius.current_speed = random.randint(0, 200)
Prado.current_speed = random.randint(0, 200)
print(Camry.current_speed)
print(Prius.current_speed)
print(Prado.current_speed)
