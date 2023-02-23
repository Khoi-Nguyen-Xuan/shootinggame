import pygame
import random
import math

# Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Background image
background = pygame.image.load('background.png')

#Title and Icon
pygame.display.set_caption("Snake game")
icon = pygame.image.load('fighter-jet.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('fighter-jet.png')
playX = 370
playY = 480
playXChange = 0

#enemy
enemyImg = pygame.image.load('cthulhu.png')
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
eXChange = 5
eYChange = 0

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bXChange = 0
bYChange = 10
bulletstate = "ready" #ready means you can't see the bullet on the screen


score = 0

#PlayerFunction


def player(x,y):
    screen.blit(playerImg,(x,y))

#EnemyFunction

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

#BulletFunction

def fireBullet(x,y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletImg, (x+16, y+10))


# Game loop
running = True
while running :

    screen.fill((0,0,0))

    #background image
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:

         if event.key == pygame.K_LEFT:
             playXChange = -5

         if event.key == pygame.K_RIGHT:
             playXChange = 5

         if event.key == pygame.K_SPACE:
            if bulletstate is "ready":
             bulletX = playX
             fireBullet(bulletX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              playXChange = 0


    #player movement
    playX += playXChange

    if playX <= 0:
        playX = 0
    elif playX >=738:
        playX = 736

    player(playX,playY)

    #enemy movement
    enemyX += eXChange
    if enemyX <= 0:
        eXChange = 5
    elif enemyX >=736:
        eXChange = -5

    enemy(enemyX, enemyY)

    #bullet movement
    if bulletY <= -10 :
        bulletY = 480
        bulletstate ="ready"
    if bulletstate is "fire":
        fireBullet(bulletX,bulletY)
        bulletY -= bYChange

  

    pygame.display.update()
