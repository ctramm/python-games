from random import randint
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

# Global Settings
WIDTH = 500
HEIGHT = 500
GAME_LENGTH = 60  # Time in seconds

# Game State
class GameState:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.time_left = GAME_LENGTH
        self.characters = [Actor("fox", pos=(100, 100)), Actor("hedgehog", pos=(100, 100)), Actor("sonic", pos=(100, 100))]
        self.current_character_index = randint(0, len(self.characters) - 1)
        self.current_character = self.characters[self.current_character_index]
        self.coin = Actor("coin", pos=(200, 200))

    def reset(self):
        self.score = 0
        self.game_over = False
        self.time_left = GAME_LENGTH
        new_character_index = self.current_character_index
        while new_character_index == self.current_character_index:
            new_character_index = randint(0, len(self.characters) - 1)
        self.current_character_index = new_character_index
        self.current_character = self.characters[self.current_character_index]
        self.current_character.pos = (100, 100)
        place_coin(self.coin)
        clock.schedule(time_up, GAME_LENGTH)

game_state = GameState()

def draw():
    screen.fill("dark green")
    game_state.current_character.draw()
    game_state.coin.draw()
    screen.draw.text(f"Score: {game_state.score}", topleft=(10, 10), fontsize=20, color="black")
    screen.draw.text(f"High Score: {game_state.high_score}", topright=(WIDTH - 10, 10), fontsize=20, color="black")
    screen.draw.text(f"Time Left: {game_state.time_left:.1f}", midtop=(WIDTH / 2, 10), fontsize=20, color="black")

    if game_state.game_over:
        screen.fill("pink")
        screen.draw.text("TIME'S UP!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="black")
        screen.draw.text(f"Final Score: {game_state.score}", center=(WIDTH/2, HEIGHT/2 + 50), fontsize=30, color="black")
        screen.draw.text("Press 'R' to Restart", center=(WIDTH / 2, HEIGHT / 2 + 100), fontsize=30, color="black")

def place_coin(coin):
    coin.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))

def time_up():
    game_state.game_over = True
    if game_state.score > game_state.high_score:
        game_state.high_score = game_state.score

def update():
    if not game_state.game_over:
        game_state.time_left -= 1 / 60  # Assuming update is called 60 times per second
        if game_state.time_left <= 0:
            time_up()

        if keyboard.left:
            game_state.current_character.x -= 4
        elif keyboard.right:
            game_state.current_character.x += 4
        elif keyboard.up:
            game_state.current_character.y -= 4
        elif keyboard.down:
            game_state.current_character.y += 4

        # Wrap around the screen boundaries
        if game_state.current_character.x < 0:
            game_state.current_character.x = WIDTH
        elif game_state.current_character.x > WIDTH:
            game_state.current_character.x = 0
        if game_state.current_character.y < 0:
            game_state.current_character.y = HEIGHT
        elif game_state.current_character.y > HEIGHT:
            game_state.current_character.y = 0

        if game_state.current_character.colliderect(game_state.coin):
            game_state.score += 10
            place_coin(game_state.coin)
    else:
        if keyboard.r:
            game_state.reset()

clock.schedule(time_up, GAME_LENGTH)
place_coin(game_state.coin)
pgzrun.go()