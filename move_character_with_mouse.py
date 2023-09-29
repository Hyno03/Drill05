from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

# def random_handprint():
#     random_x = random.randint(0, TUK_WIDTH)
#     random_y = random.randint(0, TUK_HEIGHT)
#     hand.draw(random_x,random_y)

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
    global i

    t = i / 100
    x = (1-t)*player_first_x + t*player_last_x
    y = (1-t)*player_first_y + t*player_last_y
    i += 1
    if i > 100:
        i = 0


running = True
random_x = random.randint(0, TUK_WIDTH)
random_y = random.randint(0, TUK_HEIGHT)
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
player_first_x, player_first_y = x, y
player_last_x, player_last_y = random_x, random_y
frame = 0
i = 0


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(random_x, random_y)
    move_in_line()
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()


close_canvas()




