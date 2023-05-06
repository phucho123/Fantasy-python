import pygame as pg
from animation import *

class Player:
    def __init__(self,game,x,y):
        self.game = game
        self.max_speed = 8
        self.width,self.height = 30.0,50.0
        self.rect = pg.Rect(x,y,self.width,self.height)
        self.speed = 0
        self.dir = 0
        self.jump = -20
        self.gravity = 0.8
        self.y_speed = 0
        self.tile_size = self.game.map.tile_size
        self.attack = False
        self.health = 100
        self.can_jump = False
        self.idle_animation = Player_Animation(self,'Image/_Idle.png',10)
        self.run_animation = Player_Animation(self,'Image/_Run.png',10)
        self.jump_animation = Player_Animation(self,'Image/_Jump.png',3)
        self.fall_animation = Player_Animation(self,'Image/_Fall.png',3)
        self.attack_animation = Player_Animation(self,'Image/_Attack.png',4)
        self.takehit_animation = Player_Animation(self,'Image/_Hit.png',1)
        self.death_animation = Player_Animation(self,'Image/_Death.png',10)
    def update(self):
        if self.health > 0:
            self.move()
            self.x_moverment()
        self.y_moverment()
    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.dir = -1
            self.speed = -self.max_speed
        elif key[pg.K_d]:
            self.dir = 1
            self.speed = self.max_speed
        else:
            self.speed = 0
        if key[pg.K_w] and self.can_jump:
            self.y_speed = self.jump
            self.can_jump = False
        if key[pg.K_SPACE]:
            self.attack = True
        else:
            self.attack = False
        # if key[pg.K_DOWN]:
        #     if self.crouch == False:
        #         self.rect.y+=10
        #         self.rect.height = 30.0
        #     self.crouch = True
        # else:
        #     if self.crouch == True:
        #         self.rect.y-=10
        #         self.rect.height = 40.0
        #     self.crouch = False
    def x_moverment(self):
        self.rect.x+=self.speed
        if self.rect.x > 750 and self.dir > 0:
            self.game.map.update(-self.speed,0)
            for npc in self.game.npcs:
                npc.scroll(-self.speed,0)
            for hp in self.game.hps:
                hp.scroll(-self.speed,0)
            self.rect.x -= self.speed
        elif self.rect.x < 250 and self.dir < 0:
            self.game.map.update(-self.speed,0)
            for npc in self.game.npcs:
                npc.scroll(-self.speed,0)
            for hp in self.game.hps:
                hp.scroll(-self.speed,0)
            self.rect.x -= self.speed
        for tile in self.game.map.tiles:
            if self.rect.colliderect(tile.rect):
                if self.dir > 0:
                    self.rect.right = tile.rect.left
                elif self.dir < 0:
                    self.rect.left = tile.rect.right
    def y_moverment(self):
        self.y_speed+=self.gravity
        self.rect.y+=self.y_speed
        for tile in self.game.map.tiles:
            if self.rect.colliderect(tile.rect):
                if self.y_speed>0:
                    self.rect.bottom = tile.rect.top
                    self.y_speed = 0
                    self.can_jump = True
                elif self.y_speed < 0:
                    self.rect.top = tile.rect.bottom
                    self.y_speed = 0
        # tmp = self.rect.y-500
        # self.rect.y = 500
        # self.game.map.update(0,-tmp)
        if self.rect.centery < 0:
            self.game.map.update(0,500)
            for npc in self.game.npcs:
                npc.scroll(0,500)
            for hp in self.game.hps:
                hp.scroll(0,500)
            self.rect.centery+=500
        elif self.rect.centery > 600:
            self.game.map.update(0,-500)
            for npc in self.game.npcs:
                npc.scroll(0,-500)
            for hp in self.game.hps:
                hp.scroll(0,-500)
            self.rect.centery-=500
    def draw_health_bar(self):
        pg.draw.rect(self.game.screen,'red',(self.rect.x-20,self.rect.y-5,self.rect.width+40,2))
        blood = self.health/100*(self.rect.width+40)
        pg.draw.rect(self.game.screen,'green',(self.rect.x-20,self.rect.y-5,blood,2))
    def draw(self):
        # pg.draw.rect(self.game.screen,'green',self.rect)
        # self.takehit_animation.draw()
        if self.health == 0:
            self.attack = False
            self.death_animation.draw()
            return
        for npc in self.game.npcs:
            if npc.attack and npc.attack_animation.frame == npc.attack_animation.num_frame-1:
                self.health = max(self.health-0.5,0)
                # self.takehit_animation.draw()
                # return
        self.draw_health_bar()
        if self.attack:
            self.attack_animation.draw()
        elif self.y_speed < 0:
            self.jump_animation.draw()
        elif self.y_speed > 0.8:
            self.fall_animation.draw()
        elif self.speed != 0:
            self.run_animation.draw()
        else:
            self.idle_animation.draw()
    