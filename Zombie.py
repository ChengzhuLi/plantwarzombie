import random

import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie,self).__init__()
        self.image = pygame.image.load('material/images/Zombie_0.png').convert_alpha()
        self.images = [pygame.image.load('material/images/Zombie_{}.png'.format(i)).convert_alpha() for i in range(0,22)]
        self.dieimages = [pygame.image.load('material/images/ZombieDie_{}.png'.format(i)).convert_alpha() for i in range(0,10)]
        self.attack_images = [pygame.image.load('material/images/ZombieAttack_{}.png'.format(i)).convert_alpha() for i in
                          range(0, 21)]
        self.rect = self.images[0].get_rect()
        self.rect.top = 25 + random.randrange(0,4)*125
        self.energy = 6
        self.rect.left = 1000
        self.speed = 5
        # dietimes不是击中次数，是一项新指标，控制死亡动画显示时间
        self.dietimes = 0
        # 初始化和其他的关系
        self.isMeetWallNut = False
        self.isAlive = True

    def update(self, *args):
        if self.energy > 0:
            # energy就是生命值
            if self.isMeetWallNut:
                # 如果遇到僵尸吃植物，进入袭击模式
                self.image = self.attack_images[args[0] % len(self.attack_images)]
            else:
                # 否则就是正常模式
                self.image = self.images[args[0] % len(self.images)]
            if self.rect.left > 250 and not self.isMeetWallNut:
                self.rect.left -= self.speed
        else:
            # 此时僵尸已经挂了，但要显示挂了的动画
            # 对应正好10张，所以dietimes显示为20为界限
            if self.dietimes < 20:
                self.image = self.dieimages[self.dietimes//2]
                self.dietimes += 1
            else:
                # 20次以后僵尸尸体保留一段时间，所以直接到30次是分界线
                if self.dietimes > 30:
                    self.isAlive = False
                    self.kill()
                else:
                    self.dietimes += 1
