import pygame as pg

FPS = 120

while True:
    window = pg.display.set_mode((200, 200))
    clock = pg.time.Clock()

    window.fill(pg.Color('black'))

    pg.display.update()
    clock.tick(FPS)
