import pygame as pg
import math
from animation import *

class NPC:
    def __init__(self,game,x,y,type):
        self.game = game
        self.rect = pg.Rect(x,y,50,50)
        self.y_speed = 0
        self.dir = 1
        self.speed = 1
        self.gravity = 0.8
        self.type = type
        self.action = []
        self.get_action()
        self.attack_animation = NPC_Animation(self,'Image/'+type+'/Attack.png',self.action[0])
        self.walk_animation = NPC_Animation(self,'Image/'+type+'/Walk.png',self.action[1])
        self.takehit_animation = NPC_Animation(self,'Image/'+type+'/Take Hit.png',self.action[2])
        self.death_animation = NPC_Animation(self,'Image/'+type+'/Death.png',self.action[3])
        self.time = pg.time.get_ticks()
        self.health = 100
        self.attack = False
    def get_action(self):
        if self.type == 'Skeleton':
            self.action = [8,4,4,4]
        elif self.type == 'Goblin':
            self.action = [8,8,4,4]
        elif self.type == 'Flying eye':
            self.action = [8,8,4,4]
    def update(self):
        self.x_moverment()
        self.y_moverment()
    def scroll(self,shilf1,shilf2):
        self.rect.x+=shilf1
        self.rect.y+=shilf2
    def x_moverment(self):
        self.rect.x+=self.speed*self.dir
        for tile in self.game.map.tiles:
            if self.rect.colliderect(tile.rect):
                if self.dir > 0:
                    self.rect.right = tile.rect.left
                elif self.dir < 0:
                    self.rect.left = tile.rect.right
        if pg.time.get_ticks()-self.time > 3000 and self.speed != 0:
            self.dir = -self.dir
            self.time = pg.time.get_ticks()
    def y_moverment(self):
        self.y_speed+=self.gravity
        self.rect.y+=self.y_speed
        for tile in self.game.map.tiles:
            if self.rect.colliderect(tile.rect):
                if self.y_speed>0:
                    self.rect.bottom = tile.rect.top
                    self.y_speed = 0
                elif self.y_speed < 0:
                    self.rect.top = tile.rect.bottom
                    self.y_speed = 0
    def draw(self):
        self.update()
        if self.health == 0:
            self.death_animation.draw()
            self.speed = 0
            self.dir = 0
            self.attack = False
            return
        # pg.draw.rect(self.game.screen,'red',self.rect)
        dist = math.hypot(self.rect.centerx-self.game.player.rect.centerx,self.rect.centery-self.game.player.rect.centery)
        dir = (self.game.player.rect.x-self.rect.x)*self.game.player.dir
        if dist < 150 and self.game.player.health > 0:
            if self.rect.x < self.game.player.rect.x:
                self.dir = 1
            else: self.dir = -1
        if self.game.player.attack and dist < 80 and dir < 0:
            self.takehit_animation.draw()
            self.speed = 0
            # if self.rect.x < self.game.player.rect.x:
            #     self.dir = 1
            # else: self.dir = -1
            if self.game.player.attack_animation.frame == self.game.player.attack_animation.num_frame-1:
                self.health = max(self.health-3,0)
        else: self.speed = 1
        dir = (self.rect.x-self.game.player.rect.x)*self.dir
        dist2 = 80
        if self.type == 'Goblin':
            dist2 = 50
        elif self.type == 'Flying eye':
            dist2 = 40
        if dist < dist2 and dir < 0 and self.game.player.health > 0:
            self.attack_animation.draw()
            self.speed = 0
            self.attack = True
        else:
            self.speed = 1
            self.attack = False
        if self.speed != 0:
            self.walk_animation.draw()
        self.draw_health_bar()
    def draw_health_bar(self):
        pg.draw.rect(self.game.screen,'red',(self.rect.x,self.rect.y-5,self.rect.width,2))
        blood = self.health/100*self.rect.width
        pg.draw.rect(self.game.screen,'green',(self.rect.x,self.rect.y-5,blood,2))
