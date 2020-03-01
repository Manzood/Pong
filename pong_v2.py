import pygame 
import time
import random

pygame.init() 

#The equivalent of #define in languages like c, c++
#Use this one variable to change the speed/intensity of the game at any point
#upon testing, 10 or 9 seem like the ideal values for difficulty
speed = 10
MAX_SCORE = 10

#basic initialization of all variables
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = [0, 0, 0]
yellow = [210, 212, 90]
red = [255, 0, 0]

gameDisplay = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Pong')   
clock = pygame.time.Clock()

#initialization of everything important to an FPS metre display
'''
fpsdefault = 'FPS = '
fpsfont = pygame.font.Font('freesansbold.ttf', 10)
fpstext = fpsfont.render(fpsdefault, True, white, black)
fpstextRect = fpstext.get_rect()
fpstextRect.center = (760, 10)
'''   
'''
#global variables for the FPS display function
starttime = time.time()
ticks = 0
numresets = 0
totalfps = 0
avgfps = 0
'''
#initialization of paddle positions:

paddle1x = 20
paddle1y = 235
paddle2x = 755
paddle2y = 235
middlet=399
middlel=0
ballx = 400
bally = 300


def funcmiddleline(x,y):
    middleline = pygame.Surface((2,600))
    middleline.fill(white)
    gameDisplay.blit(middleline,(x,y))
    


#function to randomly return either a 1 or a -1
def coinflip():
    r = random.randrange(-1, 2, 2)
    return r

#function to return a random number between and 0.75 (used to decide initial vertical velocity of the ball
#uses basic recursiom
def randomdecimal():
    r = 0
    while r <= (1/speed) or r > 0.75: 
        r = random.random()
    return r

playing = 0

#Function in charge of an initial (probably unnecessary) loading screen
def loadingscreen():
   
    loadingfont = pygame.font.Font('freesansbold.ttf', 200)
    loadingtext = loadingfont.render('PONG', True, white, black)
    loadingtextRect = loadingtext.get_rect()
    X = 400
    Y = 300
    loadingtextRect.center = (X, Y)
    gameDisplay.blit(loadingtext, loadingtextRect)
    starttime = time.time()
    #groundwork for a loading screen animation
    while time.time() - starttime < 2:
        gameDisplay.blit(loadingtext, loadingtextRect)
        pygame.display.update()
        
    size = 40
    change = 1
    temptime = time.time()
    
    events = pygame.event.get()
    
    global playing
    
    while playing == 0:
        
        gameDisplay.fill(black)
        
        playfont = pygame.font.Font('freesansbold.ttf', size)
        playtext = playfont.render('PLAY', True, white, black)
        playtextRect = playtext.get_rect()
        playtextRect.center = (400, 450)
        gameDisplay.blit(playtext, playtextRect)
        
        mouse = pygame.mouse.get_pos()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0]>330 and mouse[0]<470 and mouse[1]<480 and mouse[1]>410:
                    playing = 1
        
        if time.time() - temptime >= 0.1:
            size+=change
            temptime = time.time()
            #print(mouse)
            
        if size >= 45:
            change = -1
        elif size <= 40:
            change = 1
            
        if mouse[0]>330 and mouse[0]<470 and mouse[1]<480 and mouse[1]>410:
            pygame.draw.rect(gameDisplay, yellow, (330,410,3,70))
            pygame.draw.rect(gameDisplay, yellow, (330,410,140,3))
            pygame.draw.rect(gameDisplay, yellow, (330,480,140,3))
            pygame.draw.rect(gameDisplay, yellow, (470,410,3,73))
            
        gameDisplay.blit(loadingtext, loadingtextRect)
            
        pygame.display.update()
        

def endscreen(p1score,p2score):
    global playing
    playing = 0
    
    size = 30
    change = 1
    temptime = time.time()
    
    while playing == 0:
        
        gameDisplay.fill(black)
        
        endfont = pygame.font.Font('freesansbold.ttf', 40)
    
        if p1score>p2score:
            endtext = endfont.render('PLAYER 1 WINS!',True, white, black)
            endtextRect = endtext.get_rect()
            endtextRect.center = (200, 200)
            gameDisplay.blit(endtext, endtextRect)
        
        else:
            endtext = endfont.render('PLAYER 2 WINS!', True, white, black)
            endtextRect = endtext.get_rect()
            endtextRect.center = (600, 200)
            gameDisplay.blit(endtext, endtextRect)
        
        playfont = pygame.font.Font('freesansbold.ttf', size)
        playtext = playfont.render('PLAY AGAIN?', True, white, black)
        playtextRect = playtext.get_rect()
        playtextRect.center = (400, 450)
        gameDisplay.blit(playtext, playtextRect)
        
        quitfont = pygame.font.Font('freesansbold.ttf', size-2)
        quittext = quitfont.render('QUIT', True, white, black)
        quittextRect = quittext.get_rect()
        quittextRect.center = (400, 525)
        gameDisplay.blit(quittext, quittextRect)
        
        mouse = pygame.mouse.get_pos()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0]>350 and mouse[0]<450 and mouse[1]<500 and mouse[1]>400:
                    playing = 1
                if mouse[0]>330 and mouse[0]<470 and mouse[1]<555 and mouse[1]>496:
                    pygame.quit()
        
        if time.time() - temptime >= 0.1:
            size+=change
            temptime = time.time()
            #print(mouse)
            
        if size >= 35:
            change = -1
        elif size <= 30:
            change = 1
            
        if mouse[0]>330 and mouse[0]<470 and mouse[1]<480 and mouse[1]>410:
            pygame.draw.rect(gameDisplay, yellow, (270,410,3,70))
            pygame.draw.rect(gameDisplay, yellow, (270,410,260,3))
            pygame.draw.rect(gameDisplay, yellow, (270,480,260,3))
            pygame.draw.rect(gameDisplay, yellow, (530,410,3,73))
            
        if mouse[0]>330 and mouse[0]<470 and mouse[1]<555 and mouse[1]>495:
            pygame.draw.rect(gameDisplay, yellow, (345,495,3,50))
            pygame.draw.rect(gameDisplay, yellow, (345,495,110,3))
            pygame.draw.rect(gameDisplay, yellow, (345,545,110,3))
            pygame.draw.rect(gameDisplay, yellow, (455,495,3,53))
            
        gameDisplay.blit(endtext, endtextRect)
        
        pygame.display.update()

#function that displays the average FPS that the game is running on -- *NEEDS IMPROVEMENT*
def showfps():
    global ticks
    global starttime
    global avgfps
    global numresets
    global totalfps
    tensecondsago = 0

    ticks += 1
    
    if time.time() - starttime >= 1:
        #print(time.time() - starttime)
        ticks = 0
        numresets+=1
        starttime = time.time()
        
    if numresets>0:
        totalfps += ticks
        avgfps = totalfps//numresets
        
    fps = fpsdefault+ str(avgfps)
    fpstext = fpsfont.render(fps, True, white, black)
    gameDisplay.blit(fpstext, fpstextRect)
    
def scoreboard(p1score, p2score):
    p1font = pygame.font.Font('freesansbold.ttf', 90)
    p1text = p1font.render(str(p1score), True, white, black)
    p1textrect = p1text.get_rect()
    x1 = 250
    y1 = 100
    p1textrect.center = (x1, y1)
    gameDisplay.blit(p1text, p1textrect)
    
    p2font = pygame.font.Font('freesansbold.ttf', 90)
    p2text = p2font.render(str(p2score), True, white, black)
    p2textrect = p2text.get_rect()
    x2 = 550
    y2 = 100
    p2textrect.center = (x2, y2)
    gameDisplay.blit(p2text, p2textrect)

#function to draw the paddle at the specified location
def paddle1(x, y):
    #pygame.draw.rect(gameDisplay, white, (x, y, 25, 130), 1)
    paddle = pygame.Surface((26, 130))
    paddle.fill(white)
    gameDisplay.blit(paddle, (x, y))

#function to draw second paddle
def paddle2(x, y):
    paddle = pygame.Surface((26, 130))
    paddle.fill(white)
    gameDisplay.blit(paddle, (x, y))
    
#function to draw the ball at the specifed location
def ball(x, y):
    pygame.draw.circle(gameDisplay, white, (x,y), 10)

def checkCollision (ballx, bally, paddle1x, paddle1y, paddle2x, paddle2y, ballvelocityx, ballvelocityy):
    global speed
    
    if ballx >= paddle2x and ballx <= paddle2x+speed and bally > paddle2y and bally < paddle2y+130:
        ballx = paddle2x
        ballvelocityy = int(ballvelocityx *((bally - (paddle2y + 65))/65))
        ballvelocityx = -ballvelocityx
        ballx+=ballvelocityx
        
    elif ballx <= paddle1x+26 and ballx >= paddle1x + (26-speed) and bally > paddle1y and bally < paddle1y+130:
        ballx = paddle1x+26
        ballvelocityx = -ballvelocityx
        ballvelocityy = int(ballvelocityx *((bally - (paddle1y + 65))/65))
        ballx+=ballvelocityx
        
    #the following elif statements are responsible for making the ball bounce off the edges of the paddles,
    #thereby removing the glitchy feel
    elif ballx >= paddle2x+speed and ballx <= paddle2x+26 and bally >= paddle2y and bally <= paddle2y+130:
        ballvelocityy = -ballvelocityy
        bally+=ballvelocityy
        
    elif ballx <= paddle1x+26-speed and ballx >= paddle1x and bally >= paddle2y and bally <= paddle2y+130:
        ballvelocityy = -ballvelocityy
        bally+=ballvelocityy
    
    return ballx, ballvelocityx, ballvelocityy, bally
    
#Calling the loading screen function for the first and only time
loadingscreen()

#final initialization
p1score = 0 #player 1 score
p2score = 0 #player 2 score

gameDisplay.fill(black)
ball(ballx,bally)
#funcmiddleline(middlet,middlel)
paddle1(paddle1x, paddle1y)
paddle2(paddle2x, paddle2y)
scoreboard(p1score, p2score)
funcmiddleline(middlet,middlel)
pygame.display.update()
time.sleep(1)

ballvelocityx = coinflip() * speed
ballvelocityy = int(randomdecimal() * coinflip() * ballvelocityx)

#Main function, essentially (A loop that runs infintely until the quit button is pressed)
while playing: 
    gameDisplay.fill(black)
    
    #self explanatory, displays the FPS
    #showfps()
    
    scoreboard(p1score, p2score)
    funcmiddleline(middlet,middlel)
            
    keys=pygame.key.get_pressed()
    if keys[pygame.K_k]:
        if paddle2y >= 0:
            paddle2y -= speed
    if keys[pygame.K_m]:
        if paddle2y <= 470:
            paddle2y += speed
    if keys[pygame.K_a]:
        if paddle1y >= 0:
            paddle1y -= speed
    if keys[pygame.K_z]:
        if paddle1y <= 470:
            paddle1y += speed
    
    if ballx <= 810 and ballx >= -10:
        ballx += ballvelocityx
    elif ballx > 810:
        p1score+= 1
        ballx = 400
        bally = 300
        ballvelocityx = coinflip() * speed
        ballvelocityy = int(randomdecimal() * ballvelocityx)
        scoreboard(p1score, p2score)
        ball(ballx,bally)
        paddle1(paddle1x, paddle1y)
        paddle2(paddle2x, paddle2y)
        pygame.display.update()
        time.sleep(1)
    elif ballx < -10:
        p2score+=1
        ballx = 400
        bally = 300
        ballvelocityx = coinflip() * speed
        ballvelocityy = int(randomdecimal() * ballvelocityx)
        scoreboard(p1score, p2score)
        ball(ballx,bally)
        paddle1(paddle1x, paddle1y)
        paddle2(paddle2x, paddle2y)
        pygame.display.update()
        time.sleep(1)
        
    if bally < 590 and bally > 10:
        bally +=ballvelocityy
    elif bally == 590 or bally == 10:
        ballvelocityy = -ballvelocityy
        bally += ballvelocityy
    else:
        if bally > 590:
            bally = 590
        else:
            bally = 10
            
    #Checking the collision between the paddles
    ballx, ballvelocityx, ballvelocityy, bally = checkCollision(ballx, bally, paddle1x, paddle1y, paddle2x, paddle2y, ballvelocityx, ballvelocityy)
    
    ball(ballx,bally)
    paddle1(paddle1x, paddle1y)
    paddle2(paddle2x, paddle2y)
    
    if p1score == MAX_SCORE or p2score == MAX_SCORE:
        endscreen(p1score, p2score)
        p1score = 0
        p2score = 0
    
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            pygame.quit() 
            playing = 0
    
    clock.tick(60)

    #print(clock.get_fps())
        # Draws the surface object to the screen.   
    pygame.display.update() 