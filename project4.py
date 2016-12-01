import pygame
from pygame.locals import *
import math
import random

class Badguy(pygame.sprite.Sprite):
    def __init__(self, image, position, minSpeed):
        self.minSpeed = minSpeed
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
    def update(self):
        self.position[0] -= random.randint(self.minSpeed, 32)

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100,100]
acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
minspeed = 0 
healthvalue=194
pygame.mixer.init()
count = 0

# 3 - Load images
player = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/newman.bmp")
grass = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/newhorizon.bmp")
castle = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/planet.bmp")
arrow = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/rocket.bmp")
badguyimg1 = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/newastroid.bmp")
badguyimg=badguyimg1
healthbar = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.bmp")
health = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.bmp")
gameover = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.bmp")
youwin = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.bmp")

firstBadGuy = Badguy("/Users/jessicastuart/Desktop/206project4/images/newastroid.bmp", [640, 100], minspeed)
badguys=[firstBadGuy]


hit = pygame.mixer.Sound("/Users/jessicastuart/Desktop/206project4/sounds/cannon.wav")
enemy = pygame.mixer.Sound("/Users/jessicastuart/Desktop/206project4/sounds/explosion.wav")
shoot = pygame.mixer.Sound("/Users/jessicastuart/Desktop/206project4/sounds/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('/Users/jessicastuart/Desktop/206project4/sounds/starwars.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.20)


# 4 - keep looping through
running = 1
exitcode = 0
while running:
    badtimer-=1
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass,(x*100,y*100))
     
    # DRAW THINGS HERE    
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    xMin = playerpos1[0]
    xMax = playerpos1[0] + 100
    yMin = playerpos1[1] - 62
    yMax = playerpos1[1]
    for badguy in badguys:
        if badguy.position[0] >= xMin and badguy.position[0] <= xMax:
            if badguy.position[1] >= yMin and badguy.position[1] <= yMax:
                healthvalue -= 1 
                
        


    
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    if badtimer==0:
        newBadGuy = Badguy("/Users/jessicastuart/Desktop/206project4/images/astroid.bmp"\
                           ,[640, random.randint(50,430)], minspeed)
        badguys.append(newBadGuy)
        badtimer=100-(badtimer1*2)
        if badtimer1>=42:
            badtimer1=42
        else:
            badtimer1+=7

        if minspeed >= 32:
            minspeeed = 32
        else:
            minspeed += 2
    index=0
    for badguy in badguys:
        if badguy.position[0]<-64:
            badguys.pop(index)
        badguy.update()
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy.position[1]
        badrect.left=badguy.position[0]
        if badrect.left<64:
            healthvalue -= 5
            badguys.pop(index)
            enemy.play()
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
                count += 1
                hit.play()
            index1+=1
 
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy.position)     

    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))
     

    pygame.display.flip()


#HANDLE EVENTS HERE
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])


    # UPDATE POSITION HERE
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
        
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0

 
# 11 - Win/lose display        
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%" + "  Count: "+str(count), True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    #scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()

exit()
