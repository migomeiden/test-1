from pygame.locals import *
import pygame
import sys

x = 300
y = 200
h = y
osu = 0

eneX = 300 
eneY = 100

haiX = -300
haiY = -200

def draw(screen, player_image, img3, hai1, kou1):
        global x,y,h,osu , haiX,haiY
        screen.fill(pygame.Color("white"))
        screen.blit(hai1, ( haiX, haiY))
        screen.blit(img3, ( x, y))#最初のスライムの座標
        screen.blit(player_image, ( eneX, eneY))
        
        if osu == 0:
        
           screen.blit(kou1, ( x , 1000))
       
        if osu == 1:
          
           screen.blit(kou1, ( x , h - 15))
        
        pygame.display.update()
        
def move(screen):     #スライムを動かす
        global x,y,h,osu,eneX,eneY,haiX,haiY
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if y > 150:
                y = y - 3
            else:
                haiY = haiY + 3
                eneY = eneY + 3
        #if y < -10:
            #y = -10

        if key[pygame.K_s]:
            if y < 250:    
                y = y + 3
            else:
                haiY = haiY - 3
                eneY = eneY - 3
            #if y > 360:
                #y = 360
        
        if key[pygame.K_a]:
            if x > 250:
                x = x - 3
            else:
                haiX = haiX + 3
                eneX = eneX + 3
            #if x < -8:
                #x = -8
        
        if key[pygame.K_d]:
            if x < 350:
                x = x + 3
            else:
                haiX = haiX - 3
                eneX = eneX - 3
            #if x > 557:
                #x = 557
                       
        if key[pygame.K_UP]:
            osu = 1
        
            for i in range (50):
              #h = y
              if h > 0:
                  
             
                  h = h - 0.5
              else:
                h = y
                osu = 0          
                   
              
        else:
               osu = 0      
               h = y  
            
def main():
     pygame.init()
     clock = pygame.time.Clock()
     screen = pygame.display.set_mode((600, 400))    
     player_image = pygame.image.load("画像/ｔame.png").convert()
     img3 = pygame.image.load("画像/スライム（背景なし）.png")
     hai1 = pygame.image.load("画像/yakei.hai.jpg")
     kou1 = pygame.image.load("画像/kougeki.png")
     hai1 = pygame.transform.scale(hai1,(1200 , 800))
     
     while True:
        FPS = 60
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.event.clear()
        

        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            break
       
        mouse_pos = pygame.mouse.get_pos()

        draw(screen, player_image, img3, hai1, kou1)
        
        move(screen)

     pygame.quit()


main()