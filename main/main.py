import pygame
import random
import sprites as sps
import Colors as c
import os

# set up game
WIDTH = 800
HEIGHT = 600
FPS = 30
pygame.init()
pygame.mixer.init()

# create window
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
pygame.display.set_caption('Test Game')

# frame conditions
clock = pygame.time.Clock()
game_over = False

# settings for the images
img_folder = os.path.join(os.path.dirname(__file__), 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'lario2.png')).convert_alpha()
p1 = sps.Player(WIDTH, HEIGHT, player_img)

back_img_loc = os.path.join(img_folder, 'backpic.png')
BackGround = sps.Background(back_img_loc, [0, 0])

# group of sprites that will be the obstacles
obs = pygame.sprite.Group()
ob1 = sps.Block((WIDTH/2, HEIGHT-40))
ob2 = sps.Block((WIDTH/2 + 200, HEIGHT-120))
obs.add(ob1)
obs.add(ob2)

height = 0  # variable for change in direction
width = 0  # lol same

jump = False
max_jmp = 2  # max amount of jumps without landing
cur_height = HEIGHT  # where the player is right now
jmp_height = -80  # jump height of ONE jump (- because (0,0) is upper left
cur_goal = HEIGHT  # the goal of the jump. standard is HEIGHT, because without the jump goal and current height is
# the same
jmp_cntr = 2  # jumps still available
jmp_change = 4  # amount of change in a frame while jumping
reached = False  # if the jmp_goal was reached

collision_detected = False
col_old = False  # old value of collision detection
fall = False  # if the player currently falls



while not game_over:
    clock.tick(FPS)
    height = 0
    width = 0

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                jump = True
                if jmp_cntr > 0:
                    cur_goal = cur_height + jmp_height
                    reached = False
                    jmp_cntr -= 1
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        width = -4
    elif keystate[pygame.K_RIGHT]:
        width = 4
    #   elif event.type == pygame.MOUSEBUTTONUP:
    #      pos = pygame.mouse.get_pos()
    #     drawCircle(pos, 30)

    col_old = collision_detected
    collision_detected = pygame.sprite.spritecollide(p1, obs, False)
    if col_old and not collision_detected:
        fall = True

    if fall:
        if not collision_detected and not p1.rect.bottom == HEIGHT:  # down till on obstacle or on Ground
            height = -jmp_change
        else:
            height = 0
            fall = False

    if jump:
        if cur_height <= cur_goal:
            reached = True
        if cur_height > cur_goal and not reached:  # Ziel noch nicht erreicht
            height = jmp_change
            cur_height -= jmp_change  # i know, seems stupid, but remember (0,0) is upper left
        elif not collision_detected and not p1.rect.bottom == HEIGHT:  # down till on obstacle or on Ground
            height = -jmp_change
            cur_height += jmp_change  # i know, seems stupid, but remember (0,0) is upper left
        else:
            jmp_cntr = max_jmp
            height = 0
            jump = False
            reached = False

    p1.update(height, width)
    obs.update()
    dis.fill(c.BLACK)
    # draw everything after this line!!!!!:
    dis.blit(BackGround.image, BackGround.rect)  # background image
    # from now on you can draw stuff. If you do that before the background it will be behind the background!
    p1.draw(dis)
    # best draw after this, the player should always be visible too
    obs.draw(dis)
    pygame.display.update()

pygame.quit()
quit()
