import pygame as pg

class Player_Animation:
    def __init__(self,player,path,num_frame):
        self.player = player
        self.path = path
        self.sprites = pg.image.load(path).convert_alpha()
        self.width,self.height = 120,80
        self.animate_time = pg.time.get_ticks()
        self.num_frame = num_frame
        self.frame = 0
        self.images = []
        self.flip = False
        self.get_images()
    def get_images(self):
        if '_Attack' in self.path:
            tmp = 3
        else: tmp = 10
        for i in range(self.num_frame):
            image = self.sprites.subsurface(i*self.width,0,self.width-tmp,self.height).convert_alpha()
            image = pg.transform.scale(image,(1.3*self.width,1.3*self.height))
            self.images.append(image)
    def draw(self):
        if self.player.dir>0:
            self.flip = False
        elif self.player.dir<0:
            self.flip = True
        if pg.time.get_ticks() - self.animate_time > 50:
            if '_Death' in self.path and self.frame == self.num_frame-1:
                self.frame = self.num_frame-1
            else: self.frame = (self.frame+1)%self.num_frame
            self.animate_time = pg.time.get_ticks()
        tmp = pg.transform.flip(self.images[self.frame],self.flip,False)
        self.player.game.screen.blit(tmp,(self.player.rect.x-63,self.player.rect.y-54,self.width,self.height))


class NPC_Animation:
    def __init__(self,npc,path,num_frame):
        self.npc = npc
        self.path = path
        self.num_frame = num_frame
        self.sprites = pg.image.load(self.path).convert_alpha()
        self.images = []
        self.width,self.height = 150,150
        self.frame = 0
        self.time_animation = pg.time.get_ticks()
        self.get_images()
    def get_images(self):
        k = 15
        if 'Goblin' in self.path:
            k = 5
        elif 'Flying eye' in self.path:
            k = 5
        for i in range(self.num_frame):
            image = self.sprites.subsurface(i*self.width+k,0,self.width-k,self.height).convert_alpha()
            self.images.append(image)
    def draw(self):
        if pg.time.get_ticks()-self.time_animation > 50:
            if 'Death' in self.path and self.frame == self.num_frame-1:
                self.frame = self.num_frame-1
            else: self.frame = (self.frame+1)%self.num_frame
            self.time_animation = pg.time.get_ticks()
        tmp = self.images[self.frame]
        if self.npc.dir < 0:
            tmp = pg.transform.flip(tmp,True,False)
        self.npc.game.screen.blit(tmp,(self.npc.rect.x-45,self.npc.rect.y-50,self.width,self.height))
