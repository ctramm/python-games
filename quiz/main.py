import pgzrun
from pygame import *


WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box_1 = Rect(0, 0, 495, 165)
answer_box_2 = Rect(0, 0, 495, 165)
answer_box_3 = Rect(0, 0, 495, 165)
answer_box_4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box_1.move_ip(50, 358)
answer_box_2.move_ip(735, 358)
answer_box_3.move_ip(50, 538)
answer_box_4.move_ip(735, 538)

answer_boxes = [answer_box_1, answer_box_2, answer_box_3, answer_box_4]

score = 0
time_left = 10

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color="black")
    screen.draw.textbox(question[0], main_box, color="black")

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color="black")
        index += 1

def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left
    score += 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Click on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

def on_key_up():
    pass

def default_questions():
    global questions
    questions = [
        ["What is the capital of France?", "Lyon", "Marseille", "Paris", "Nice", 3],
        ["Who wrote the play 'Romeo and Juliet'?", "William Wordsworth", "William Shakespeare", "Charles Dickens", "Jane Austen", 2],
        ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
        ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Osmium", "Nitrogen", 2],
        ["In which year did the Titanic sink?", "1914", "1912", "1916", "1920", 2]
    ]
    return questions

# questions = get_questions.fetch_questions()
question = default_questions().pop(0)
clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()