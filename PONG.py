import pygame
import time
import random

pygame.init()

# basic initialization of all variables
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = [0, 0, 0]

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# initialization of everything important to an FPS metre display
fpsdefault = "FPS = "
fpsfont = pygame.font.Font("freesansbold.ttf", 10)
fpstext = fpsfont.render(fpsdefault, True, white, black)
fpstextRect = fpstext.get_rect()
fpstextRect.center = (760, 10)

# global variables for the FPS display function
starttime = time.time()
ticks = 0
numresets = 0
totalfps = 0
avgfps = 0

# initialization of paddle positions:
paddle1x = 20
paddle1y = 235
paddle2x = 755
paddle2y = 235
ballx = 400
bally = 300

# function to randomly return either a 1 or a -1
def coinflip():
    r = random.randrange(-1, 2, 2)
    return r


# function to return a random number between -1 and 1 (used to decide initial vertical velocity of the ball)
def randomdecimal():
    r = random.random()
    r = r * coinflip()
    return r


# Function in charge of an initial (probably unnecessary) loading screen
def loadingscreen():
    loadingfont = pygame.font.Font("freesansbold.ttf", 200)
    loadingtext = loadingfont.render("PONG", True, white, black)
    loadingtextRect = loadingtext.get_rect()
    X = 400
    Y = 300
    loadingtextRect.center = (X, Y)
    gameDisplay.blit(loadingtext, loadingtextRect)
    starttime = time.time()
    # groundwork for a loading screen animation
    while time.time() - starttime < 2:
        gameDisplay.blit(loadingtext, loadingtextRect)
        pygame.display.update()


# function that displays the average FPS that the game is running on -- *NEEDS IMPROVEMENT*
def showfps():
    global ticks
    global starttime
    global avgfps
    global numresets
    global totalfps
    tensecondsgo = 0

    ticks += 1

    if time.time() - starttime >= 1:
        ticks = 0
        numresets += 1
        starttime = time.time()

    if numresets > 0:
        totalfps += ticks
        avgfps = totalfps // numresets

    fps = fpsdefault + str(avgfps)
    fpstext = fpsfont.render(fps, True, white, black)
    gameDisplay.blit(fpstext, fpstextRect)


def scoreboard(p1score, p2score):
    p1font = pygame.font.Font("freesansbold.ttf", 90)
    p1text = p1font.render(str(p1score), True, white, black)
    p1textrect = p1text.get_rect()
    x = 250
    y = 100
    p1textrect.center = (x, y)
    gameDisplay.blit(p1text, p1textrect)


def paddle1(x, y):
    # pygame.draw.rect(gameDisplay, white, (x, y, 25, 130), 1)
    paddle = pygame.Surface((26, 130))
    paddle.fill(white)
    gameDisplay.blit(paddle, (x, y))


def paddle2(x, y):
    paddle = pygame.Surface((26, 130))
    paddle.fill(white)
    gameDisplay.blit(paddle, (x, y))


def ball(x, y):
    pygame.draw.circle(gameDisplay, white, (x, y), 10)


# Calling the loading screen function for the first and only time
loadingscreen()

ballvelocityx = coinflip() * 8
ballvelocityy = int(randomdecimal() * ballvelocityx)

# final initialization
playing = 1
p1score = 0  # player 1 score
p2score = 0  # player 2 score

# Main function, essentially (A loop that runs infintely until the quit button is pressed)
while playing:
    gameDisplay.fill(black)

    # self explanatory, displays the FPS
    showfps()

    scoreboard(p1score, p2score)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if paddle2y >= 0:
            paddle2y -= 8
    if keys[pygame.K_DOWN]:
        if paddle2y <= 470:
            paddle2y += 8
    if keys[pygame.K_w]:
        if paddle1y >= 0:
            paddle1y -= 8
    if keys[pygame.K_s]:
        if paddle1y <= 470:
            paddle1y += 8

    if ballx <= 810 and ballx >= -10:
        ballx += ballvelocityx
    elif ballx > 810:
        p1score += 1
        ballx = 400
        bally = 300
        ballvelocityx = coinflip() * 8
        ballvelocityy = int(randomdecimal() * ballvelocityx)
        time.sleep(3)
    elif ballx < -10:
        p2score += 1
        ballx = 400
        bally = 300
        ballvelocityx = coinflip() * 8
        ballvelocityy = int(randomdecimal() * ballvelocityx)
        time.sleep(3)

    if bally < 590 and bally > 10:
        bally += ballvelocityy
    elif bally == 590 or bally == 10:
        ballvelocityy = -ballvelocityy
        bally += ballvelocityy
    else:
        if bally > 590:
            bally = 590
        else:
            bally = 10

    ball(ballx, bally)
    paddle1(paddle1x, paddle1y)
    paddle2(paddle2x, paddle2y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = 0

    clock.tick(60)

    # print(clock.get_fps())
    # Draws the surface object to the screen.
    pygame.display.update()
