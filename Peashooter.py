import pygame

class Peashooter(pygame.sprite.Sprite):
    def __init__(self):
        super(Peashooter,self).__init__()
        self.image = pygame.image.load('material/images/Peashooter_00.png').convert_alpha()
        self.images = [pygame.image.load('material/images/Peashooter_{:02d}.png'.format(i)).convert_alpha() for i in range(0,13)]

        self.rect = self.images[0].get_rect()
        # 有些位置无法放置种子，比如图里面的房子部分，所以要人为规定一下那个位置
        self.rect.top = 100
        self.rect.left = 250
        self.energy = 3*15
        # set   是一个不允许内容重复的组合，而且set里的内容位置是随意的，所以不能用索引列出。
        # 可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
        self.zombies = set()

    def update(self, *args):
        # 如果僵尸死了则跳过循环
        for zombie in self.zombies:
            # 僵尸是否活着，默认是活着的
            if zombie.isAlive == False:
                continue

            self.energy -= 1

        if self.energy <= 0:
            for zombie in self.zombies:
                #  僵尸是否遇到了坚果，没遇到就是遇到了射手，直接吃掉
                zombie.isMeetWallNut = False
            self.kill()
        # 随时更新图片，args【0】提取图片位置
        self.image = self.images[args[0] % len(self.images)]
