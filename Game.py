import pygame
import Screen
import sys
from Theme import Theme

class Game:

    def __init__(self,width=800,height=600):
        pygame.init()
        self.WINWIDTH = width
        self.WINHEIGHT = height
        self.HALF_WINWIDTH = int(width/2)
        self.HALF_WINHEIGHT = int(height/2)
        
        self.FPSLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINWIDTH,self.WINHEIGHT))
        self.DISPLAYSURF.fill((205,255,255))
        


    def play(self):
        pygame.init()
        pygame.mixer.music.load('audio/ipsi.mp3')
        pygame.mixer.music.play(-1)
        scr=Screen.Screen(self.DISPLAYSURF,self.WINWIDTH,self.WINHEIGHT)
        theme_no,plyr_no = scr.starts()
        scr.story(plyr_no,Theme.mainStory)
        completed = False
        while not completed:
            completed = scr.runLevels(theme_no,plyr_no)
            if not completed:
                scr.story(plyr_no,Theme.retryStory,speed=300)
        scr.story(plyr_no,Theme.thankYouStory,speed=300)
        scr.Credits()

    def GameExit():
        pygame.quit()
        sys.exit()
    

