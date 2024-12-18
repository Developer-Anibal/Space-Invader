import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40

# Bullet
# Ready state - you can't see the bullet on the screen
# Fire - The bullet is currently moving
# We are moving bulletX coordinate inside loop
# bulletY is 480 due PlayerY is 480 at nose of player
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.3
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x + 16, y + 10))

# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((192, 192, 192))
    # Backgroud
    screen.blit(background,(0,0))
    # playerY -= 0.05
    # print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:                                  # print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:                                # print("Left arrow is pressed")
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:                               # print("Right arrow is pressed")
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:                               # print("Space arrow is pressed")
                if bullet_state == "ready":
                    bulletX = playerX                                     # Get the current x coordinate of the spaceship
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # print("Keystroke has been released")
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    # Set limits bisided - width of spacecraft is 64 minus 800 = 736
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    # Set limits bisided - width of spacecraft is 64 minus 800 = 736
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY <= 0: # Above 0 is going to negative values
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
