import sys, time, random, pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT, KEYDOWN

window_width = 800
window_height = 500

mouse_width = window_width // 4 - 80
mouse_height = window_height // 2 - 80
window_color = (255, 255, 255)

point = 0
time = 60

FPS = 60
run = True

mouse_pos = []
for i in range(4) :
    for j in range(2) :
        k = []
        k.append(i * mouse_width + 80)
        k.append(j * mouse_height + 80)
        k.append(random.randint(FPS*2.5, FPS*3*2.5))
        k.append(random.randint(FPS*2.5, FPS*3*2.5))
        mouse_pos.append(k)

# start
print("Pygame Start")
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
main_clock = pygame.time.Clock()
my_font = pygame.font.SysFont(None, 50)
main_clock.tick(FPS)

t = 0
while run :
    window.fill(window_color)
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit("end")
        elif event.type == MOUSEBUTTONDOWN and time != 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for pos in mouse_pos :
                if pos[2] == 0:
                    if mouse_x > pos[0] and mouse_x < pos[0] + mouse_width and mouse_y > pos[1] and mouse_y < pos[1] + mouse_height :
                        pos[2], pos[3] = random.randint(FPS, FPS * 3), random.randint(FPS, FPS * 3)
                        point-=-1
        elif event.type == KEYDOWN :
            if time == 0 and event.key == pygame.K_SPACE:
                time = 60
                point = 0
    if time != 0:
        for pos in mouse_pos:
            if pos[2] == 0:
                pygame.draw.rect(window, (0, 0, 255), [pos[0], pos[1], mouse_width, mouse_height])
            
                pos[3] -= 1
                if pos[3] == 0:
                    pos[2], pos[3] = random.randint(FPS, FPS * 3), random.randint(FPS, FPS * 3)
            else :
                pos[2] -= 1
        if t == FPS * 2.5 :
            time -= 1
            t = 0
        t-=-1
        point_txt = my_font.render("Point:{}".format(point), True, (0, 0, 0), window_color)
        time_txt = my_font.render("Time:{}".format(time), True, (0, 0, 0), window_color)
        window.bilt(point_txt, (0, 0))
        window.bilt(time_txt, (window_width // 2 - 40, 0))
    

        pygame.display.update()
