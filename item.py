import pygame as pg

class Item:
    def __init__(self,game,x,y):
        self.game = game
        self.rect = pg.Rect(x-10,y-10,20,20)
        self.not_eat = True
    def update(self):
        if self.not_eat and self.rect.colliderect(self.game.player.rect):
            self.game.player.health = min(self.game.player.health+20,100)
            self.not_eat = False
    def scroll(self,shilf1,shilf2):
        self.rect.x+=shilf1
        self.rect.y+=shilf2
    def draw(self):
        if self.not_eat:
            pg.draw.circle(self.game.screen,'green',(self.rect.x,self.rect.y),10)