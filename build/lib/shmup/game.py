import pygame
import os
from shmup.config import Config

class Game:

    def __init__(self):
        pygame.init()

        self.__screen=pygame.display.set_mode([Config.screen_width,Config.screen_height],0,32)
        pygame.display.set_caption(Config.game_name)

        self.__walking_image=pygame.image.load(os.path.join(*Config.image_path)).convert_alpha()
    
        self.__image=pygame.transform.scale(self.__walking_image,(Config.image_width,Config.image_height))
        self.__walking_frames=[]
        for i in range(10):
            self.__walking_frames.append(self.__walking_image.subsurface((i*64,0,64,128)))
        self.__standing_frame=self.__walking_image.subsurface((256,0,64,64))
    
        self.running=False

    def run(self):
        self.__running=True
        self.__clock=pygame.time.Clock()
        while self.__running:
            self.__clock.tick(60)
            self.__process_events()
            self.__update()
            self.__render()
    
        self.quit()
    
    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running=False

    def __update(self):
        if Config.direction == "right":
            Config.x += Config.vel
            if Config.x > Config.screen_width-64:
                Config.direction = "left"
        elif Config.direction == "left":
            Config.x -= Config.vel
            if Config.x < 0:
                Config.direction = "right"

    def __render(self):
        if Config.direction == "right":
            frame = self.__walking_frames[int(pygame.time.get_ticks()/100) % 10]
        elif Config.direction == "left":
            frame = pygame.transform.flip(self.__walking_frames[int(pygame.time.get_ticks()/100) % 10], True, False)

        self.__screen.fill(Config.background_color)
        self.__screen.blit(frame,(Config.x,Config.y))
        pygame.display.update()

    def quit(self):
        pygame.quit()