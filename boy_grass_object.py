from pico2d import *

import random

# Game object class here
class Grass:
    # 생성자를 이용해서 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 400), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball1:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.ball1 = load_image('ball21x21.png')

    def update(self):
        if self.y > 60 + 10:
            self.y -= random.randint(1, 10)
        else:
            self.y = 65

    def draw(self):
        self.ball1.draw(self.x, self.y)


class Ball2:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.ball2 = load_image('ball41x41.png')

    def update(self):
        if self.y > 60 + 20:
            self.y -= random.randint(1, 10)
        else:
            self.y = 75

    def draw(self):
        self.ball2.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball in ball1:
        ball.update()
    for ball in ball2:
        ball.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in ball1:
        ball.draw()
    for ball in ball2:
        ball.draw()
    update_canvas()

def reset_world(): # 초기화하는 함수
    global running
    global grass
    global team
    global ball1, ball2

    running = True
    grass = Grass() # Grass 클래스를 이용해서 grass 객체 생성
    team = [Boy() for i in range(11)]
    ball1 = [Ball1() for i in range(10)]
    ball2 = [Ball2() for i in range(10)]

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
