import time

import pygame
# import os

from Bullet import Bullet
from FlagZombie import FlagZombie
from Peashooter import Peashooter
from SunFlower import SunFlower
from WallNut import WallNut
from Sun import Sun
from Zombie import Zombie

pygame.init()
# 1200长正好卡在那个草坪末端
backgd_size = (1200, 600)

screen = pygame.display.set_mode(backgd_size)
pygame.display.set_caption('plant_vs_zoomie')
#初始化音乐模块
pygame.mixer.init()
#加载音乐
pygame.mixer.music.load("material/music/02 - Crazy Dave (Intro Theme).mp3")
# 必须加上play函数
pygame.mixer.music.play()

bg_img_path = 'material/images/background1.jpg'
bg_img_obj = pygame.image.load(bg_img_path).convert_alpha()

sunFlowerImg = pygame.image.load('material/images/SunFlower_00.png').convert_alpha()
wallnutImg = pygame.image.load('material/images/WallNut_00.png').convert_alpha()
peashooterImg = pygame.image.load('material/images/Peashooter_00.png').convert_alpha()
# sunbank_img_path = 'material/images/SunBack.png'
# sunbank_img_obj = pygame.image.load(sunbank_img_path).convert_alpha()

sunbackImg = pygame.image.load('material/images/SeedBank.png').convert_alpha()
flower_seed = pygame.image.load("material/images/TwinSunflower.gif")
wallNut_seed = pygame.image.load("material/images/WallNut.gif")
peashooter_seed = pygame.image.load("material/images/Peashooter.gif")

# 字体渲染
text = '1000'
sun_font = pygame.font.SysFont('arial',20)
# pygame.font.SysFont()  ——  从系统字体库创建一个 Font 对象
# Arial是一套随同多套微软应用软件所分发的无衬线体TrueType字型
# SysFont(name, size, bold=False, italic=False) -> Font
sun_num_surface = sun_font.render(text,True,(0,0,0))

# peashooter = Peashooter()
# sunflower = SunFlower()
# wallnut = WallNut()
# zombie = Zombie()

# spriteGroup = pygame.sprite.Group()
# spriteGroup.add(peashooter)
# spriteGroup.add(sunflower)
# spriteGroup.add(wallnut)
# spriteGroup.add(zombie)
bulletGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()
wallNutGroup = pygame.sprite.Group()
peaShooterGroup = pygame.sprite.Group()
sunFlowerGroup = pygame.sprite.Group()

sunList = pygame.sprite.Group()

# sunList = []

clock = pygame.time.Clock()

GEN_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GEN_SUN_EVENT,1000)
# 将事件类型设置为每隔给定的毫秒数显示在事件队列中。第一个事件将在经过一段时间后才会出现。
GEN_BULLET_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GEN_BULLET_EVENT,1000)

GEN_ZOMBIE_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GEN_ZOMBIE_EVENT,8000)

GEN_FLAGZOMBIE_EVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GEN_FLAGZOMBIE_EVENT,20000)


choose = 0
def main():
    global text,choose
    global sun_num_surface
    running = True
    # index必须初始化为0，否则第一张图片进不去屏幕
    index = 0
    while running:
        # if index >= 130:
        #     index = 0

        clock.tick(20)
        # if not pygame.mixer.music.get_busy():
        #     pygame.mixer.music.play()
        #2s产生一个太阳花
        # if index % 40 == 0:
        #     sun = Sun(sunflower.rect)
        #     sunList.add(sun)

        #3s产生一个子弹
        # if index % 30 == 0:
        #     for sprite in spriteGroup:
        #         if isinstance(sprite, Peashooter):
        #             bullet = Bullet(sprite.rect, backgd_size)
        #             spriteGroup.add(bullet)

        for bullet in bulletGroup:
            for zombie in zombieGroup:
                # 直接使用下列函数实现碰撞检测，
                # 这个函数接收两个精灵作为参数，返回值是一个bool变量。
                if pygame.sprite.collide_mask(bullet,zombie):
                    zombie.energy -= 1
                    bulletGroup.remove(bullet)

        for wallNut in wallNutGroup:
            # 只要僵尸与植物接触就是zombie.isMeetWallNut = True
            # 接触之后将其放入精灵建立的set函数产生的无序列表中
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(wallNut, zombie):
                    zombie.isMeetWallNut = True
                    wallNut.zombies.add(zombie)

        for peaShooter in peaShooterGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(peaShooter, zombie):
                    zombie.isMeetWallNut = True
                    peaShooter.zombies.add(zombie)

        for sunFlower in sunFlowerGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(sunFlower, zombie):
                    zombie.isMeetWallNut = True
                    sunFlower.zombies.add(zombie)

        # 图片绘制
        screen.blit(bg_img_obj,(0,0))
        screen.blit(sunbackImg,(250,0))
        # 这个是放植物的框图
        screen.blit(sun_num_surface,(270,60))
        # 绘制种子图片在框框里面
        screen.blit(flower_seed, (330, 10))
        screen.blit(wallNut_seed, (380, 10))
        screen.blit(peashooter_seed, (430, 10))


        # spriteGroup.update(index)
        # spriteGroup.draw(screen)
        bulletGroup.update(index)
        bulletGroup.draw(screen)
        zombieGroup.update(index)
        zombieGroup.draw(screen)


        wallNutGroup.update(index)
        wallNutGroup.draw(screen)
        peaShooterGroup.update(index)
        peaShooterGroup.draw(screen)

        sunFlowerGroup.update(index)
        sunFlowerGroup.draw(screen)

        sunList.update(index)
        sunList.draw(screen)
        # 确定鼠标点击的横纵坐标
        (x,y) = pygame.mouse.get_pos()

        # if choose == 1:
        #     screen.blit(sunFlowerImg,(x,y))
        # elif choose == 2:
        #     screen.blit(wallnutImg, (x, y))
        # elif choose == 3:
        #     screen.blit(peashooterImg, (x, y))


        # 确定好三种植物后绘制图像位置，一般都在鼠标点击点在图片的正中心
        if choose == 1:
            screen.blit(sunFlowerImg, (x - sunFlowerImg.get_rect().width // 2, y - sunFlowerImg.get_rect().height // 2))
        if choose == 2:
            screen.blit(wallnutImg, (x - wallnutImg.get_rect().width // 2, y - wallnutImg.get_rect().height // 2))
        if choose == 3:
            screen.blit(peashooterImg,
                        (x - peashooterImg.get_rect().width // 2, y - peashooterImg.get_rect().height // 2))
        # index控制确定的次数和机会，点了一次，index加一对应刷新一次屏幕
        index+=1




        # 精灵调用以及添加精灵组
        for event in pygame.event.get():
            if event.type == GEN_FLAGZOMBIE_EVENT:
                zombie = FlagZombie()
                zombieGroup.add(zombie)

            if event.type == GEN_ZOMBIE_EVENT:
                zombie = Zombie()
                zombieGroup.add(zombie)

            if event.type == GEN_SUN_EVENT:
                for sprite in sunFlowerGroup:
                    # 返回当前时间的时间戳，控制太阳出现的时间
                    now = time.time()
                    if now - sprite.lasttime >= 5:
                        sun = Sun(sprite.rect)
                        sunList.add(sun)
                        sprite.lasttime = now

            if event.type == GEN_BULLET_EVENT:
                for sprite in peaShooterGroup:
                    bullet = Bullet(sprite.rect, backgd_size)
                    bulletGroup.add(bullet)

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_key = pygame.mouse.get_pressed()
                print(pressed_key)
                if pressed_key[0] == 1:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    x,y = pos
                    if 330<=x<=380 and 10<=y<=80 and int(text) >= 50:
                        print('点中了太阳花卡片')
                        choose = 1
                    elif 380<x<=430 and 10<=y<=80 and int(text) >= 50:
                        print('点中了坚果卡片')
                        choose = 2
                    elif 430 < x <= 480 and 10 <= y <= 80 and int(text) >= 100:
                        print('点中了豌豆射手卡片')
                        choose = 3
                    elif 250 < x < 1200 and 70<y<600:
                        #种植植物
                        if choose == 1:
                            current_time = time.time()
                            sunFlower = SunFlower(current_time)
                            sunFlower.rect.top = y
                            sunFlower.rect.left = x
                            sunFlowerGroup.add(sunFlower)
                            choose = 0

                            #扣除分数
                            text = int(text)
                            text -= 50
                            myfont = pygame.font.SysFont('arial',20)
                            sun_num_surface = myfont.render(str(text),True,(0,0,0))
                        elif choose == 2:
                            wallNut = WallNut()
                            wallNut.rect.top = y
                            wallNut.rect.left = x
                            wallNutGroup.add(wallNut)
                            choose = 0

                            # 扣除分数
                            text = int(text)
                            text -= 50
                            myfont = pygame.font.SysFont('arial', 20)
                            sun_num_surface = myfont.render(str(text), True, (0, 0, 0))
                        elif choose == 3:
                            peashooter = Peashooter()
                            peashooter.rect.top = y
                            peashooter.rect.left = x
                            peaShooterGroup.add(peashooter)
                            choose = 0

                            # 扣除分数
                            text = int(text)
                            text -= 50
                            myfont = pygame.font.SysFont('arial', 20)
                            sun_num_surface = myfont.render(str(text), True, (0, 0, 0))

                        print('#########')
                        print(x,y)
                        pass
                    else:
                        pass
                    for sun in sunList:
                        if sun.rect.collidepoint(pos):
                            sunList.remove(sun)
                            text = str(int(text)+50)
                            # 分数变化后循环渲染字体
                            sun_font = pygame.font.SysFont('arial', 20)
                            sun_num_surface = sun_font.render(text, True, (0, 0, 0))

        pygame.display.update()

if __name__ == '__main__':
    main()
