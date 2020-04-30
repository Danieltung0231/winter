import sys, time
import random
import pygame
from pygame.locals import Color, QUIT, KEYDOWN

window_width = 1000
window_height = 800

balloon_width = 200
balloon_height = 200

balloon_position_x = window_width/2
balloon_position_y = window_height - balloon_height
heart = 10

window_color = (150, 150, 150)
enemy_color = (255, 0, 0)
enemy_num = 7
enemy_speed = 3

max_time = 0

# 紀錄敵人位置
enemy_position = []
for i in range(enemy_num):
    k = []
    k.append(random.randint(0,window_width))
    k.append(random.randint(0,window_width/10))
    enemy_position.append(k)

FPS = 60# 貞數
time = 0
run = True
life = True

# 定義角色
class Balloon(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.raw_image = pygame.image.load('balloon.png').convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (balloon_width, balloon_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (int(position_x), int(position_y))

# pygame開始
print("pygame Start")
pygame.init()# 初始化
window_surface = pygame.display.set_mode((window_width, window_height))# 定義視窗長寬
pygame.display.set_caption('gmae')# 設定標題
main_clock = pygame.time.Clock()# 設定時鐘
my_font = pygame.font.SysFont(None, 50)# 設定字體
main_clock.tick(FPS)# 控制遊戲迴圈迭代速率

t = 0
while run:
    # 偵測事件
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit("end")
        elif event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                if life == False:
                    life = True
                    heart = 10
                    time = 0
                    t = 0
                    for pos in enemy_position:
                        enemy_x = pos[0]
                        enemy_y = pos[1]
                        enemy_y = random.randint(0,window_width/10)
                        enemy_x = random.randint(0, window_width)
                        pos[0] = enemy_x
                        pos[1] = enemy_y
    if life:
        # 清除畫布
        window_surface.fill(window_color)
        # 更新角色位置
        balloon_position_x, mouse_y = pygame.mouse.get_pos()
        balloon = Balloon(balloon_position_x - balloon_width/2, balloon_position_y)
        window_surface.blit(balloon.image, balloon.rect)
        # 更新子彈位置
        for pos in enemy_position:
            enemy_x = pos[0]
            enemy_y = pos[1]
            if enemy_y > window_height-10:
                enemy_y = random.randint(0,window_width/10)
                enemy_x = random.randint(0, window_width)
            elif enemy_y > balloon_position_y and enemy_x > balloon_position_x - balloon_width/2 and enemy_x < balloon_position_x + balloon_width/2:
                enemy_y = random.randint(0,window_width/10)
                enemy_x = random.randint(0, window_width)
                heart -= 1
            enemy_y += enemy_speed
            pygame.draw.rect(window_surface, enemy_color, [enemy_x, enemy_y, 30, 30])
            pos[0] = enemy_x
            pos[1] = enemy_y
        t -=-1
        if t == FPS*2.5:
            time -=-1
            t = 0
        heart_txt = my_font.render('Heart: {}'.format(heart), True, (0, 0, 0))# 顯示血量
        time_txt = my_font.render('Time: {}'.format(time), True, (0, 0, 0))# 顯示時間
        # 渲染物件
        window_surface.blit(heart_txt, (10, 0))
        window_surface.blit(time_txt, (400, 0))
        if heart == 0 :
            life = False
            with open('time.txt', 'r') as f :
                max_time = int(f.read())
            if max_time < time :
                max_time = time
                with open("time.txt", "w") as f :
                    f.write(str(max_time))
    else :
        restart_txt = my_font.render("press SPACE to restart", True, (0, 0, 0))
        window_surface.blit(restart_txt, (window_width/2 - 60, window_height/2))
        max_time_txt = my_font.render("The most long time is {}".format(max_time), True, (0, 0, 0))
        window_surface.blit(max_time_txt, (window_width/2 - 60, window_height/2+30))
    
    pygame.display.update()# 畫面更新
