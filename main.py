import pygame
import sys
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
WIDTH = 500
HEIGHT = 500
initialhealth = 10
healthred = initialhealth
healthyellow = initialhealth
screen = pygame.display.set_mode((WIDTH, HEIGHT))
textfont = pygame.font.SysFont("Times New Roman", 20)
bgimg = pygame.image.load("images/bg.png")
rocketyellowimg = pygame.image.load("images/rocketyellow.png")
rocketredimg = pygame.image.load("images/rocketred.png")
rocketredimg = pygame.transform.scale(rocketredimg, (70, 70))
rocketredimg = pygame.transform.rotate(rocketredimg, 90)

rocketyellowimg = pygame.transform.scale(rocketyellowimg, (70, 70))
rocketyellowimg = pygame.transform.rotate(rocketyellowimg, -90)
screenborder = pygame.Rect(250, 0, 10, 500000)

#                up     down   left   right
rocketredkeys = [False, False, False, False]
rocketyellowkeys = [False, False, False, False]
charspeed = 0.2
rocketredx = 50
rocketredy = 200

rocketyellowx = 375
rocketyellowy = 200
def draw():
    screen.blit(bgimg, (0,0))
    screen.blit(rocketredimg, (rocketredx,rocketredy))
    screen.blit(rocketyellowimg, (rocketyellowx,rocketyellowy))
    pygame.draw.rect(screen, (0,0,0), screenborder)
    textrenderred = textfont.render("Health: " + str(healthred), True, (255,255,255))
    screen.blit(textrenderred, (0,0))

    textrenderyellow = textfont.render("Health: " + str(healthyellow), True, (255,255,255))
    screen.blit(textrenderyellow, (410,0))
running = True
while running:

    if rocketredkeys[0] == True:
        rocketredy -= charspeed
    if rocketredkeys[1] == True:
        rocketredy += charspeed
    if rocketredkeys[2] == True:
        rocketredx -= charspeed
    if rocketredkeys[3] == True:
        rocketredx += charspeed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if rocketredy >= 0:
                    rocketredkeys[0] = True
                else:
                    rocketredkeys[0] = False
                
            if event.key == pygame.K_DOWN:
                rocketredkeys[1] = True
            if event.key == pygame.K_LEFT:
                rocketredkeys[2] = True
            if event.key == pygame.K_RIGHT:
                rocketredkeys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocketredkeys[0] = False
            if event.key == pygame.K_DOWN:
                rocketredkeys[1] = False
            if event.key == pygame.K_LEFT:
                rocketredkeys[2] = False
            if event.key == pygame.K_RIGHT:
                rocketredkeys[3] = False

    draw()
    pygame.display.update()
  
