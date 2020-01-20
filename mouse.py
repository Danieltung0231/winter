import sys, time, random, pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT 

window_width = 800
window_height = 500

window_color = (255, 255, 255)

point = 0

FPS = 60
run = True

mouse_pos = []
for i in range(4):
    for j in range(2):
        k = []
        k.append(i * window_width // 5 + 20)
        k.append(j * window_height // 3 + 20)
        k.append(random.randint(FPS, FPS*3))
        mouse_pos.append(k)


# start
print("Pygame Start")
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
main_clock = pygame.time.Clock()
my_font = pygame.font.SysFont(None, 50)
main_clock.tick(FPS)

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit("end")
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    
    window.fill(window_color)

    for pos in mouse_pos:
        pygame.draw.rect(window, (0, 0, 255), [pos[0], pos[1], window_width // 5 , window_height // 3])

    pygame.display.update()