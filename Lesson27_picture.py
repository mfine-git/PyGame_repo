import pygame

MAX_X = 1366
MAX_Y = 768

game_over = False
bg_color = (5, 0, 90)
image_size = 100

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My first Pygame Game! :-)")

picture = pygame.image.load("picture.png").convert()
picture = pygame.transform.scale(picture, (image_size, image_size))

x = 400
y = 200
move_right = False
move_left = False
move_up = False
move_down = False



# _______________ MAIN GAME LOOP _______________

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left == True:
        x -= 1
        if x < 0:
            x = 0

    if move_right == True:
        x += 1
        if x > MAX_X-image_size:
            x = MAX_X-image_size
    if move_up == True:
        y -= 1
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        if y > MAX_Y-image_size:
            y = MAX_Y-image_size

    screen.fill(bg_color)
    screen.blit(picture, (x, y))
    pygame.display.flip()
