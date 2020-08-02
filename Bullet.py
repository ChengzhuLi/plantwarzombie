import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, wdrect,bg_size):
        # python2 用法
        super(Bullet, self).__init__()
        # convert函数作用是将图片转化为Surface对象，pygame现在会自动这么做；
        # convert_alpha相对于convert，保留了图像的Alpha 通道信息，
        self.image = pygame.image.load('material/images/Bullet_1.png').convert_alpha()
        self.rect = self.image.get_rect()

        #定义子弹的初始化位置
        self.rect.left = wdrect[0] + 45
        self.rect.top = wdrect[1]
        self.width = bg_size[0]
        self.speed = 5

    def update(self, *args):
        # 它接收元组作为位置参数，而非是常见的参数列表。在这里，”args”是个元组
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.kill()
