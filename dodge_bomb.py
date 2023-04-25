import random as rd
import sys
import pygame as pg


idou ={
    pg.K_UP:(0,-1),
    pg.K_DOWN:(0,1),
    pg.K_LEFT:(-1,0),
    pg.K_RIGHT:(1,0)
       }


def bound_chk(scr_rct:pg.Rect,obj_rct:pg.Rect) :
    #オブジェクトが画面内外を判定して真理値を返す
    #引数1 画面Surfaceのrect
    #引数2 こうかとん,または爆弾SurfaceのRect
    #戻り値 横方向縦方向のはみだし判定結果
    yoko,tate=True,True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ProjExD2023/ex02-20230425/fig/pg_bg.jpg")
    kk_img = pg.image.load("ProjExD2023/ex02-20230425/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct=kk_img.get_rect()#こうかとんrect対応
    kk_rct.center=900,400#こうかとんセンターどり
    
    bb_img=pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)#円を書き込む
    bb_img.set_colorkey((0,0,0))#爆弾の四隅を透過
    dx,dy=+1,+1#爆弾の移動速度
    bb_x,bb_y=rd.randint(0,1600),rd.randint(0,900)#爆弾のx、yの位置をランダム化
    bb_rct=bb_img.get_rect()#爆弾rect対応
    bb_rct.center=bb_x,bb_y#爆弾センターどり

    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst=pg.key.get_pressed()#押されているキーを判定
        for k,mv in idou.items():
            if key_lst[k]:#押されているキーが[k]なら
                kk_rct.move_ip(mv)#こうかとんが動く方向を決定する
        if bound_chk(screen.get_rect(),kk_rct)!=(True,True): # type: ignore
            for k,mv in idou.items():
                if key_lst[k]:#押されているキーが[k]ならなら
                    kk_rct.move_ip(-mv[0],-mv[1])#こうかとんが動く方向を決定する
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)#こうかとんが動く
        bb_rct.move_ip(dx,dy)#円が動く
        screen.blit(bb_img, bb_rct)#円を描写させる

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()