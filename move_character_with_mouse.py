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
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_in_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0, 100+1, 4):
        t = i / 100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
random_x = random.randint(0, TUK_WIDTH)
random_y = random.randint(0, TUK_HEIGHT)

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    # character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(random_x,random_y)
    move_in_line((x,y),(random_x,random_y))
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()


close_canvas()




