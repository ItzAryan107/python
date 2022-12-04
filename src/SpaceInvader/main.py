import pygame as pyg
import random as ran
import math as mat
from pygame import mixer as sound

pyg.init()
# initialization of pygame(Which is very important), without this initialization the game/pygame won't work

#                  breadth(x-axis), height(y-axis)
screen = pyg.display.set_mode((800, 600))  # its take tuple as argument
# use to create a screen, in .set_mode function we give tuple breadth and height of window

"""
just after creation of screen, if you will run the code
a window will come, but it will last just only for few seconds
it is bcz our python program goes with these three above lines only and exit the program

in short
there is nothing to do in the program that's it went off in 2 or 3 seconds
means the coming window will close when it will reach to end code of the file

like if in between there is an infinite loop then the window will continue to run
and system will hang
so we use QUIT function, as someone press the red cross button, window get smoothly terminate

this comment is only when there is above three lines only
"""

# to change the caption of the window
pyg.display.set_caption("SPACE INVADERS")

# adding icon
icon = pyg.image.load("icon.png")
pyg.display.set_icon(icon)


def screenToFill():
    """
    fill function of screen takes tuple as argument,
    the tuple takes three argument(r, g, b)
    r - red, g - green, b - blue
    as the all colors in this world is the mixture of rgb
    value ranges from 0 to 255 for RGB
    for pure RGB use 255
    """
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))  # it ask the coordinate for top left corner
    pyg.display.update()


# adding fighter flight to the event(Player)
playerImage = pyg.image.load("player.png")
playerX = 370
playerY = 450
playerX_Change = 0


def player(x, y):
    """blit means draw"""
    screen.blit(playerImage, (x, y))  # this is going to draw the image on screen window
    pyg.display.update()


# adding enemy
enemyImage = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
numOfEnemy = 6
for i in range(numOfEnemy):
    enemyImage.append(pyg.image.load("alien.png"))
    enemyX.append(ran.randint(0, 735))
    enemyY.append(ran.randint(50, 200))
    enemyX_Change.append(4)
    enemyY_Change.append(20)


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))
    pyg.display.update()


# adding background to the window
background = pyg.image.load("background.png")

# adding bullet to thw spaceship
bulletImage = pyg.image.load("bullet.png")
bulletX = 0
bulletY = 450
bulletX_Change = 0
bulletY_Change = 5
bullet_state = "ready"


# ready - you can't see the image on the screen
# fire - you can see the image on the screen, when its trigger to see


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = mat.sqrt(mat.pow(enemyX - bulletX, 2) + mat.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# initializing the value of score
scoreValue = 0
scoreFont = pyg.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


def showScore(x, y):
    score = scoreFont.render("Score :" + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))
    pyg.display.update()


overFont = pyg.font.Font("freesansbold.ttf", 84)


def gameOver():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overText, (180, 250))
    pyg.display.update()


# adding background sound
sound.music.load("Resident Evil 4.mp3")  # we are using music function bcz this music is need to be played till the game
# ends, but if you want to play a sound for few seconds then we will use sound function
# sound.music.play()  <--- this will let you play the music just for once
sound.music.play(-1)  # by giving -1 as argument, let the music to play on loop

# game loop
running = True
while running:
    # anything which is need to be persistent on game window, that is need to be put in this while loop
    # so that it can be used continuously
    screenToFill()  # this should bw executed first, bcz first background should be completed first
    """
    Now creating variable event to all through all event,
    which i am keeping in for loop to iterate all event one ny one
    """
    for event in pyg.event.get():
        """
        if in between quit command is given to event,
        then we wll check the command is quit then we will quit the window
        """
        if event.type == pyg.QUIT:
            running = False

        # connecting movement to keyboard
        # if key-stroke is pressed check whether its right or left(this is an event)
        if event.type == pyg.KEYDOWN:  # it will indicate the interpreter, that any keystroke is pressed(if type is
            # keyboard)
            if event.key == pyg.K_LEFT or event.key == pyg.K_a:  # this will check that the pressed key is left or not
                playerX_Change -= 5
            if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                playerX_Change += 5
            if event.key == pyg.K_SPACE:
                if bullet_state == "ready":
                    # adding sound to bullet, whenever its fire
                    bulletSound = sound.Sound("laser.wav")
                    bulletSound.play()
                    # get the current x-coordinate of the spaceship
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pyg.KEYUP:
            if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT or event.key == pyg.K_a or event.key == pyg.K_d:
                playerX_Change = 0

    playerX += playerX_Change
    # adding some condition so it wont get out of the screen
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:  # taking 736pix bcz spaceship pix is 64, so subtracting it as it wont get out of the screen
        playerX = 0
    # make sure that if you are adding anything to the display window, display is need to be update

    # enemy movement
    for i in range(numOfEnemy):

        # Game-Over
        if enemyY[i] > 425:
            for i in range(numOfEnemy):
                enemyY[i] = 2000
            gameOver()
            break

        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 0:
            enemyX_Change[i] += 4
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 736:
            enemyX_Change[i] += -4
            enemyY[i] += enemyY_Change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # adding sound whenever, bullet strike the enemy
            explosionSound = sound.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 450
            bullet_state = "ready"
            scoreValue += 1
            enemyX[i] = ran.randint(0, 735)
            enemyY[i] = ran.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 450
        bullet_state = "ready"
    if bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    player(playerX, playerY)
    showScore(textX, textY)

"""
you can fet the images from flaticon.com
In present there is only one font in in this pygame - freesansbold.ttf

if ou want to add more font to your pygame it need to download from the website
https://www.dafont.com/ <--- from here you can download the fonts, which will give you zip file
which is need to be extract that zip file, which will give you a .ttf file
and that ttf file is need to be pasted in the project/folder in which you need
"""
