import pygame

class Config:
    screen_width=640
    screen_height=360
    background_color=(0,0,0)
    image_path=['docs','walking_animation.png']
    game_name='Personaje caminando!!'
    image_width=64
    image_height=128
    x=0
    y=screen_height - image_height
    vel=5
    direction='right'

    def __init__(self):
        pass
        