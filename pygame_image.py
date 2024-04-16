import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習２
    kk_img = pg.transform.flip(kk_img, True, False)#練習２
    tbg_img = pg.transform.flip(bg_img, True, False)#練習７
    kk_img_rct = kk_img.get_rect()#練習８-1こうかとんrectを抽出
    kk_img_rct.center = 300, 200#こうかとんrectの指定
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        #print(key_lst) 
        if key_lst[pg.K_UP]:
            kk_img_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kk_img_rct.move_ip((0,1))
        if key_lst[pg.K_LEFT]:
            kk_img_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_img_rct.move_ip((1,0))

        x = tmr%3200#練習６（背景画像繰り返すための処理）
        screen.blit(bg_img, [-x, 0])
        screen.blit(tbg_img,[(-x+1600),0])#練習７
        screen.blit(bg_img, [(-x+3200),0])
        screen.blit(tbg_img,[(-x+4800),0])
        screen.blit(kk_img, kk_img_rct)
        #print(tmr,x)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()