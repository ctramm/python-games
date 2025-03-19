from random import randint
import pgzrun
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600
SCORE = 0
HIGH_SCORE = 0

apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")

FRUITS = [apple, pineapple, orange]
CURRENT_FRUIT = None

def draw():
    screen.clear()
    CURRENT_FRUIT.draw()
    screen.draw.text(f"Score: {SCORE}", topleft=(10, 10), fontsize=30, color="white")
    screen.draw.text(f"High Score: {HIGH_SCORE}", topright=(WIDTH - 10, 10), fontsize=30, color="white")

def place_fruit():
    global CURRENT_FRUIT
    CURRENT_FRUIT = FRUITS[randint(0, len(FRUITS) - 1)]
    CURRENT_FRUIT.x = randint(10, WIDTH - 10)
    CURRENT_FRUIT.y = randint(10, HEIGHT - 10)

def on_mouse_down(pos):
    global SCORE, HIGH_SCORE
    if CURRENT_FRUIT.collidepoint(pos):
        SCORE += 1
        print("Good Shot!")
        place_fruit()
        print(f"Your current score is {SCORE}")
    else:
        print("You missed!")
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
        SCORE = 0
        print("Your score has been reset. :(")
        place_fruit()

place_fruit()
pgzrun.go()