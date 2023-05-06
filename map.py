import pygame as pg

mini_map = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                    FF H                      X',
    'X     GG         XXXXXXXXX        F            X',
    'X  XXXXXXXX                   XXXXXXXX         X',
    'X                     S               XXXX     X',
    'X        S        XXXXXXXXX                 XXXX',
    'X      XXXXXX                 XXXX     S F     X',
    'X    GH                             XXXXXXX    X',
    'X  XXXXXXX            FFFH                     X',
    'X                  XXXXXXXXXX             XX   X',
    'X      F                              XX       X',
    'X   XXXXXXX                     S           XX X',
    'X                    GF      XXXXXXX           X',
    'X         S       XXXXXXXX              XX    XX',
    'X      XXXXXXX                   H           XXX',
    'X               G               XXXX           X',
    'X P           XXXXX             S           H  X',
    'XXXXXXXXXX                   XXXXXXXX     XXXXXX',
    'XXXXXXXXXXX                       XXXXX       XX',
    'XXXXXXXXXXXXX           G  F  G     XXXX   XXXXX',
    'XXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXX   XXXXXX',
    'XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXX      XXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX    S     G   G    XXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]
tile_size = 64
class Map:
    def __init__(self,game):
        self.mini_map = mini_map
        self.tile_size = tile_size 
        self.game = game
        self.tiles = []
        self.get_tiles() 
    def get_tiles(self):
        for i,row in enumerate(self.mini_map):
            for j,value in enumerate(row):
                if value == 'X':
                    self.tiles.append(Tile(j*self.tile_size,i*self.tile_size))
    def update(self,shilf1,shilf2):
        for tile in self.tiles:
            tile.update(shilf1,shilf2)
    def draw(self):
        for tile in self.tiles:
            tile.draw(self.game.screen)
class Tile:
    def __init__(self,x,y):
        self.tile_size = tile_size
        self.rect = pg.Rect(x,y,self.tile_size,self.tile_size)
        # self.tile_image = pg.image.load('Image/Background/tile.png').convert()
        # self.tile_image = pg.transform.scale(self.tile_image,(64,64))
        # self.tile_image.set_colorkey((0,0,0))
    def update(self,shilf1,shilf2):
        self.rect.x+=shilf1
        self.rect.y+=shilf2
    def draw(self,screen):
        pg.draw.rect(screen,'darkgray',self.rect)
        # screen.blit(self.tile_image,self.rect)