import pygame
# import Colors as c


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, img):
        self.sc_wd = screen_width
        self.sc_hd = screen_height
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 100))
        self.image = img
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (screen_width/4, screen_height)

    def update(self, height, width):
        self.rect.y -= height
        self.rect.x += width
        if self.rect.x > self.sc_wd:
            self.rect.x = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Block(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75, 25))
        self.rect = self.image.get_rect()
        self.rect.center = location

