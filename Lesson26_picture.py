import pygame
MAX_X = 1366
MAX_Y = 768

game_over = False
bg_color = (0, 50, 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My first Pygame Game! :-)")

picture = pygame.image.load("picture.png").convert()
picture = pygame.transform.scale(picture, (100, 100))

x = 400
y = 200

# _______________ MAIN GAME LOOP _______________

while game_over == False:
   for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_ESCAPE:
               game_over = True
           if event.key == pygame.K_LEFT:
               x -= 20
           if event.key == pygame.K_RIGHT:
               x += 20
           if event.key == pygame.K_UP:
               y -= 20
           if event.key == pygame.K_DOWN:
               y += 20
       if event.type == pygame.MOUSEBUTTONDOWN:
           x, y = event.pos
   screen.fill(bg_color)
   screen.blit(picture, (x,y))
   pygame.display.flip()
