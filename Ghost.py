import pygame
import random
class Ghost:

    def __init__(self,gh,speed,maxLimit):
        self.type = gh['type']
        self.pos = [gh['pos'][0],gh['pos'][1]]
        self.speed = speed
        self.interval = speed
        self.limit = maxLimit -1
        self.direction = 1
        self.img = None

    def getinfo(self):
        print(self.type)
        print(self.pos)
        print(self.speed)
        print(self.interval)
        print(self.limit)

    def Haunt(self,curTime):
        if curTime > self.interval:
            if self.type == 'V':
                self.getNextPosV()
            else:
                self.getNextPosH()
            
            self.interval += self.speed

            return True,self.pos
        return False,self.pos

    def getNextPosH(self):
        if self.pos[1] < self.limit and self.pos[1] > 0:
            self.pos[1] += self.direction
        else:
            self.pos[1] -= self.direction
            self.direction = 0-(self.direction)

    def getNextPosV(self):
        if self.pos[0] < self.limit and self.pos[0] > 0:
            self.pos[0] += self.direction
        else:
            self.pos[0] -= self.direction
            self.direction = 0-self.direction
    
    def getSprite(self):
        #choose random image for ghost
        if self.img == None:
            s = 'Images/ghosts/ghost' + str(random.randint(1,4)) + '.png'
            self.img = pygame.image.load(s)
        return self.img
        
        '''
        if self.type == 'V':
            return pygame.image.load('Images/ghosts/ghost1.png')
        else:
            return pygame.image.load('Images/ghosts/ghost2.png')
        '''