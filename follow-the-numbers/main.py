from random import randint
import pgzrun
from pgzero.actor import Actor

class GameState:
    def __init__(self):
        self.game_over = False
        self.number_of_dots = 10
        self.next_dot = 0
        self.lines = []
        self.dots = []
        self.input_value = ""
        self.reset()

    def reset(self):
        self.game_over = False
        self.next_dot = 0
        self.lines = []
        self.dots = []
        for _ in range(self.number_of_dots):
            actor = Actor("dot")
            actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
            self.dots.append(actor)

WIDTH, HEIGHT = 400, 400
game_state = GameState()

def draw():
    screen.fill("dark green")
    if game_state.game_over:
        screen.draw.text("Game Over! Press 'R' to Restart", center=(WIDTH / 2, HEIGHT / 2), fontsize=30, color="white")
        screen.draw.text("Enter number of dots (1-20) and press Enter:", center=(WIDTH / 2, HEIGHT / 2 + 40), fontsize=20, color="white")
        screen.draw.text(game_state.input_value, center=(WIDTH / 2, HEIGHT / 2 + 70), fontsize=20, color="white")
    else:
        for i, dot in enumerate(game_state.dots, start=1):
            screen.draw.text(str(i), (dot.pos[0], dot.pos[1] + 12))
            dot.draw()
        for line in game_state.lines:
            screen.draw.line(line[0], line[1], (100, 0, 0))

def on_mouse_down(pos):
    if game_state.game_over:
        return
    if game_state.dots[game_state.next_dot].collidepoint(pos):
        if game_state.next_dot:
            game_state.lines.append((game_state.dots[game_state.next_dot - 1].pos, game_state.dots[game_state.next_dot].pos))
        game_state.next_dot += 1
        if game_state.next_dot >= game_state.number_of_dots:
            game_state.game_over = True
    else:
        game_state.lines, game_state.next_dot = [], 0

def on_key_down(key):
    if game_state.game_over:
        if key == keys.R and game_state.game_over:
            game_state.reset()
        elif key == keys.RETURN:
            if game_state.input_value.isdigit():
                number_of_dots = int(game_state.input_value)
                if 1 <= number_of_dots <= 20:
                    game_state.number_of_dots = number_of_dots
                    game_state.reset()
            game_state.input_value = ""
        elif keys.K_0 <= key <= keys.K_9:
            game_state.input_value += chr(key)

pgzrun.go()