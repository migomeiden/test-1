# tesuto
from pygame.locals import *
import pygame
import sys
import math
import random
start = 1 
level = 1
alpha = 255 #255は不透明
delta = -5  #deltaの数字は消える速さ
score_ookisa = 0
score_ookisa_henkou = 1
setumei_button = 1

setumei_anime = 0

x_image = 100
y_image = -100
x_image_ufo = 450
y_image_ufo = -290
x_image_hikari = 450
y_image_hikari = -170
y_waku_scale = 200
command = 0
command_time = 0

     
def drew_back_setumei (screen,waku, rule, move_rule, attack_image, attack_rule, yajirusi_migi, yajirusi_hidari, 
                       shasin_clear, shasin_kougeki, shasin_bakuhatu, batu_button, shasin_kougeki_si, shasin_teki_jimenn, shasin_game_over, haikei_ufo, hikari):   
        global setumei_anime,x_image,y_image, setumei_button, alpha, delta, x_image_ufo, y_image_ufo, x_image_hikari, y_image_hikari, y_waku_scale
        
        font_game = pygame.font.Font("テキスト/DotGothic16-Regular.ttf " , 50)
        yajirusi_hidari.set_alpha( alpha) #imageの透明度を設定
        yajirusi_migi.set_alpha( alpha) #imageの透明度を設定
        escape = font_game.render (("escape") , True ,pygame.Color("white")) 
        escape = pygame.transform.scale(escape,( 50, 30))
        
        if setumei_anime == 0 :
 
                 
                  
              #  ルール説明のボード
                waku = pygame.transform.scale(waku,( 1000, y_waku_scale))
                hikari = pygame.transform.scale(hikari,( 300, 80))  
                  
                y_image += 10       #  動かくデイ
                y_image_ufo += 10
                y_image_hikari += 10
                y_waku_scale += 20
                
                screen.blit(hikari, (x_image_hikari, y_image_hikari))
                screen.blit(haikei_ufo, ( x_image_ufo, y_image_ufo))
                screen.blit(waku, ( x_image, y_image))
                
                pygame.display.update()

                if  y_image <= 100 and y_waku_scale <=600:     # 来てほしいとこまできてなかったら？
                
                    return
                
                else :

                        setumei_anime = 1
                    

      
      
       
        
        screen.blit(waku, ( x_image, y_image))
     
        batu_button = pygame.transform.scale(batu_button,( 50, 50))
        
        
        if mouse_x >= 1030 and mouse_x <= 1080 and mouse_y >= 130 and mouse_y <= 180:
            batu_button.set_alpha(255)
            
        else:
            batu_button.set_alpha(150)
            
            
        screen.blit(batu_button, ( 1030,130)) 
        screen.blit(escape, (1030, 165))
        
        if setumei_button == 1:

            screen.blit(rule, (270, 260))
            screen.blit(move_rule, (348, 510))
            screen.blit(attack_image, (755, 290))
            screen.blit(attack_rule, (780, 510))
            screen.blit(yajirusi_migi, (1030, 375))
            
        if setumei_button == 2:
            rule_font_1 = font_game.render (("敵を攻撃で撃破して、得点を獲得しよう！！") , True ,pygame.Color("white")) 
            rule_font_2 = font_game.render (("攻撃ボタンを押すと、攻撃が出るぞ！") , True ,pygame.Color("white")) 
            rule_font_3 = font_game.render (("攻撃をあてると敵が爆破し、新たな敵が出てくるぞ！") , True ,pygame.Color("white")) 
            rule_font_1 = pygame.transform.scale(rule_font_1,(800, 110))
            rule_font_2 = pygame.transform.scale(rule_font_2,(650, 70))
            rule_font_3 = pygame.transform.scale(rule_font_3,(750, 70))
            
            screen.blit(rule_font_1, (210, 150))
            screen.blit(rule_font_2, (270, 380))
            screen.blit(rule_font_3, (230, 590))
            screen.blit(shasin_kougeki, (545, 270))
            screen.blit(shasin_bakuhatu, (545, 480))
            screen.blit(yajirusi_migi, (1030, 375))
            screen.blit(yajirusi_hidari, (110, 375))
        
        if setumei_button == 3:
            
            rule_font_4 = font_game.render (("６０秒間耐えればゲームクリア ^ ^") , True ,pygame.Color("white"))
            rule_font_4 = pygame.transform.scale(rule_font_4,(740, 80))
            
            screen.blit(yajirusi_migi, (1030, 375))
            screen.blit(yajirusi_hidari, (110, 375))
            screen.blit(shasin_clear, (310, 175))
            screen.blit(rule_font_4, (230, 550))
            
        if setumei_button == 4:
            
            rule_font_5 = font_game.render (("敵が地面に来るか、敵の攻撃に当たるとゲームオーバー ; ;") , True ,pygame.Color("white")) 
            rule_font_5 = pygame.transform.scale(rule_font_5,(750, 70))
            screen.blit(shasin_kougeki_si, (395, 490))
            
            screen.blit(shasin_teki_jimenn, (695, 490))
            screen.blit(shasin_game_over, (310, 175))
            screen.blit(rule_font_5, (230, 590))
            screen.blit(yajirusi_hidari, (110, 375))
        
        pygame.display.update()


def  becomebig (screen,score_image):
        global sco, score_ookisa , score_ookisa_henkou
        
        if score_ookisa > 6:
            score_ookisa = 0
        
        if score_ookisa < 1 :
            score_ookisa_henkou = 1
            
        if score_ookisa > 5 :
            score_ookisa_henkou = -1
            
        if score_ookisa >= 1 :
             score_ookisa +=  score_ookisa_henkou
             
        if score_ookisa_henkou == -1 :
          score_ookisa +=  score_ookisa_henkou
          
        if score_ookisa == 1 :
                score_image = pygame.transform.scale(score_image,( 60, 150))
                
                screen.blit(score_image, ( scox, scoy))
                
        if score_ookisa == 2 :
            
                if sco < 100:
                    score_image = pygame.transform.scale(score_image,( 70, 160))
                    
                else:
                    score_image = pygame.transform.scale(score_image,( 90, 170))
                    
                screen.blit(score_image, ( scox, scoy))
                
        if score_ookisa == 3 :
            
                if sco < 100:
                    score_image = pygame.transform.scale(score_image,( 80, 170))
                    
                else:
                    score_image = pygame.transform.scale(score_image,( 120, 190))
                    
                screen.blit(score_image, ( scox, scoy))
                
        if score_ookisa == 4 :
            
                if sco < 100:
                     score_image = pygame.transform.scale(score_image,( 90, 180))
                    
                else:
                    score_image = pygame.transform.scale(score_image,( 150, 210))
                    
                screen.blit(score_image, ( scox, scoy))
                
        if score_ookisa == 5 :
            
                if sco < 100:
                    score_image = pygame.transform.scale(score_image,( 100, 190))
                    
                else:
                  score_image = pygame.transform.scale(score_image,( 180, 230))
                  
                screen.blit(score_image, ( scox, scoy))

 
def limit(score_image_game):
    global time, time_finish, gameover
    
    if time >= time_finish:
        font = pygame.font.Font(None, 100)
        score_image_game = font.render (("game clear"), True, pygame.Color("yellow"))
        
        gameover = 1


def countdown(screen, cou1, cou2, cou3, rule):
    global cou, gameover, count1, time_finish
    
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
            pygame.time.wait(900)
            return
            
        if cou == 3:
            cou = 2
            screen.blit(cou2, ( 480, 200))
            pygame.display.update()
            pygame.time.wait(900)
            return    
        
        if cou == 2:
            screen.blit(cou1, ( 480, 200))
            pygame.display.update()
            pygame.time.wait(900)
            cou = 0
            
            count1 = 1
            gameover = 0
            time_finish = pygame.time.get_ticks() +61000
            time_finish = time_finish / 1000
            return
        

def reset():
    global x, y, osu, teki1, teki2, py, px, kx1, ky1, kx2, ky2, mxky, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, gameover, ene3x, ene4x, ene5x, sco, scox, scoy, cou, count1, start, level, time, time_finish, time_print, score_ookisa, score_ookisa_henkou
    x = 570
    y = 400
    osu = 0
    teki1 = 0
    teki2 = 0
    py = 2000#自分の攻撃
    px = 2000#自分の攻撃
    kx1 = random.randint(0, 1114) #敵からの攻撃
    ky1 = 0
    kx2 = random.randint(0, 1114) #敵からの攻撃
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
    time_finish = 60
    time_print = 0
    
    score_ookisa = 0
    score_ookisa_henkou = 1
    
    x_image = 100
    y_image = -100


def draw_back(screen, easy, hard, ex, yajirusi, setumei, waku, rule, move_rule, attack_image, attack_rule, yajirusi_migi, yajirusi_hidari, 
              shasin_clear, shasin_kougeki, shasin_bakuhatu, batu_button, shasin_kougeki_si, shasin_teki_jimenn, shasin_game_over, haikei_ufo, hikari):
    global level, alpha, toumei1, setumei_button, x_image, y_image, setumei_anime
    
    
    screen.fill(pygame.Color("#613898"))
        
    screen.blit(easy, ( 30, 450))
    screen.blit(hard, ( 420, 450))
    screen.blit(ex, ( 810, 450))
    easy.set_alpha( 120) #imageの透明度を設定
    hard.set_alpha( 120) #imageの透明度を設定
    ex.set_alpha( 120) #imageの透明度を設定
    screen.blit(setumei, ( 1025, 650))
    
        
    if level == 1:
        screen.blit(yajirusi, (185, 400))
        easy.set_alpha( 255) #imageの透明度を設定
        
    if level == 2:
        screen.blit(yajirusi, (575, 400))
        hard.set_alpha( 255) #imageの透明度を設定
        
    if level == 3:
        screen.blit(yajirusi, (965, 400))
        ex.set_alpha( 255) #imageの透明度を設定
        
    if level == 0:
        screen.blit(yajirusi, (1075, 650))
     
    font_game = pygame.font.Font("テキスト/DotGothic16-Regular.ttf " , 50)
    start_image_SPACE = font_game.render (("--- スペースを押してスタート ---") , True ,pygame.Color("black")) 
    start_image_SPACE.set_alpha( alpha) #imageの透明度を設定
    screen.blit(start_image_SPACE, ( 200, 680))
    
    start_image_arrow = font_game.render ((" 矢印キーを押す ") , True ,pygame.Color("black"))
    start_image_arrow.set_alpha( alpha) #imageの透明度を設定
    screen.blit(start_image_arrow, ( 370, 225))
    
    start_image_or = font_game.render (("---         または          ---") , True ,pygame.Color("black"))
    start_image_or.set_alpha( alpha) #imageの透明度を設定
    screen.blit(start_image_or, ( 180, 275))
    
    start_image_click = font_game.render ((" クリックで難易度選択 ") , True ,pygame.Color("black"))
    start_image_click.set_alpha( alpha) #imageの透明度を設定
    screen.blit(start_image_click, ( 280, 325))
    
    start_image_title_shadow = font_game.render ((" スライム vs UFO ") , True ,pygame.Color(62, 193, 236))
    start_image_title_shadow = pygame.transform.scale(start_image_title_shadow,( 1000, 120))
    screen.blit(start_image_title_shadow, ( 93, 53))
    
    start_image_title = font_game.render ((" スライム vs UFO ") , True ,pygame.Color("white"))
    start_image_title = pygame.transform.scale(start_image_title,( 1000, 120))
    screen.blit(start_image_title, ( 90, 50))
    
    if level == -1:
        

        drew_back_setumei(screen,waku, rule, move_rule, attack_image, attack_rule, yajirusi_migi, yajirusi_hidari, 
                          shasin_clear, shasin_kougeki, shasin_bakuhatu, batu_button, shasin_kougeki_si, shasin_teki_jimenn, shasin_game_over, haikei_ufo, hikari)
    
    pygame.display.update()


def move_back(screen, easy, hard, ex, waku):
    global start, mouse_x, mouse_y, mouse_pos, level ,clock, alpha, setumei_button, x_image, y_image, setumei_anime, setumei_button, x_image_ufo, y_image_ufo, x_image_hikari, y_image_hikari, y_waku_scale
    
    reset()
    key = pygame.key.get_pressed()
    FPS = 60
    renzokubousi_migi = 0
    renzokubousi_hidari = 0
    if level == 1 :
    
        if key[pygame.K_RIGHT]:
            
            pygame.time.wait(100)
            easy.set_alpha( 120) #imageの透明度を設定
            level = 2
            pygame.event.clear()
            
            clock.tick(FPS)
            return
        
        if key[pygame.K_DOWN]:
            level = 0
            pygame.event.clear()
            
    if level == 2:
            
        if key[pygame.K_RIGHT]:
            
                pygame.time.wait(100)
                hard.set_alpha( 120) #imageの透明度を設定
                level = 3 
                pygame.event.clear()
                return
                
        if key[pygame.K_LEFT]: 
  
                pygame.time.wait(100)
                hard.set_alpha( 120) #imageの透明度を設定
                level = 1
                pygame.event.clear()
                return
            
        if key[pygame.K_DOWN]:
            level = 0 
            pygame.event.clear()

                
    if level == 3:
        
        if key[pygame.K_LEFT]:
        
            pygame.time.wait(100)  
            ex.set_alpha( 120) #imageの透明度を設定
            level = 2 
            pygame.event.clear()
            clock.tick(FPS)
            return
        
        if key[pygame.K_DOWN]:
            level = 0
            pygame.event.clear()
            
    if level == 0 and key[pygame.K_UP]:
        level = 1
        pygame.event.clear()
        
    if level == -1:
        
        if setumei_button == 1 and key[pygame.K_RIGHT]:
            pygame.time.wait(200)  
            setumei_button = 2         
            renzokubousi_migi = 1
            pygame.event.clear()
            return
            
        if setumei_button == 2:
            
            if key[pygame.K_LEFT]:
                pygame.time.wait(200)
                
                if renzokubousi_hidari == 0:
                    setumei_button = 1
                    renzokubousi_hidari = 1
                else:    
                    renzokubousi_hidari = 0
                    
                pygame.event.clear()
                return
                
            if key[pygame.K_RIGHT]:
                pygame.time.wait(200)  
                if renzokubousi_migi == 0:
                    setumei_button = 3
                    renzokubousi_migi = 1
                else:    
                    renzokubousi_migi = 0
                    
                pygame.event.clear()
                return
            
        if setumei_button == 3:
            
            if key[pygame.K_LEFT]:
                pygame.time.wait(200)
                
                if renzokubousi_hidari == 0:
                    setumei_button = 2
                    renzokubousi_hidari = 1
                else:    
                    renzokubousi_hidari = 0
                    
                pygame.event.clear()
                return
            
            if key[pygame.K_RIGHT]:
                pygame.time.wait(200)
                
                if renzokubousi_migi == 0:
                    setumei_button = 4
                    renzokubousi_migi = 1
                else:    
                    renzokubousi_migi = 0
                    
                pygame.event.clear()
                return
            
        if setumei_button == 4:
            
            if key[pygame.K_LEFT]:
                pygame.time.wait(200)
                
                if renzokubousi_hidari == 0:
                    setumei_button = 3
                    renzokubousi_hidari = 1
                else:    
                    renzokubousi_hidari = 0
                    
                pygame.event.clear()
                return
            
      #      if key[pygame.K_RIGHT]:
      #          setumei_button = 5
      #          pygame.event.clear()
                
 
            
        
    for event in pygame.event.get():   
        
        if event.type == MOUSEBUTTONDOWN and event.button == 1: 
            
            if level != -1:
            
                if mouse_x >= 75 and mouse_x <= 335 and mouse_y >= 415 and mouse_y <= 585:
                    level = 1
                    
                if mouse_x >= 465 and mouse_x <= 725 and mouse_y >= 415 and mouse_y <= 585:
                    level = 2
                    
                if mouse_x >= 855 and mouse_x <= 1115 and mouse_y >= 415 and mouse_y <= 585:
                    level = 3
                
            else:
                if mouse_x >= 1030 and mouse_x <= 1080 and mouse_y >= 130 and mouse_y <= 180:
                

                    x_image = 100
                    y_image = -100
                    x_image_ufo = 450
                    y_image_ufo = -290
                    x_image_hikari = 450
                    y_image_hikari = -170
                    y_waku_scale = 200
                    
                    setumei_anime = 0
                    
                    level = 0
                    
                    setumei_button = 1
                    
                
    if key[pygame.K_SPACE]:
        
        if level == 1 or level == 2 or level ==  3:    
            start = 0
            
        else: 
            level = -1
            

def draw(screen, img3, hai1, kou1, kou2, kou3, ene1, ene2, ene3, ene4, ene5, 
         root1, root2, root3, root4, root5, rootk1, rootk2, score_image, cou1, cou2, cou3, time_image, rule, move_rule, attack_image, attack_rule, bakuhatu):
        global x, y, px, py, kx1, ky1, kx2, ky2, osu, teki1, teki2, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, ene3x, ene4x, ene5x, sco, scox, scoy, gameover, count1, level,alpha, score_ookisa, score_ookisa_henkou
        screen.fill(pygame.Color("white"))
        screen.blit(hai1, ( 0, 0))
        screen.blit(img3, ( x, y))#最初のスライムの座標
        becomebig(screen, score_image)
        if score_ookisa == 0:
            screen.blit(score_image, ( scox, scoy))
        screen.blit(time_image, ( 1020, 0))
        attack_image = pygame.transform.scale(attack_image,( 150, 225))
        bakuhatu.set_alpha( 190) #imageの透明度を設定
        
    #    if not cou == 0:
    #        screen.blit(rule, (200, 220))
    #        screen.blit(move_rule, (278, 470))
     #       screen.blit(attack_image, (825, 250))
     #       screen.blit(attack_rule, (850, 470))
        
       
        if count1 == 0:
            sco = 0
        
        if root1 < 50 :
            screen.blit(bakuhatu, ( ex1, ey1))  
            ey1 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex1 = random.randint(0, 1114)
            
            if score_ookisa == 0:
                score_ookisa = 1
            
            if level == 1:
                sco += 5
            
            if level == 2:
                sco += 10
            
            if level == 3:
                sco += 20
                
            
                    
        screen.blit(ene1, ( ex1, ey1))
          
        
        if root2 < 50 :
            screen.blit(bakuhatu, ( ex2, ey2))
            ey2 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex2 = random.randint(0, 1114)
            
            if score_ookisa == 0:
                score_ookisa = 1
            
            if level == 1:
                sco += 8
            
            if level == 2:
                sco += 15
            
            if level == 3:
                sco += 30
            
            
                
        screen.blit(ene2, ( ex2, ey2))
        
        
        if root3 < 50:
            screen.blit(bakuhatu, ( ex3, ey3))    
            ey3 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex3 = random.randint(0, 1114)
            ene3x = random.randint(0, 1)
            
            if score_ookisa == 0:
                score_ookisa = 1
            
            if level == 1:
                sco += 5
            
            if level == 2:
                sco += 10
            
            if level == 3:
                sco += 20
                
            
                
        screen.blit(ene3, ( ex3, ey3))
        
            
        if root4 < 50 :
            screen.blit(bakuhatu, ( ex4, ey4))
            ey4 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex4 = random.randint(0, 1114)
            ene4x = random.randint(0, 1)
            
            if score_ookisa == 0:
                score_ookisa = 1
            
            if level == 1:
                sco += 10
            
            if level == 2:
                sco += 20
            
            if level == 3:
                sco += 40
                
                
        screen.blit(ene4, ( ex4, ey4))
        

        if root5 < 50 :
            screen.blit(bakuhatu, ( ex5, ey5)) 
            ey5 = 10 
            osu = 0
            py = 2000
            px = 2000
            ex5 = random.randint(0, 1114)
            ene5x = random.randint(0, 1)
            
            if score_ookisa == 0:
                score_ookisa = 1
            
            if level == 1:
                sco += 12  
            
            if level == 2:
                sco += 25
            
            if level == 3:
                sco += 50
                
               
                
        screen.blit(ene5, ( ex5, ey5))           
               
        
        if rootk1 < 45 :
            gameover = 1

        if rootk2 < 45 :
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
     global x, y, px, py, kx1, ky1, kx2, ky2, mxky, osu, teki1, teki2, ex1, ey1, ex2, ey2, ex3, ey3, ex4, ey4, ex5, ey5, ene3x, ene4x, ene5x, gameover, sco, scox, scoy, cou, count1, start, mouse_x, mouse_y, mouse_pos, level, time, time_finish, time_print,clock, alpha, delta, setumei_anime, setumei_button, x_image, y_image, x_image_hikari, y_image_hikari, x_image_ufo, y_image_ufo, y_waku_scale, command, command_time
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
     rule = pygame.image.load("画像/wasd.png")
     yajirusi = pygame.image.load("画像/yajirusi.png")
     bakuhatu = pygame.image.load("画像/爆発.png")
     setumei = pygame.image.load("画像/ru-ru.png")
     waku = pygame.image.load("画像/枠.png")
     yajirusi_migi = pygame.image.load("画像/矢印＿右向き.png")
     yajirusi_hidari = pygame.image.load("画像/矢印＿左向き.png")
     shasin_clear = pygame.image.load("画像/スクリーンショット ゲームクリア.png")
     shasin_kougeki = pygame.image.load("画像/スクリーンショット 攻撃（自）.png")
     shasin_bakuhatu = pygame.image.load("画像/スクリーンショット 爆発エフェクト.png")
     shasin_kougeki_si = pygame.image.load("画像/スクリーンショット 攻撃(死).png")
     shasin_teki_jimenn = pygame.image.load("画像/スクリーンショット 敵　到達.png")
     shasin_game_over = pygame.image.load("画像/スクリーンショット ゲームオーバー.png")
     batu_button = pygame.image.load("画像/×ボタン.png")
     hikari = pygame.image.load("画像/hikari.png")
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
     rule = pygame.transform.scale(rule,( 250, 250))
     bakuhatu = pygame.transform.scale(bakuhatu,( 100, 100))
     setumei = pygame.transform.scale(setumei,( 150, 150))
     waku = pygame.transform.scale(waku,( 1000, 600))
     yajirusi_migi = pygame.transform.scale(yajirusi_migi,( 60, 60))
     yajirusi_hidari = pygame.transform.scale(yajirusi_hidari,( 60, 60))
     shasin_clear = pygame.transform.scale(shasin_clear,( 575, 350))
     shasin_kougeki = pygame.transform.scale(shasin_kougeki,( 120, 100))
     shasin_bakuhatu = pygame.transform.scale(shasin_bakuhatu,( 120, 100))
     shasin_kougeki_si = pygame.transform.scale(shasin_kougeki_si,( 120, 100))
     shasin_teki_jimenn = pygame.transform.scale(shasin_teki_jimenn,( 120, 100))
     shasin_game_over = pygame.transform.scale(shasin_game_over,( 575, 300))
     haikei_ufo = pygame.transform.scale(ene1,( 300, 150))

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
        rootk1 = math.sqrt((x - (kx1 - 20))**2 + ((ky1 - 20) - y)**2)
        rootk2 = math.sqrt((x - (kx2 - 20))**2 + ((ky2 - 20) - y)**2)
        
        score_image = font.render (str(sco) , True ,pygame.Color("white"))
        score_image_game = font.render (("gameover") , True ,pygame.Color("red"))
        
        if time >= time_finish:
            score_image_game = font.render (("game clear"), True, pygame.Color("yellow"))

        keypress_image = font_keypress.render (("タイトルへ戻る/G   リスタート/SPACE") , True ,pygame.Color("white"))
        move_rule = font_keypress.render (("移動") , True ,pygame.Color("white"))
        attack_image = font_keypress.render (("↑") , True ,pygame.Color("white"))
        attack_rule = font_keypress.render (("攻撃") , True ,pygame.Color("white"))
        
        attack_image = pygame.transform.scale(attack_image,( 120, 180))
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_pos
        
        if cou == 0:
            time_image = font.render (str( int(abs(time - time_finish))) , True, pygame.Color("white"))
        else:
            time_image = font.render (("60") , True, pygame.Color("white"))
            
            
        #計算
        alpha += delta
        if alpha <= 0 or alpha >=255:
            delta = -delta
            
        time = pygame.time.get_ticks()
        time = time / 1000
        
        
        if gameover == 1:
            
            if scox == 0:
                scox = 2000
                scoy = 2000
                draw(screen, img3, hai1, kou1, kou2, kou3, ene1, ene2, ene3, ene4, ene5, root1, root2, root3, root4, root5, rootk1, rootk2, score_image, cou1, cou2, cou3, time_image, rule, move_rule, attack_image, attack_rule, bakuhatu)
                
                screen.blit(score_image_game, ( 400, 250))    
                screen.blit(keypress_image, (150, 460))    
                
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
            
            if level == -1:

                    x_image = 100
                    y_image = -100
                    x_image_ufo = 450
                    y_image_ufo = -290
                    x_image_hikari = 450
                    y_image_hikari = -170
                    y_waku_scale = 200
                    
                    setumei_anime = 0
                    
                    level = 0
                    
                    setumei_button = 1
                
            pygame.event.clear()
            
            
        if command_time <= 0:
            command = 0
            command_time
            
        command_time -= 1   
            
        if key_pressed[pygame.K_m] and command == 0 :
            command = 1
            command_time = 70
            
            
        if key_pressed[pygame.K_e] and command == 1 :
            command = 2
            
            
        if key_pressed[pygame.K_i] and command == 2 :
            command = 3
            
            
        if key_pressed[pygame.K_d] and command == 3 :
            command = 4
            
            
        if key_pressed[pygame.K_e] and command == 4 :
            command = 5
            
            
        if key_pressed[pygame.K_n] and command == 5 :
            command = 6
            
            
            
        if command == 6:
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
            draw_back(screen, easy, hard, ex, yajirusi, setumei, waku, rule, move_rule, attack_image, attack_rule, yajirusi_migi, yajirusi_hidari, 
                      shasin_clear, shasin_kougeki, shasin_bakuhatu, batu_button, shasin_kougeki_si, shasin_teki_jimenn, shasin_game_over, haikei_ufo, hikari)
            move_back(screen, easy, hard, ex, waku)
            
            
        else:
            if gameover == 0:
                
                draw(screen, img3, hai1, kou1, kou2, kou3, ene1, ene2, ene3, ene4, ene5, 
                root1, root2, root3, root4, root5, rootk1, rootk2, score_image, cou1, cou2, cou3, time_image, rule, move_rule, attack_image, attack_rule, bakuhatu)
                
                if count1 == 0:
                    countdown(screen, cou1, cou2, cou3, rule)
                
                if cou == 0: 
                    move(screen, root1, root2, root3, root4, root5, rootk1, rootk2, yajirusi)
                
                if start == 0:
                    limit(score_image_game)
           
            
     pygame.quit()


reset()
main()
