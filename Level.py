import os
class Level:
    def __init__(self,filename):
        self.curlevel = 0
        self.levels = Level.readlevels(filename)


    def getCurLevel(self):
        return self.curlevel
    
    def getLevels(self):
        return self.levels
    
    def getCurLevelObj(self):
        return self.levels[self.curlevel]
    
    def gotoNextLevel(self):
        if (self.curlevel-1) < len(self.levels):
            self.curlevel += 1
    
    def levelInfo(self):
        return (self.getCurLevel()+1,len(self.levels))

    def readlevels(filename):
        assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
        mapFile = open(filename,'r')
        content = mapFile.readlines() + ['\r\n']
        mapFile.close()
        
        # dictionary of levels
        levels = {}
        #current processing Level in loop
        curLevel = 0
        #current level Map in list
        clevelMap = []
        
        for lineNum in range(len(content)):
            line = content[lineNum].rstrip('\r\n')
            if 'i' in line:
                pass
            elif len(line) > 0 :
                letters = []
                for i in line:
                    letters.append(i)
                clevelMap.append(letters)
            elif line == '' and len(clevelMap) > 0:
                levels[curLevel] = {}
                levels[curLevel]['Ghosts'] = []
                for i in range(len(clevelMap)):
                    
                    g_count = 0
                    if 'S' in clevelMap[i]:
                        levels[curLevel]['Start'] = (i,clevelMap[i].index('S'))
                        clevelMap[i][clevelMap[i].index('S')] = ' '
                    
                    if 'G' in clevelMap[i]:
                        levels[curLevel]['Goal'] = (i,clevelMap[i].index('G'))
                        g_count += 1
                    if (g_count + clevelMap[i].count(' ') + clevelMap[i].count('#')) != len(clevelMap[i]):
                        for letr_no in range(len(clevelMap[i])):
                            if clevelMap[i][letr_no] in ['V','H']:
                                tmp = {}
                                tmp['type'] = clevelMap[i][letr_no]
                                tmp['pos'] = (i,letr_no)
                                levels[curLevel]['Ghosts'].append(tmp)
                                clevelMap[i][letr_no] = ' '
                # make all line with same length by adding space at end
                maxLen = len(max(clevelMap,key= lambda i: len(i)))
                for i in range(len(clevelMap)):
                    if len(clevelMap[i]) < maxLen :
                        clevelMap[i] += (maxLen-len(clevelMap[i])) *" "
                
                
                levels[curLevel]['map'] = clevelMap
                try:
                    assert 'Start' in levels[curLevel].keys(), 'Cannot Find Start State for player in level %d' % (curLevel)
                    assert 'Goal' in levels[curLevel].keys(), 'Cannot Find Goal State for player in level %d' % (curLevel)
                except AssertionError as error:
                    print(error)
                    levels[curLevel] = {}
                    curLevel -= 1
                clevelMap = []
                curLevel += 1
        return levels
    
    def makeMove(self,Move):
        level = self.getCurLevelObj()
        x,y = level['Start']
        
        if Move == 'left':
            y -= 1
        elif Move == 'right':
            y += 1
        elif Move == 'up':
            x -= 1
        else:
            x += 1
        
        if x < 0 or y < 0 or x >= len(level['map']) or y >= len(level['map'][0]):
            return False,level,False

        if level['map'][x][y] == 'G' :
            return True,level,True
        
        if level['map'][x][y] == ' ':
            level['Start'] = (x,y)
            return True,level,False
        
        return False,level,False