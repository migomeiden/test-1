from pygame.locals import *
import pygame
import sys
import math
import random


def limit(score_image_game):
    global time, time_finish, gameover
    
    if time >= time_finish:
        font = pygame.font.Font(None, 100)
        score_image_game = font.render (("game clear"), True, pygame.Color("yellow"))
        
        gameover = 1


def count(screen, cou1, cou2, cou3):
    global cou, gameover, count1
    
    if count1 == 0:
        gameover = 0
        
        if cou == 5:
            cou = 4
            sco = 0
            return
        
        if cou == 4:  
            cou = 3
            screen.blit(cou3, ( 480, 200))
            pygame.display.update()
            pygame.time.wait(1000)
            return
            
        if cou == 3:
            cou = 2
            screen.blit(cou2, ( 480, 200))
            pygame.display.update()
            pygame.time.wait(1000)
            return    
        
        if cou == 2:
            cou = 1
            screen.blit(cou1, ( 480, 200))
            pygame.display.update()
            pygame.time.wait(1000)
            cou = 0
            
            count1 = 1
            gameover = 0
            return
        

def reset():
    global x, y, osu, teki1, teki2, py, px, kx1, ky1, kx2, ky2, mxky, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, gameover, ene3x, ene4x, ene5x, sco, scox, scoy, cou, count1, start, level, time, time_finish, time_print
    x = 570
    y = 400
    osu = 0
    teki1 = 0
    teki2 = 0
    py = 2000
    px = 2000
    kx1 = random.randint(0, 1114)
    ky1 = 0
    kx2 = random.randint(0, 1114)
    ky2 = 0
    mxky = 800
    ex1 = random.randint(0, 1114)
    ey1 = 10
    ex2 = random.randint(0, 1114) 
    ey2 = 10
    ex3 = random.randint(0, 1114)
    ey3 = 10
    ex4 = random.randint(0, 1114)
    ey4 = 10
    ex5 = random.randint(0, 1114)
    ey5 = 10
    gameover = 0

    ene3x = 0
    ene4x = 0
    ene5x = 0
    
    sco = 0
    scox = 0
    scoy = 0

    cou = 5
    count1 = 0
    
    time = 0
    time_finish = 95
    time_print = 0


def draw_back(screen, easy, hard, ex, yajirusi):
    global level 
     
    screen.fill(pygame.Color("#613898"))
    screen.blit(easy, ( 30, 450))
    screen.blit(hard, ( 420, 450))
    screen.blit(ex, ( 810, 450))
    
    if level == 1:
        screen.blit(yajirusi, (185, 400))
        
    if level == 2:
        screen.blit(yajirusi, (575, 400))
        
    if level == 3:
        screen.blit(yajirusi, (965, 400))
     
    font_game = pygame.font.Font("テキスト/DotGothic16-Regular.ttf " , 50)
    staet_image_font = font_game.render (("--- Playing the game, please press SPACE key ---") , True ,pygame.Color("black"))
    screen.blit(staet_image_font, ( 15, 680))
    
    staet_image_font = font_game.render ((" Please press ARROW key ") , True ,pygame.Color("black"))
    screen.blit(staet_image_font, ( 300, 225))
    
    staet_image_font = font_game.render (("---           or            ---") , True ,pygame.Color("black"))
    screen.blit(staet_image_font, ( 200, 275))
    
    staet_image_font = font_game.render ((" MOUSE CLICK on the level ") , True ,pygame.Color("black"))
    screen.blit(staet_image_font, ( 280, 325))
    
    pygame.display.update()


def move_back(screen):
    global start, mouse_x, mouse_y, mouse_pos, level ,clock 
    
    reset()
    key = pygame.key.get_pressed()
    FPS = 60
    if level == 1 and key[pygame.K_RIGHT]:
            
            pygame.time.wait(100)
            level = 2
            pygame.event.clear()
            
            clock.tick(FPS)
            return
            
    if level == 2:
            
        if key[pygame.K_RIGHT]:
                pygame.time.wait(100)
                level = 3 
                pygame.event.clear()
                return
                
        if key[pygame.K_LEFT]: 
                pygame.time.wait(100)
                level = 1
                pygame.event.clear()
                return
                
    if level == 3 and key[pygame.K_LEFT]:
            pygame.time.wait(100)   
            level = 2 
            pygame.event.clear()
            clock.tick(FPS)
            return
        
    for event in pygame.event.get():   
        
        if event.type == MOUSEBUTTONDOWN and event.button == 1: 
          #  start = 0
            
            if mouse_x >= 75 and mouse_x <= 335 and mouse_y >= 415 and mouse_y <= 585:
                level = 1
                
            if mouse_x >= 465 and mouse_x <= 725 and mouse_y >= 415 and mouse_y <= 585:
                level = 2
                
            if mouse_x >= 855 and mouse_x <= 1115 and mouse_y >= 415 and mouse_y <= 585:
                level = 3
                
    if key[pygame.K_SPACE]:    
        start = 0


def draw(screen, img3, hai1, kou1, kou2, kou3, ene1, ene2, ene3, ene4, ene5, 
         root1, root2, root3, root4, root5, rootk1, rootk2, score_image, cou1, cou2, cou3, time_image):
        global x, y, px, py, kx1, ky1, kx2, ky2, osu, teki1, teki2, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, ene3x, ene4x, ene5x, sco, scox, scoy, gameover, count1, level
        screen.fill(pygame.Color("white"))
        screen.blit(hai1, ( 0, 0))
        screen.blit(img3, ( x, y))#最初のスライムの座標
        screen.blit(score_image, ( scox, scoy))
        screen.blit(time_image, ( 1020, 0))
       
        if count1 == 0:
            sco = 0
        
        if root1 < 50 :
            ey1 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex1 = random.randint(0, 1114)
            
            if level == 1:
                sco += 5
            
            if level == 2:
                sco += 10
            
            if level == 3:
                sco += 20
                    
        screen.blit(ene1, ( ex1, ey1))
            
        if root2 < 50 :
            ey2 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex2 = random.randint(0, 1114)
            
            if level == 1:
                sco += 8
            
            if level == 2:
                sco += 15
            
            if level == 3:
                sco += 30
                
        screen.blit(ene2, ( ex2, ey2))
        
        if root3 < 50 :
            ey3 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex3 = random.randint(0, 1114)
            ene3x = random.randint(0, 1)
            
            if level == 1:
                sco += 5
            
            if level == 2:
                sco += 10
            
            if level == 3:
                sco += 20
                
        screen.blit(ene3, ( ex3, ey3))
            
        if root4 < 50 :
            ey4 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex4 = random.randint(0, 1114)
            ene4x = random.randint(0, 1)
            
            if level == 1:
                sco += 10
            
            if level == 2:
                sco += 20
            
            if level == 3:
                sco += 40
                
        screen.blit(ene4, ( ex4, ey4))
        
        if root5 < 50 :
            ey5 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex5 = random.randint(0, 1114)
            ene5x = random.randint(0, 1)
            
            if level == 1:
                sco += 12  
            
            if level == 2:
                sco += 25
            
            if level == 3:
                sco += 50
                
        screen.blit(ene5, ( ex5, ey5))           
        
        if rootk1 < 50 :
            gameover = 1

        if rootk2 < 50 :
             gameover = 1
        
        if osu == 0:
        
           screen.blit(kou1, ( x , 2000))
       
        if osu == 1:
          
           screen.blit(kou1, ( px , py ))

        if teki1 == 0:
        
           screen.blit(kou2, ( 2000 , 2000))
       
        if teki1 == 1:
          
           screen.blit(kou2, ( kx1 , ky1 ))   

        if teki2 == 0:
        
           screen.blit(kou3, ( 2000 , 2000))
       
        if teki2 == 1:
          
           screen.blit(kou3, ( kx2 , ky2 ))   
        
        pygame.display.update()
        
        
def move(screen, root1, root2, root3, root4, root5, rootk1, rootk2, yajirusi):     #スライムを動かす
        global x, y, px, py, kx1, ky1, kx2, ky2, mxky, osu, teki1, teki2, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, ene3x, ene4x, ene5x, gameover, level
      
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]: #ue
            y = y - 10
        if y < -20:
            y = -20

        if key[pygame.K_s]:#sita
            y = y + 10
            if y > 720:
                y = 720
        
        if key[pygame.K_a]:#hidari
            x = x - 10
            if x < -16:
                x = -16
        
        if key[pygame.K_d]:#migi
            x = x + 10
            if x > 1114:
                x = 1114
                       
        if key[pygame.K_UP]: #攻撃
            if osu == 0 :
                 osu = 1
                 px = x
                 py = y
                
        if   osu == 1:  
               py = py - 15  # 速さ 弾
               if py <= 0 :
                   osu = 0
                   py = 2000
                   px = 2000   
                   
        if teki1 == 0 :
                    teki1 = 1 
            
        if teki2 == 0 :
                    teki2 = 1            
                    
        if level == 1:         
             
                 
            if   teki1 == 1:  
                ky1 = ky1 + 6  # 速さ 弾
                if ky1 > mxky :
                    teki1 = 0
                    ky1 = 0
                    kx1 = random.randint(0, 1114)   

                    
            if   teki2 == 1:  
                ky2 = ky2 + 8  # 速さ 弾
                if ky2 > mxky :
                    teki2 = 0
                    ky2 = 0
                    kx2 = random.randint(0, 1114)  
                    
                    
            ey1 = ey1 + 1.2  # ufo gray1 速さ
            if ey1 > 760 :   
                gameover = 1
                        
            ey2 = ey2 + 1.8  # ufo gray2 速さ
            if ey2 > 760 :
                gameover = 1
            
            ey3 = ey3 + 1.2  # ufo gray3 速さ
            
            if ey3 > 760 :
                gameover = 1
                
            if ene3x == 0:
                ex3 += 2.0
                if ex3 > 1114:
                    ene3x = 1
            if ene3x == 1:
                ex3 -= 2.0
                if ex3 < 0:
                    ene3x = 0        
                        
            
            ey4 = ey4 + 0.8  # ufo gray4 速さ
            if ey4 > 760 :
                gameover = 1    
            
            if ene4x == 0:
                ex4 += 6.5
                if ex4 > 1114:
                    ene4x = 1
            if ene4x == 1:
                ex4 -= 6.5
                if ex4 < 0:
                    ene4x = 0      
                    
             
            if ey5 > 760 : # ufo gray5 速さ
                gameover = 1
            
            if ene5x == 0:
                ex5 += 10
                if ex5 > 1114:
                    ey5 = ey5 + 60
                    ene5x = 1            
            if ene5x == 1:
                ex5 -= 10
                if ex5 < 0:
                    ey5 = ey5 + 60
                    ene5x = 0 
                    
        if level == 2:         
             
                 
            if   teki1 == 1:  
                ky1 = ky1 + 8  # 速さ 弾
                if ky1 > mxky :
                    teki1 = 0
                    ky1 = 0
                    kx1 = random.randint(0, 1114)   

                    
            if   teki2 == 1:  
                ky2 = ky2 + 10  # 速さ 弾
                if ky2 > mxky :
                    teki2 = 0
                    ky2 = 0
                    kx2 = random.randint(0, 1114)  
                    
                    
            ey1 = ey1 + 1.8  # ufo gray1 速さ
            if ey1 > 760 :   
                gameover = 1
                        
            ey2 = ey2 + 2.4  # ufo gray2 速さ
            if ey2 > 760 :
                gameover = 1
            
            ey3 = ey3 + 1.8  # ufo gray3 速さ
            
            if ey3 > 760 :
                gameover = 1
                
            if ene3x == 0:
                ex3 += 3.0
                if ex3 > 1114:
                    ene3x = 1
            if ene3x == 1:
                ex3 -= 3.0
                if ex3 < 0:
                    ene3x = 0        
                        
            
            ey4 = ey4 + 1.0  # ufo gray4 速さ
            if ey4 > 760 :
                gameover = 1    
            
            if ene4x == 0:
                ex4 += 7.4
                if ex4 > 1114:
                    ene4x = 1
            if ene4x == 1:
                ex4 -= 7.4
                if ex4 < 0:
                    ene4x = 0 
            
        
            if ey5 > 760 : # ufo gray5 速さ
                gameover = 1
            
            if ene5x == 0:
                ex5 += 20
                if ex5 > 1114:
                    ey5 = ey5 + 60
                    ene5x = 1            
            if ene5x == 1:
                ex5 -= 20
                if ex5 < 0:
                    ey5 = ey5 + 60
                    ene5x = 0 
           
        if level == 3:    
            
            key = pygame.key.get_pressed()
            if key[pygame.K_w]: #ue
                y = y - 10
            if y < -20:
                y = -20

            if key[pygame.K_s]:#sita
                y = y + 10
                if y > 720:
                    y = 720
            
            if key[pygame.K_a]:#hidari
                x = x - 10
                if x < -16:
                    x = -16
            
            if key[pygame.K_d]:#migi
                x = x + 10
                if x > 1114:
                    x = 1114
                        
            if key[pygame.K_UP]: #攻撃
                if osu == 0 :
                    osu = 1
                    px = x
                    py = y
                    
            if   osu == 1:  
                py = py - 15  # 速さ 弾
                if py <= 0 :
                    osu = 0
                    py = 2000
                    px = 2000        
             
                 
            if   teki1 == 1:  
                ky1 = ky1 + 16  # 速さ 弾
                if ky1 > mxky :
                    teki1 = 0
                    ky1 = 0
                    kx1 = random.randint(0, 1114)   

                    
            if   teki2 == 1:  
                ky2 = ky2 + 20  # 速さ 弾
                if ky2 > mxky :
                    teki2 = 0
                    ky2 = 0
                    kx2 = random.randint(0, 1114)  
                    
                    
            ey1 = ey1 + 3.6  # ufo gray1 速さ
            if ey1 > 760 :   
                gameover = 1
                        
            ey2 = ey2 + 4.8  # ufo gray2 速さ
            if ey2 > 760 :
                gameover = 1
            
            ey3 = ey3 + 3.6  # ufo gray3 速さ
            
            if ey3 > 760 :
                gameover = 1
                
            if ene3x == 0:
                ex3 += 6.0
                if ex3 > 1114:
                    ene3x = 1
            if ene3x == 1:
                ex3 -= 6.0
                if ex3 < 0:
                    ene3x = 0        
                        
            
            ey4 = ey4 + 2.0  # ufo gray4 速さ
            if ey4 > 760 :
                gameover = 1    
            
            if ene4x == 0:
                ex4 += 14.8
                if ex4 > 1114:
                    ene4x = 1
            if ene4x == 1:
                ex4 -= 14.8
                if ex4 < 0:
                    ene4x = 0      
                    
            
            if ey5 > 760 : # ufo gray5 速さ
                gameover = 1
            
            if ene5x == 0:
                ex5 += 30
                if ex5 > 1114:
                    ey5 = ey5 + 160
                    ene5x = 1            
            if ene5x == 1:
                ex5 -= 30
                if ex5 < 0:
                    ey5 = ey5 + 60
                    ene5x = 0 
  
            
def main():
     global x, y, px, py, kx1, ky1, kx2, ky2, mxky, osu, teki1, teki2, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, ene3x, ene4x, ene5x, gameover, sco, scox, scoy, cou, count1, start, mouse_x, mouse_y, mouse_pos, level, time, time_finish, time_print,clock
     pygame.init()
     clock = pygame.time.Clock()
     screen = pygame.display.set_mode(( 1200, 800))    # 1530 790
     img3 = pygame.image.load("画像/スライム（背景なし）.png")
     hai1 = pygame.image.load("画像/yakei.hai.jpg")
     kou1 = pygame.image.load("画像/kougeki.png")
     kou2 = pygame.image.load("画像/kou2.png")
     kou3 = pygame.image.load("画像/kou3.png")
     ene1 = pygame.image.load("画像/ufo_gray.png")
     ene2 = pygame.image.load("画像/ufo_gray_2.png")
     ene3 = pygame.image.load("画像/ufo_green.png")
     ene4 = pygame.image.load("画像/ufo_purple.png")
     ene5 = pygame.image.load("画像/ufo_wide.png")
     cou1 = pygame.image.load("画像/cou1.png")
     cou2 = pygame.image.load("画像/cou2.png")
     cou3 = pygame.image.load("画像/cou3.png")
     easy = pygame.image.load("画像/easy.png")
     hard = pygame.image.load("画像/hard.png")
     ex   = pygame.image.load("画像/EX.png")
     yajirusi = pygame.image.load("画像/yajirusi.png")
     img3 = pygame.transform.scale(img3,( 100, 90))
     hai1 = pygame.transform.scale(hai1,( 1200, 800))
     kou1 = pygame.transform.scale(kou1,( 100, 90))
     ene1 = pygame.transform.scale(ene1,( 100, 60))
     ene2 = pygame.transform.scale(ene2,( 100, 60))
     ene3 = pygame.transform.scale(ene3,( 100, 60))
     ene4 = pygame.transform.scale(ene4,( 100, 60))
     ene5 = pygame.transform.scale(ene5,( 100, 60))
     kou2 = pygame.transform.scale(kou2,( 50, 50))
     kou3 = pygame.transform.scale(kou3,( 50, 50))
     cou1 = pygame.transform.scale(cou1,( 300, 360))
     cou2 = pygame.transform.scale(cou2,( 300, 360))
     cou3 = pygame.transform.scale(cou3,( 300, 360))
     easy = pygame.transform.scale(easy,( 350, 200))
     hard = pygame.transform.scale(hard,( 350, 200))
     ex   = pygame.transform.scale(ex,( 350, 200))


     font = pygame.font.Font("テキスト/DotGothic16-Regular.ttf " , 100)
     font_keypress = pygame.font.Font("テキスト/DotGothic16-Regular.ttf ", 50)  
    
     
     while True:
        FPS = 60
        clock.tick(FPS)
        root1 = math.sqrt((ex1 - px)**2 + (py - ey1)**2)
        root2 = math.sqrt((ex2 - px)**2 + (py - ey2)**2)
        root3 = math.sqrt((ex3 - px)**2 + (py - ey3)**2)
        root4 = math.sqrt((ex4 - px)**2 + (py - ey4)**2)
        root5 = math.sqrt((ex5 - px)**2 + (py - ey5)**2)
        rootk1 = math.sqrt((x - (kx1 - 20))**2 + ((ky1 - 40) - y)**2)
        rootk2 = math.sqrt((x - (kx2 - 20))**2 + ((ky2 - 40) - y)**2)
        
        score_image = font.render (str(sco) , True ,pygame.Color("white"))
        score_image_game = font.render (("gameover") , True ,pygame.Color("red"))
        
        if time >= time_finish:
            score_image_game = font.render (("game clear"), True, pygame.Color("yellow"))
            
        keypress_image = font_keypress.render (("title/G   replay/SPACE") , True ,pygame.Color("white"))
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_pos
        
        time_image = font.render (str( int(abs(time - time_finish))) , True, pygame.Color("white"))
        
        time = pygame.time.get_ticks()
        time = time / 1000
        
        
        if gameover == 1:
            
            if scox == 0:
                scox = 2000
                scoy = 2000
                draw(screen, img3, hai1, kou1, kou2, kou3, ene1, ene2, ene3, ene4, ene5, root1, root2, root3, root4, root5, rootk1, rootk2, score_image, cou1, cou2, cou3, time_image)
                
                screen.blit(score_image_game, ( 400, 250))    
                screen.blit(keypress_image, (350, 460))    
                
                if sco < 10:
                    screen.blit(score_image, (570, 350))
                    
                if sco < 100 and sco >= 10:
                        screen.blit(score_image, (550, 350))
                    
                        
                if sco < 1000 and sco >= 100:
                        screen.blit(score_image, (520, 350))
                        
                if sco < 10000 and sco >= 1000:
                        screen.blit(score_image, (500, 350))
                    
                                
                pygame.display.update()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.event.clear()
        
        
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            break
        
        if gameover == 1:
            
            if key_pressed[pygame.K_SPACE]:
                reset()
                time_finish = pygame.time.get_ticks() + 94000
                time_finish = time_finish / 1000
                
            if key_pressed[pygame.K_g]:
                reset()
                start = 1
                time_finish = pygame.time.get_ticks() +94000
                time_finish = time_finish / 1000
            
        if start == 1:
            draw_back(screen, easy, hard, ex, yajirusi)

            move_back(screen)
            
            
        else:
            if gameover == 0:
                
                draw(screen, img3, hai1, kou1, kou2, kou3, ene1, ene2, ene3, ene4, ene5, 
                root1, root2, root3, root4, root5, rootk1, rootk2, score_image, cou1, cou2, cou3, time_image)
                
                if count1 == 0:
                    count(screen, cou1, cou2, cou3)
                
                if cou == 0: 
                    move(screen, root1, root2, root3, root4, root5, rootk1, rootk2, yajirusi)
                
                if start == 0:
                    limit(score_image_game)
           
            
     pygame.quit()


start = 1 
level = 1
reset()
main()