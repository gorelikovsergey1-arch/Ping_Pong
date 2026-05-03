from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
clock = time.Clock()
FPS = 60
run = True
finish = False
while run:
    for e  in event.get():
        if e.type == QUIT:
            run = False
        window.blit(background,(0, 0))
        draw_lost(lost)
        draw_score(0)
        if not finish:
            enemies.update()
            enemies.draw(window)
            hero.update()
            hero.reset()
        display.update() 
        clock.tick(60)
