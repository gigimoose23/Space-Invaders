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
textfont = pygame.font.SysFont("Times New Roman", 20);
bgimg = pygame.image.load("images/bg.png");
rocketyellowimg = pygame.image.load("images/rocketyellow.png");
rocketredimg = pygame.image.load("images/rocketred.png");
rocketredimg = pygame.transform.scale(rocketredimg, (70, 70));
rocketredimg = pygame.transform.rotate(rocketredimg, 90);

rocketyellowimg = pygame.transform.scale(rocketyellowimg, (70, 70));
rocketyellowimg = pygame.transform.rotate(rocketyellowimg, -90);
screenborder = pygame.Rect(250, 0, 10, 500000)

#                up     down   left   right
rocketyellowkeys = [False, False, False, False]
redbullets = []
yellowbullets = []
charspeed = 0.2
rocketredx = 50
rocketredy = 200

rocketyellowx = 375
rocketyellowy = 200
def draw():
    
    screen.blit(bgimg, (0,0))
    screen.blit(rocketredimg, (rocketredx,rocketredy));
    screen.blit(rocketyellowimg, (rocketyellowx,rocketyellowy));
    pygame.draw.rect(screen, (0,0,0), screenborder);
    textrenderred = textfont.render("Health: " + str(healthred), True, (255,255,255));
    screen.blit(textrenderred, (0,0))

    textrenderyellow = textfont.render("Health: " + str(healthyellow), True, (255,255,255));
    screen.blit(textrenderyellow, (410,0))
    for redBullet in redbullets:
        pygame.draw.rect(screen, (255, 0,0), redBullet);
  
bulletspeed = .5
def moveRedRocket():
    global rocketredx,rocketredy
    
    pressedKeys = pygame.key.get_pressed();
 
    if pressedKeys[pygame.K_UP] and rocketredy >= 0:
        rocketredy -= charspeed;
    if pressedKeys[pygame.K_DOWN] and rocketredy <= HEIGHT - 70:
        rocketredy += charspeed;
    if pressedKeys[pygame.K_LEFT] and rocketredx >= 0:
        rocketredx -= charspeed;
    if pressedKeys[pygame.K_RIGHT] and rocketredx <= WIDTH / 2 - 70:
        rocketredx += charspeed;
yellowBeenHit = pygame.USEREVENT
print("id: " + str(yellowBeenHit))
rocketRedRect = pygame.Rect(rocketredx, rocketredy, 70,70)
rocketYellowRect = pygame.Rect(rocketyellowx, rocketyellowy,70,70)
def moveRedBullets():
    global healthyellow
    for redBullet in redbullets:
        
        redBullet.x += bulletspeed
        if rocketYellowRect.colliderect(redBullet):
            print("HIT BULLET!!!")
            healthyellow -= 10
            redbullets.remove(redBullet)

running = True
while running:

    moveRedRocket()
    moveRedBullets()
    rocketYellowRect.x = rocketyellowx
    rocketYellowRect.y = rocketyellowy
    if rocketyellowkeys[0] == True:
        rocketyellowy -= charspeed
    if rocketyellowkeys[1] == True:
        rocketyellowy += charspeed
    if rocketyellowkeys[2] == True:
        rocketyellowx -= charspeed
    if rocketyellowkeys[3] == True:
        rocketyellowx += charspeed

  



    if rocketyellowx < WIDTH / 2 + 10:  
        rocketyellowx = WIDTH / 2 + 10
    if rocketyellowx + 70 > WIDTH:  
        rocketyellowx = WIDTH - 70
    if rocketyellowy < 0:  
        rocketyellowy = 0
    if rocketyellowy + 70 > HEIGHT:  
        rocketyellowy = HEIGHT - 70

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
           
            
            if event.key == pygame.K_w:
                rocketyellowkeys[0] = True
            if event.key == pygame.K_s:
                rocketyellowkeys[1] = True
            if event.key == pygame.K_a:
                rocketyellowkeys[2] = True
            if event.key == pygame.K_d:
                rocketyellowkeys[3] = True

           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                redBullet = pygame.Rect(rocketredx+70, rocketredy+70 / 2, 20, 10)
                redbullets.append(redBullet)



            if event.key == pygame.K_w:
                rocketyellowkeys[0] = False
            if event.key == pygame.K_s:
                rocketyellowkeys[1] = False
            if event.key == pygame.K_a:
                rocketyellowkeys[2] = False
            if event.key == pygame.K_d:
                rocketyellowkeys[3] = False

            

    draw()
    pygame.display.update()
