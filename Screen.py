import pygame
from pygame.locals import *
import sys


# from Credit import Credit
from Level import Level
from Player import Player
from Theme import Theme
from Ghost import Ghost

#FONT and color collection 
class Screen:
    
    def __init__(self,displaySurf,winWidth,winHeight):
        self.DISPLAYSURF = displaySurf
        self.WINWIDTH = winWidth
        self.WINHEIGHT = winHeight
#         self.credit_instance = Credit(displaySurf,winWidth,winHeight)
        self.goalStar = pygame.image.load('Images/Theme/Star.png')
        self.Clock = pygame.time.Clock()

        self.TILEWIDTH = 50
        self.TILEHEIGHT = 85
        self.TILEFLOORHEIGHT = 40

        self.GameOver = pygame.mixer.Sound('audio/pew_pew.wav')
         

    def starts(self):
        #first display logo for 2 sec(2000 miliseconds)
        self.fullScreenImageDisplay('Images/credit/logo.png',halt=2000)
        theme_no,playerSprite_no = self.Selection()
        theme_no,playerSprite_no = self.Selection(theme_no,playerSprite_no,False)

        return theme_no,playerSprite_no
    
    def runLevels(self,theme_no,playerSprite_no):
        self.level = Level("level/MazePuzzle.txt")
        no_levels = self.level.levelInfo()[1]
        for i in range(no_levels):
            passed = self.runLevel(self.level.getCurLevelObj(),theme_no,playerSprite_no)
            if passed == False:
                break
            self.level.gotoNextLevel()
        
        #if last level is complete show congratulations
        if passed:
            self.fullScreenImageDisplay('Images/Credit/Congratulations.png',halt=2500,BGCOLOR=None)
            return True
        else:
            self.fullScreenImageDisplay('Images/Credit/replay.png',halt=2500,BGCOLOR=None)
            return False

    
    def Credits(self):
        self.fullScreenImageDisplay('Images/credit/Final.png',halt=5000)
        self.fullScreenImageDisplay('Images/credit/END.png',halt=5000)

    def fullScreenImageDisplay(self,imagePath,halt=1500,BGCOLOR=(255,255,255)):
        if BGCOLOR !=None:
            self.DISPLAYSURF.fill(BGCOLOR)
        xImg1 = pygame.image.load(imagePath)
        xImg = xImg1.get_rect()
        xImg.centerx = int(self.WINWIDTH/2)
        xImg.centery = int(self.WINHEIGHT/2)
        self.DISPLAYSURF.blit(xImg1,xImg)
        pygame.display.update()
        pygame.time.wait(halt)

    def story(self,playerSprite_no,story,BGCOLOR=(0,170,255),speed=250,waitKey=True):
        
        self.DISPLAYSURF.fill(BGCOLOR)
        playerSprite = list(Player.CharacterSprites.values())[playerSprite_no]
        
        playerSprite = pygame.transform.scale(playerSprite,(150,150))

        playerSprite1 = playerSprite.get_rect()
        playerSprite1.centerx = int(self.WINWIDTH/2)
        playerSprite1.centery = int(self.WINHEIGHT/2)


        self.DISPLAYSURF.blit(playerSprite,playerSprite1)

        
        boxImg = pygame.image.load('Images/dialogue/box150.png')
        boxImg1 = boxImg.get_rect()
        boxImg1.bottomleft = (0,self.WINHEIGHT)
        #self.DISPLAYSURF.blit(boxImg,boxImg1)
        pygame.display.update()

        
        Font = Theme.getStoryFont()
        for i in story:
            Sentence = ""
            for j in i.split(' '):
                Sentence = Sentence + ' '+j
                self.DISPLAYSURF.blit(boxImg,boxImg1)
                line = Font.render(Sentence,1,(255,255,0))
                lineRect = line.get_rect()
                lineRect.center = (int(self.WINWIDTH/2),self.WINHEIGHT-75)
                self.DISPLAYSURF.blit(line,lineRect)
                pygame.time.wait(speed)
                pygame.display.update()
            if waitKey:
                _ = self.waitKeyPressed()
                




    def waitKeyPressed(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    return event.key
        return None


    def Selection(self,theme_no=0,playerSprite_no=0,themeSelect = True):
        themelevel = Level("level/themeLevel.txt")
        BGCOLOR = (0,170,255)
        self.DISPLAYSURF.fill(BGCOLOR)
        mapSurf = self.drawMap(themelevel.getCurLevelObj(),Theme.Themes[theme_no])
        mapSurf = self.drawCharacter(mapSurf,list(Player.CharacterSprites.values())[playerSprite_no],themelevel.getCurLevelObj()['Start'])
        Font = Theme.getTitleFont()

        if themeSelect:
            themeText = Font.render('Select Theme',1,(25,25,25))
        else:
            themeText = Font.render('Select Character',1,(25,25,25))
        themeTextRect = themeText.get_rect()
        themeTextRect.center = (self.WINWIDTH/2,90)
        self.DISPLAYSURF.blit(themeText,themeTextRect)
        
        Font2 = Theme.getInfoFont()
        #text below selection
        belowText = Font2.render('<<- use Arrow keys to change ->>',1,(0,0,0))
        belowTextRect = belowText.get_rect()
        belowTextRect.center = (self.WINWIDTH/2,self.WINHEIGHT-150)
        self.DISPLAYSURF.blit(belowText,belowTextRect)

        belowText2 = Font2.render('[Press Enter to select]',1,(0,0,0))
        belowTextRect2 = belowText2.get_rect()
        belowTextRect2.center = (self.WINWIDTH/2,self.WINHEIGHT-120)
        self.DISPLAYSURF.blit(belowText2,belowTextRect2)

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (self.WINWIDTH/2,self.WINHEIGHT/2)
        self.DISPLAYSURF.blit(mapSurf,mapSurfRect)

        pygame.display.update()
        
        while True:
            Move = None
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    KeyPressed = True
                    if event.key == K_LEFT or event.key == K_DOWN:
                        if themeSelect:
                            theme_no = (theme_no + 1)%len(Theme.Themes)
                        playerSprite_no = (playerSprite_no + 1) % len(Player.CharacterSprites)
                    elif event.key == K_RIGHT or event.key == K_UP:
                        if themeSelect:
                            theme_no = (theme_no + 1)%len(Theme.Themes)
                        playerSprite_no = (playerSprite_no + 1) % len(Player.CharacterSprites)
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_RETURN:
                        return theme_no,playerSprite_no
                    
                    
                    mapSurf = self.drawMap(themelevel.getCurLevelObj(),Theme.Themes[theme_no])
                    mapSurf = self.drawCharacter(mapSurf,list(Player.CharacterSprites.values())[playerSprite_no],themelevel.getCurLevelObj()['Start'])

                    mapSurfRect = mapSurf.get_rect()
                    mapSurfRect.center = (self.WINWIDTH/2,self.WINHEIGHT/2)
                    self.DISPLAYSURF.blit(mapSurf,mapSurfRect)
                    pygame.display.update()




    def runLevel(self,levelObj,theme_no=0,playerSprite_no=0):
        
        #set font and theme
        DisplayFont = Theme.getInfoFont()
        selectedTheme,selectedPlayer = Theme.Themes[theme_no],list(Player.CharacterSprites.values())[playerSprite_no]
        
        #get level no and total levels in level_no tuple
        level_no = self.level.levelInfo()
        MapRefresh = True
        LevelCompleted = False

        #initialize all current level ghosts with speeds
        cur_ghosts = []
        
        for i in levelObj['Ghosts']:
            if i['type'] == 'V':
                tmpGhost = Ghost(i,1.0,len(levelObj['map']))
            else:
                tmpGhost = Ghost(i,1.0,len(levelObj['map'][0]))
            cur_ghosts.append(tmpGhost)
            tmpGhost.getinfo()


        self.DISPLAYSURF.fill(Theme.Colors['LIGHTBLUE'])
        
        
        levelSurf = DisplayFont.render('Level %s of %s' % level_no, 1, Theme.Colors['BLACK'])
        levelRect = levelSurf.get_rect()
        levelRect.bottomleft = (20, self.WINHEIGHT - 35)
        self.DISPLAYSURF.blit(levelSurf,levelRect)

        mapSurf = self.drawMap(levelObj,selectedTheme)
        mapSurf = self.drawCharacter(mapSurf,selectedPlayer,levelObj['Start'])
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (self.WINWIDTH/2,self.WINHEIGHT/2)
        self.DISPLAYSURF.blit(mapSurf,mapSurfRect)
        pygame.display.update()
        self.Clock.tick()
        time_passed = 0.0
        levelPass = True
        #main game loop for level
        while not LevelCompleted:
            Move = None
            KeyPressed = True


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    KeyPressed = True
                    if event.key == K_LEFT:
                        Move = 'left'
                    elif event.key == K_RIGHT:
                        Move = 'right'
                    elif event.key == K_UP:
                        Move = 'up'
                    elif event.key == K_DOWN:
                        Move = 'down'
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.DISPLAYSURF.fill(Theme.Colors['LIGHTBLUE'])
            timeSec = time_passed/1000.0
            if Move != None and not LevelCompleted:
                moved,levelObj,LevelCompleted = self.level.makeMove(Move)
            #print(moved,levelObj,LevelCompleted)
            mapSurf = self.drawMap(levelObj,selectedTheme)
            mapSurf = self.drawCharacter(mapSurf,selectedPlayer,levelObj['Start'])
                
                
            #check each ghost if moved and get new position
            for ghst in cur_ghosts:
                mvd,pos = ghst.Haunt(timeSec)
                ghstSprite = ghst.getSprite()
                mapSurf = self.drawCharacter(mapSurf,ghstSprite,pos)
                if pos == list(levelObj['Start']):
                    LevelCompleted = True
                    levelPass = False
                    self.GameOver.play()




                
            
            
            levelSurf = DisplayFont.render('Level %s of %s' % level_no, 1, Theme.Colors['BLACK'])
            levelRect = levelSurf.get_rect()
            levelRect.bottomleft = (20, self.WINHEIGHT - 35)
            self.DISPLAYSURF.blit(levelSurf,levelRect)
            
            
            timeText =  DisplayFont.render('Time %s' % int(timeSec), 1, Theme.Colors['BLACK'])
            timeRect = timeText.get_rect()
            timeRect.topright = (self.WINWIDTH-20,35)
            self.DISPLAYSURF.blit(timeText,timeRect)
            
            #mapSurf = pygame.transform.scale(mapSurf,(400,500))
            mapSurfRect = mapSurf.get_rect()
            mapSurfRect.center = (self.WINWIDTH/2,self.WINHEIGHT/2)
            self.DISPLAYSURF.blit(mapSurf,mapSurfRect)
            pygame.display.update()

            time_passed += self.Clock.tick()
        return levelPass
    
    def drawCharacter(self,mapSurf,characterSprite,position):
        i,j = position
        characterSpriteRect = pygame.Rect((j*self.TILEWIDTH,i*self.TILEFLOORHEIGHT,self.TILEWIDTH,self.TILEHEIGHT))
        mapSurf.blit(characterSprite,characterSpriteRect)
        return mapSurf

    def drawMap(self,levelObj,theme):
        BGCOLOR = (  0, 170, 255)

        mapSurfHeight = (len(levelObj['map'])-1) * self.TILEFLOORHEIGHT + self.TILEHEIGHT
        mapSurfWidth = len(levelObj['map'][0])*self.TILEWIDTH
        mapSurf = pygame.Surface((mapSurfWidth,mapSurfHeight))
        mapSurf.fill(BGCOLOR)

        k,l = 0,0

        # iterate through map and create graphics on mapSurf(MapSurface) 
        for i in range(len(levelObj['map'])):
            for j in range(len(levelObj['map'][0])):
                spriteRect = pygame.Rect((j*self.TILEWIDTH,i*self.TILEFLOORHEIGHT,self.TILEWIDTH,self.TILEHEIGHT))
                if levelObj['map'][i][j] == '#' :
                    baseTile = theme['#'][k]
                    k = (k+1)%len(theme['#'])
                else:
                    baseTile = theme[' '][l]
                    l = (l+1)%len(theme[' '])
                
                mapSurf.blit(baseTile,spriteRect)
                '''
                if (i,j) == levelObj['Start']:
                    mapSurf.blit(playerSprite, spriteRect)'''
                if (i,j) == levelObj['Goal']:
                    mapSurf.blit(self.goalStar,spriteRect)
        
        return mapSurf
