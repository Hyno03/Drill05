from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def random_handprint():
    random_x = random.randint(0, TUK_WIDTH//2)
    random_y = random.randint(0, TUK_HEIGHT//2)
    hand.draw(random_x,random_y)

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    random_handprint()
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.1)


close_canvas()




