
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect,KEYDOWN,K_SPACE

def main():
    #初期化
    pygame.init()
    key_repeat_delay = 5
    key_repeat_interval = 5
    pygame.key.set_repeat(key_repeat_delay,key_repeat_interval)
    window_width = 800
    window_height = 600
    surface = pygame.display.set_mode((window_width ,window_height))
    fpsclock = pygame.time.Clock()

    wall = 80 #洞窟を構成する矩形の数
    slope = randint(1,6) #洞窟の傾き
    ship_y = 250 #自機のy座標
    velocity = 0 #自機が上下に移動する速度
    score = 0 #点数
    game_over = False # ゲームオーバーのフラグ
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("cave\\ship.png")
    bang_image = pygame.image.load("cave\\bang.png")

    holes = [] #洞窟を構成する矩形を格納する
    hole_x_width = 10
    hole_y_width = 400
    hole_y_position = 100
    for xpos in range(wall):
        holes.append(Rect(xpos * hole_x_width, hole_y_position, hole_x_width, hole_y_width))

    #メインループ
    while True:
         #ループ初期化
        is_space_down = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        # 時機移動
        if not game_over:
            score += 10
            vel = 1
            velocity += -vel if is_space_down else vel
            ship_y += velocity

            # 洞窟をスクロール
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= window_height: #作成した矩形が床か天井にヒット
                slope = randint(1,6) * (-1 if slope > 0 else 1) #作成した矩形が洞窟に収まるように傾きを調整
                edge.inflate_ip(0,-20) # Y軸方向のサイズを小さくする
            edge.move_ip(hole_x_width, slope)
            holes.append(edge)
            if holes:
               del holes[0]
            holes = [x.move(-hole_x_width, 0) for x in holes]

            # 衝突
            ship_top = ship_y
            ship_bottom = ship_y + 80
            if holes[0].top > ship_top or holes[0].bottom < ship_bottom:
                game_over = True

        # 描画
        back_color = (0,255,0)
        hole_color = (255,0,0)
        surface.fill(back_color)
        for hole in holes:
            pygame.draw.rect(surface, hole_color,hole)
        score_image = sysfont.render("score is {}".format(score),True, (0,0,255))
        score_position =(600,200)
        surface.blit(score_image, score_position )

        surface.blit(ship_image, (0, ship_y))
        if game_over:
            surface.blit(bang_image,(0, ship_y - 40))

        pygame.display.update()
        fpsclock.tick(15)

if __name__ == '__main__':
    main()
