import sys, time
import random
import pygame
from pygame.locals import Color, QUIT

window_width = 1000
window_height = 800

balloon_width = 200
balloon_height = 200

balloon_position_x = window_width/2
balloon_position_y = window_height - balloon_height
heart = 10

enemy_position = []
for i in range(7):
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
        super().kill()
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
            sys.exit()
    if life:
        # 清除畫布
        window_surface.fill((255,255,255))
        # 更新角色位置
        balloon_position_x, mouse_y = pygame.mouse.get_pos()
        balloon = Balloon(balloon_position_x - balloon_width/2, balloon_position_y)
        window_surface.blit(balloon.image, balloon.rect)
        # 更新子彈位置
        for pos in enemy_position:
            if pos[1] > window_height-10:
                pos[1] = random.randint(0,window_width/10)
                pos[0] = random.randint(0, window_width)
            if pos[1] > balloon_position_y and pos[0] > balloon_position_x - balloon_width/2 and pos[0] < balloon_position_x + balloon_width/2:
                pos[1] = random.randint(0,window_width/10)
                pos[0] = random.randint(0, window_width)
                heart -= 1
            pos[1] -=-3
            pygame.draw.rect(window_surface, (255,0,0), [pos[0], pos[1], 30, 30])
        t -=-1
        if t == FPS*2.5:
            time -=-1
            t = 0
        heart_txt = my_font.render('Heart: {}'.format(heart), True, (0, 0, 0))# 顯示血量
        time_txt = my_font.render('Time: {}'.format(time), True, (0, 0, 0))
        window_surface.blit(heart_txt, (10, 0))# 渲染物件
        window_surface.blit(time_txt, (400, 0))
        if heart == 0:
            life = False
    
    pygame.display.update()# 畫面更新

