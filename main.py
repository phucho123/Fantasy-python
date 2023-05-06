import pygame as pg
import sys
from map import *
from player import *
from npc import *
from menu import *
from item import *

WIN = (1000,640)
FPS = 60

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Knight vs Monster')
        self.screen = pg.display.set_mode(WIN)
        self.level = 0
        self.clock = pg.time.Clock()
        self.new_game()
        self.menu = Menu(self)
        self.start_game = False
    def new_game(self):
        self.gameover = False
        self.map = Map(self)
        self.npcs = []
        self.hps = []
        self.get_player()
        self.get_npcs()
    def get_npcs(self):
        for i,row in enumerate(self.map.mini_map):
            for j,value in enumerate(row):
                if value == 'S':
                    self.npcs.append(NPC(self,(j+0.5)*64,i*64,'Skeleton'))
                elif value == 'G':
                    self.npcs.append(NPC(self,(j+0.5)*64,i*64,'Goblin'))
                elif value == 'F':
                    self.npcs.append(NPC(self,(j+0.5)*64,i*64,'Flying eye'))
                elif value == 'H':
                    self.hps.append(Item(self,(j+0.5)*64,(i+0.5)*64))
    def get_player(self):
        for i,row in enumerate(self.map.mini_map):
            for j,value in enumerate(row):
                if value == 'P':
                    self.player = Player(self,j*64,i*64)
                    break
    def draw(self):
        self.screen.fill((0,0,0))
        if not self.start_game:
            self.menu.draw()
            return
        self.map.draw()
        for hp in self.hps:
            hp.draw()
        for npc in self.npcs:
            npc.draw()
        self.player.draw()
        if self.player.health == 0:
            self.gameover = True
            self.menu.draw_gameover()
        self.menu.draw_level()
        pg.display.update()
    def update(self):
        self.player.update()
        for hp in self.hps:
            hp.update()
    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if e.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if not self.start_game and pos[0]>self.menu.play_button_rect.left and pos[0] < self.menu.play_button_rect.right and pos[1]>self.menu.play_button_rect.top and pos[1] < self.menu.play_button_rect.bottom:
                        self.start_game = True
                    if self.gameover and pos[0]>self.menu.restart_rect.left and pos[0] < self.menu.restart_rect.right and pos[1]>self.menu.restart_rect.top and pos[1] < self.menu.restart_rect.bottom:
                        self.menu.time = pg.time.get_ticks()
                        self.new_game()
            self.update()
            self.draw()
            self.clock.tick(FPS)

game = Game()
game.run()