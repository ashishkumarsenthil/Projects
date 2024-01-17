
import pygame ,sys,time,math,random
from pygame.locals import*

pygame.init()
xaxis=20
yaxis=140
DISPLAYSURF=pygame.display.set_mode((800,300))
pygame.display.set_caption("spacefighter")
Aqua=(0, 255, 255)
Black=(  0,   0,   0)
Blue=(  0,  0, 255)
Fuchsia=(255,   0, 255)
Gray=(128, 128, 128)
Green=(  0, 128,   0)
Lime=(  0, 255,   0)
Maroon=(128,  0,   0)
NavyBlue=(  0,  0, 128)
Olive=(128, 128,   0)
Purple=(128,  0, 128)
Red=(255,   0,   0)
Silver=(192, 192, 192)
Teal=(  0, 128, 128)
White=(255, 255, 255)
Yellow=(255, 255,   0)
playerimg=pygame.image.load("image1.png")
playerimg=pygame.transform.scale(playerimg,(50,50))
background=pygame.image.load("image2.PNG")
background=pygame.transform.scale(background,(800,300))
def fillscreen():

    DISPLAYSURF.fill(White)
    pygame.draw.line(DISPLAYSURF,Gray,(0,280),(800,280))
    pygame.draw.line(DISPLAYSURF,Gray,(0,20),(800,20))
    pygame.draw.line(DISPLAYSURF,Gray,(20,0),(20,800))
    #pygame.draw.rect(DISPLAYSURF,Gray,(xaxis,yaxis,50,50))
    DISPLAYSURF.blit(playerimg,(xaxis,yaxis))
    DISPLAYSURF.blit(background,(0,0))
    
fillscreen()
a=random.randint(60,240)
circx=800
circxx=700
circy=a
circyy=random.randint(60,240) 

dell=3
count=1
g=(xaxis,yaxis)
v=10
while count==1:
    a=random.randint(60,240)
    circx=800
    circxx=800
    circy=a
    circyy=random.randint(60,240)
    
    while circx!=10:      
            pygame.draw.circle(DISPLAYSURF,White,(circx,circy),20)
            pygame.draw.circle(DISPLAYSURF,White,(circxx,circyy),20)
            #print("While")
            #print(event.type == pygame.KEYDOWN)
            
            #pygame.draw.rect(DISPLAYSURF,Gray,(xaxis,yaxis,40,40))
            DISPLAYSURF.blit(playerimg,(xaxis,yaxis))
            
            circx-=1
            circxx-=1
            pygame.time.delay(dell)
            if circx==90 and circy>=yaxis-20 and circy<=yaxis+20:
                print("you lose")
                count=0
                break
            elif circxx==90 and circyy>=yaxis-20 and circyy<=yaxis+20:
                print("you lose")
                count=0
                break
                
            pygame.display.update()
            fillscreen()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #print("Type")
                    if event.key== pygame.K_UP and yaxis>20:
                        fillscreen()
                        yaxis-=v
                        if event.key==pygame.K_UP and yaxis==10:
                            fillscreen()
                            yaxis+=v
                    if event.key==pygame.K_DOWN and yaxis<=270:
                        fillscreen()
                        yaxis+=v
                        if event.key==pygame.K_DOWN and yaxis==240:
                            fillscreen()
                            yaxis-=v
                if event.type==pygame.QUIT:
                    pygame.quit()
            fillscreen()  
    for event in pygame.event.get():
        DISPLAYSURF.blit(playerimg,(xaxis,yaxis))
        fillscreen()
        if event.type == pygame.KEYDOWN:
                print("Type")
                if event.key== pygame.K_UP and yaxis>20:
                    fillscreen()
                    yaxis-=10
                    if event.key==pygame.K_UP and yaxis==10:
                        fillscreen()
                        yaxis+=10
                if event.key==pygame.K_DOWN and yaxis<=270:
                    fillscreen()
                    yaxis+=10
                    if event.key==pygame.K_DOWN and yaxis==240:
                        fillscreen()
                        yaxis-=10
        if event.type==pygame.QUIT:
            pygame.quit()
            
    fillscreen()     
    pygame.display.update()
       
















