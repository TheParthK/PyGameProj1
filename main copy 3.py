from numpy import true_divide
import pygame
import random
# initialiseing pygame
pygame.init() # initilaizing all pygame module

dimensions = (800, 600)

screen = pygame.display.set_mode(dimensions)

bgcolor = (150, 150, 150) 

# Title and Icon

pygame.display.set_caption("Space Invaders!")

icon = pygame.image.load("icon.png")

player_img = pygame.image.load("player.png")
playerx, playery = 370, 500
playerx_change, playery_change = 0, 0

enemy_img = pygame.image.load("enemy.png")
enemyx, enemyy = random.randint(7, 732), random.randint(7, 400)
enemyx_change, enemyy_change = 1.2, 0
# def player():
#     screen.blit(player_img, player_coordinates)

# bullet 

bullet_img = pygame.image.load("bullet.png")
bulletx, bullety = 0, 0
bulletx_change, bullety_change = 0, 4
bullet_state = 'ready'

background = pygame.image.load("bg.jpg")
pygame.display.set_icon(icon)

run = True
hit = False
score = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # gonna quit when cross is pressed
        # if keystroke is pressed check if it is left or right
        # Movement 🥲
        if event.type == pygame.KEYDOWN:
            # print("KeyDown")
            if event.key == pygame.K_LEFT:
                playerx_change -= 4
                # print("Left arrow pressed")
            if event.key == pygame.K_RIGHT:
                playerx_change += 4
                # print("Right arrow pressed")
            if event.key == pygame.K_UP:
                playery_change -= 4
                # print("Up arrow pressed")
            if event.key == pygame.K_DOWN:
                playery_change += 4
                # print("Down arrow pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready" :
                    bulletx = playerx
                    bullety = playery
                    # screen.blit(bullet_img, (playerx + 16, bullety))
                    bullet_state = 'fire'

        if event.type == pygame.KEYUP:
            # print("KeyUp")
            playerx_change = 0
            playery_change = 0
            # need to change the chnage to 0 nhi toh pagal panti

        
    # everything  that needs to be looped is outside for loop basically 
    screen.fill(bgcolor)
    # # # # # # # # # # # # # # # # # # # # # # # 

    screen.blit(background, (0, 0))

    # player() # called after screen.fill
    screen.blit(player_img, (playerx, playery)) # drawing player on the screen
    screen.blit(enemy_img, (enemyx, enemyy)) # drawing enemy on the screen
    
    playerx += playerx_change
    playery += playery_change

    # # enemyx += random.uniform(-10, 10)
    # # enemyy += random.uniform(-10, 10)
    # enemyx += random.choice([-1, 1])
    # enemyy += random.choice([-1, 1])

    enemyx += enemyx_change
    enemyy += enemyy_change
    # fix when player and enemy gho out of bounds and also enemy goes down 
    if playerx > 732 :
        playerx = 732
    if playery > 532 :
        playery = 532
    if playerx < 7 :
        playerx = 7
    if playery < 7 :
        playery = 7
    # checking boundary of enemy and it bouces back once reaches the x boundary
    if enemyx > 732 :
        enemyx = 732
        enemyx_change = - enemyx_change
        # enemyy += random.choice([-5, 5])
        enemyy += 5
    if enemyy > 532 :
        enemyy = 532
    if enemyx < 7 :
        enemyx = 7
        enemyx_change = - enemyx_change
        # enemyy += random.choice([-5, 5])
        enemyy += 5

    if enemyy < 7 :
        enemyy = 7

    # bullet_movement 
    if bullety <= 0:
        bullety = playery
        bullet_state = "ready"
    if bullet_state == "fire" :
        screen.blit(bullet_img, (bulletx + 16, bullety))
        bullety -= bullety_change
        
    if abs(playery - bullety) > 15 :
        if abs(enemyx - bulletx) < 15 and abs(enemyy - bullety) < 15:
            hit = True
    if hit :
        score += 1
        hit = False
        enemyx, enemyy = random.randint(7, 732), random.randint(7, 400)
        bulletx, bullety = playerx, playery
        bullet_state = "ready"
        print("Score- ",score)
    

    pygame.display.update() # updating the display 
