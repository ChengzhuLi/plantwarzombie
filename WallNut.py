import pygame

class WallNut(pygame.sprite.Sprite):
    def __init__(self):
        super(WallNut, self).__init__()
        self.image = pygame.image.load('material/images/WallNut_00.png').convert_alpha()
        self.images = [pygame.image.load('material/images/WallNut_{:02d}.png'.format(i)).convert_alpha() for i in range(0,13)]
        self.crackedImgs = [
            pygame.transform.smoothscale(pygame.image.load("material/images/Wallnut_body.png").convert_alpha(),
                                         (self.image.get_rect().width, self.image.get_rect().height)),
            pygame.transform.smoothscale(
                pygame.image.load("material/images/Wallnut_cracked1.png").convert_alpha(),
                (self.image.get_rect().width, self.image.get_rect().height)),
            pygame.transform.smoothscale(
                pygame.image.load("material/images/Wallnut_cracked2.png").convert_alpha(),
                (self.image.get_rect().width, self.image.get_rect().height))]
        # 平滑地将曲面缩放到任意大小
        # smoothscale(Surface, (width, height), DestSurface = None) -> Surface
        # 使用两种不同算法中的一种来根据需要缩放输入surface的每个维度。
        # 对于收缩，输出像素是它们覆盖的颜色的面积平均值。
        # 对于扩展，使用双线性滤波器。
        # 对于x86-64和i686架构，包含优化的MMX程序，运行速度比其他机器类型快得多。
        # 大小是(width, height)的2个数字序列。 此函数仅适用于24位或32位surface。
        # 如果输入表面位深度小于24，则抛出异常。
        self.rect = self.images[0].get_rect()
        self.rect.top = 200
        self.rect.left = 250

        self.energy = 8*15
        self.zombies = set()

    def update(self, *args):
        for zombie in self.zombies:
            if zombie.isAlive == False:
                continue

            self.energy -= 1

        if self.energy <= 0:
            for zombie in self.zombies:
                zombie.isMeetWallNut = False
            self.kill()

        # 根据不同受损程度使用对应图片
        if self.energy == 8*15:
            self.image = self.images[args[0] % len(self.images)]
        elif 6*15 <= self.energy < 8*15:
            self.image = self.crackedImgs[0]
        elif 3 * 15 <= self.energy < 6 * 15:
            self.image = self.crackedImgs[1]
        else:
            self.image = self.crackedImgs[2]
