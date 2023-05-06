import pygame as pg


class Menu:
    def __init__(self,game):
        self.game = game
        self.name_of_game = pg.font.SysFont('arial',100)
        self.name_of_game_surf = self.name_of_game.render('Knight vs Monster',False,(0,0,255))
        self.name_of_game_rect = self.name_of_game_surf.get_rect(center = (500,200))

        self.play_button = pg.font.SysFont('arial',100)
        self.play_button_surf = self.play_button.render('Play',False,(255,255,255))
        self.play_button_rect = self.play_button_surf.get_rect(center = (500,350))

        self.game_over_font = pg.font.SysFont('arial',100)
        self.game_over_surf = self.game_over_font.render('GAME OVER',False,(255,0,0))
        self.game_over_rect = self.game_over_surf.get_rect(center = (500,200))

        self.restart_font = pg.font.SysFont('arial',70)
        self.restart_surf = self.restart_font.render('Restart',False,(0,0,255))
        self.restart_rect = self.restart_surf.get_rect(center = (500,350))

        self.level_font = pg.font.SysFont('arial',50)
        self.level_surf = self.restart_font.render(f'Level {str(self.game.level+1)}',False,'red')
        self.level_rect = self.restart_surf.get_rect(center = (500,200)) 

        self.time = pg.time.get_ticks()

    def draw(self): 
        self.game.screen.blit(self.name_of_game_surf,self.name_of_game_rect)
        self.game.screen.blit(self.play_button_surf,self.play_button_rect)
        pg.display.update()

    def draw_gameover(self):
        self.game.screen.blit(self.game_over_surf,self.game_over_rect)
        self.game.screen.blit(self.restart_surf,self.restart_rect)
        # pg.display.update()
    def draw_level(self):
        if pg.time.get_ticks()-self.time < 3000:
            self.game.screen.blit(self.level_surf,self.level_rect)
