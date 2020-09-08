import pygame, sys

# 初始化
pygame.init()
# 设置屏幕的宽度，高度
SCREEN = pygame.display.set_mode((400, 300))
# 设置窗口的标题
pygame.display.set_caption('Hello World!')

# 游戏主循环
while True:  # main game loop
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 将屏幕的背景填充成白色，了解下RGB三原色
    SCREEN.fill((255, 255, 255))
    # 调用 pygame.display.update() 方法更新整个屏幕的显示
    pygame.draw.rect(SCREEN, (255, 0, 0), (20, 30, 100, 50))
    pygame.display.update()
