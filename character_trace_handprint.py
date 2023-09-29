from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def random_handprint():
    global player_last_x, player_last_y
    global pickonce

    if pickonce == 0:
        player_last_x = random.randint(0, TUK_WIDTH)
        player_last_y = random.randint(0, TUK_HEIGHT)
        pickonce += 1


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_in_line():
    global player_first_x, player_first_y
    global player_last_x, player_last_y
    global x, y
    global i, moveonce

    if moveonce < 1:
        t = i / 100
        x = (1-t)*player_first_x + t*player_last_x
        y = (1-t)*player_first_y + t*player_last_y
        i += 1
        if i > 100:
            i = 0
            moveonce += 1

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
player_first_x, player_first_y = x, y
player_last_x, player_last_y = x, y

frame = 0
i, moveonce, pickonce = 0, 0, 0


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if player_first_x <= player_last_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)

    random_handprint()
    hand.draw(player_last_x, player_last_y)
    if x == player_last_x and y == player_last_y:
        player_first_x, player_first_y = player_last_x, player_last_y
        pickonce = 0
        moveonce = 0
    move_in_line()
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    delay(0.01)


close_canvas()




