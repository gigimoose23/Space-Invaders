import pygame
import sys
import time
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
winnerFont = pygame.font.SysFont("Times New Roman", 30);
bgimg = pygame.image.load("images/bg.png");
rocketyellowimg = pygame.image.load("images/rocketyellow.png");
rocketredimg = pygame.image.load("images/rocketred.png");
rocketredimg = pygame.transform.scale(rocketredimg, (70, 70));
rocketredimg = pygame.transform.rotate(rocketredimg, 90);

rocketyellowimg = pygame.transform.scale(rocketyellowimg, (70, 70));
rocketyellowimg = pygame.transform.rotate(rocketyellowimg, -90);
screenborder = pygame.Rect(250, 0, 10, 500000)
inputLocked = False
#                up     down   left   right
rocketyellowkeys = [False, False, False, False]
redbullets = []
yellowbullets = []
charspeed = 0.2
rocketredxi = 50
rocketredyi = 200
rocketredx = rocketredxi
rocketredy = rocketredyi
healthHit = 0.5
rocketyellowxi = 375
rocketyellowyi = 200
rocketyellowx = rocketyellowxi
rocketyellowy = rocketyellowyi
isInEndStage = False
endingText = None
recentlyOnAgenda = False
allowedBullets = True
def triggerDeath(winner):
    global inputLocked,isInEndStage,endingText,healthred,healthyellow,rocketyellowx,rocketyellowy,rocketredxi,rocketredyi,rocketyellowxi,rocketyellowyi,initialhealth,rocketredx,rocketredy
    healthred = initialhealth
    healthyellow = initialhealth
    rocketyellowx = rocketyellowxi
    rocketyellowy = rocketyellowyi
    for redBullet in redbullets:
        redbullets.remove(redBullet)
    for yellowBullet in yellowbullets:
        yellowbullets.remove(yellowBullet)
    rocketredx = rocketredxi
    rocketredy = rocketredyi
    print("death")
    inputLocked = True
    endingText = winnerFont.render("Winner: " + winner, True, (255,255,255));
    isInEndStage = True
    screen.blit(endingText, (150,200))
    pygame.display.flip()
  
    pygame.time.delay(2000) 
    recentlyOnAgenda = True
    isInEndStage = False
    allowedBullets = False
    inputLocked = False

def draw():
    global recentlyOnAgenda
    screen.blit(bgimg, (0,0))
    screen.blit(rocketredimg, (rocketredx,rocketredy));
    screen.blit(rocketyellowimg, (rocketyellowx,rocketyellowy));
    pygame.draw.rect(screen, (0,0,0), screenborder);
    textrenderred = textfont.render("Health: " + str(healthred), True, (255,255,255));
    screen.blit(textrenderred, (0,0))

    textrenderyellow = textfont.render("Health: " + str(healthyellow), True, (255,255,255));
   # pygame.draw.rect(screen, (255, 255,0), rocketRedRect);
    #pygame.draw.rect(screen, (255, 255,0), rocketYellowRect);
    screen.blit(textrenderyellow, (410,0))
    if isInEndStage:
        screen.blit(endingText, (150,200))
    if recentlyOnAgenda == False:
        for redBullet in redbullets:
            pygame.draw.rect(screen, (255, 0,0), redBullet);
        for yellowBullet in yellowbullets:
            pygame.draw.rect(screen, (255, 255,0), yellowBullet);
    else:
        for redBullet in redbullets:
            redbullets.remove(redBullet)
        for yellowBullet in yellowbullets:
            yellowbullets.remove(yellowBullet)
    
    recentlyOnAgenda = False  
bulletspeed = 1
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
           
            healthyellow -= healthHit
            if healthyellow == 0:
                redbullets.remove(redBullet)
                for redBullet in redbullets:
                    redbullets.remove(redBullet)
                for yellowBullet in yellowbullets:
                    yellowbullets.remove(yellowBullet)
                pygame.time.delay(1000)
                triggerDeath("Red")
            else:
                redbullets.remove(redBullet)
import math,random
def moveYellowBullets():
    global healthred
    for yellowBullet in yellowbullets:
        yellowId = random.randint(0,9999)
      
        yellowBullet.x = yellowBullet.x - bulletspeed

        if rocketRedRect.colliderect(yellowBullet):
            print("HIT BULLET!!!")
            healthred -= healthHit
            if healthred == 0:
                yellowbullets.remove(yellowBullet)
                for redBullet in redbullets:
                    redbullets.remove(redBullet)
                for yellowBullet in yellowbullets:
                    yellowbullets.remove(yellowBullet)
                pygame.time.delay(1000)
                triggerDeath("Yellow")
            else:
                yellowbullets.remove(yellowBullet)
            

running = True
while running:
    
   
    if inputLocked == False:
        moveRedRocket()
        moveRedBullets()
        moveYellowBullets()
    else:
        for redBullet in redbullets:
            redbullets.remove(redBullet)
        for yellowBullet in yellowbullets:
            yellowbullets.remove(yellowBullet)
        
  
    rocketYellowRect.x = rocketyellowx
    rocketYellowRect.y = rocketyellowy


    rocketRedRect.x = rocketredx
    rocketRedRect.y = rocketredy
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
       
        if event.type == pygame.KEYDOWN and inputLocked == False:
           
            
            if event.key == pygame.K_w:
                rocketyellowkeys[0] = True
            if event.key == pygame.K_s:
                rocketyellowkeys[1] = True
            if event.key == pygame.K_a:
                rocketyellowkeys[2] = True
            if event.key == pygame.K_d:
                rocketyellowkeys[3] = True

           
        if event.type == pygame.KEYUP and inputLocked == False:
            if event.key == pygame.K_LSHIFT:
              
                redBullet = pygame.Rect(rocketredx+70, rocketredy+70 / 2, 20, 10)
                redbullets.append(redBullet)
            if event.key == pygame.K_RSHIFT:
               
                yellowBullet = pygame.Rect(rocketyellowx, rocketyellowy+70 / 2, 20, 10)
                yellowbullets.append(yellowBullet)



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
