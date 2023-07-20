import pygame

class Theme:
    WallGraphics = {
        'Rock'              : pygame.image.load('Images/Theme/Rock.png'),
        'TreeShort'         : pygame.image.load('Images/Theme/Tree_Short.png'),
        'TreeTall'          : pygame.image.load('Images/Theme/Tree_Tall.png'),
        'TreeUgly'          : pygame.image.load('Images/Theme/Tree_Ugly.png'),
        'WallBlockTall'     : pygame.image.load('Images/Theme/Wall_Block_Tall.png'),
        'WoodBlockTall'     : pygame.image.load('Images/Theme/Wood_Block_Tall.png')
    }

    PathGraphics = {
        'GrassBlock'    : pygame.image.load('Images/Theme/Grass_Block.png'),
        'PlainBlock'    : pygame.image.load('Images/Theme/Plain_Block.png')
    }

    Themes = [
        { '#':[WallGraphics['TreeShort'],WallGraphics['TreeTall'],WallGraphics['TreeUgly']] ,    ' ':[PathGraphics['GrassBlock']] },
        { '#':[WallGraphics['WallBlockTall']] , ' ':[PathGraphics['PlainBlock']] },
        { '#':[WallGraphics['WoodBlockTall']] , ' ':[PathGraphics['GrassBlock']] },
        { '#':[WallGraphics['WoodBlockTall'],WallGraphics['WallBlockTall']] , ' ':[PathGraphics['GrassBlock']] }
    ]


    Colors = {
        'WHITE':(255,255,255),
        'BLACK':(0,0,0),
        'LIGHTBLUE':(0,170,255)
    }

    mainStory = [
            'Hi ! I am Minky !',
            'Evil Magician turn my friends into Stars.',
            'I need to find My Friends',
            'I cannot see further..',
            'Besides that There Magician\'s ghosts are roaming on ways.',
            'Once Einstein told me : ',
            'He can only see further because he stand on the shoulder of Giants',
            'Be my Giant and Help me !',
            'Guide me with arrow keys to reach my Star-friends.'
        ]
    
    thankYouStory = [
        'Thank you So much My FRIEND !',
        'True Friends never apart. Maybe in distance but never in heart.'
    ]
    
    retryStory = [
        'Friends are Sunshine of life. Please Try Again to find my sunshine !'
    ]

    def getTitleFont():
        return pygame.font.Font('fonts/crackman.ttf',60)
    
    def getMenuFont():
        return pygame.font.Font('fonts/halo.ttf',40)
    
    def getInfoFont():
        return pygame.font.Font('fonts/carbon.ttf',25)

    def getStoryFont():
        return pygame.font.Font('fonts/carbon.ttf',27)