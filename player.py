import pygame

WIDTH = 30
HEIGHT = 50
SPEED = 3
J_SPEED = 10
G = 0.5
P_WIDTH = 50
P_HEIGHT = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, serf, ms):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = (15, 570))
        self.ms = ms
        self.speed = SPEED
        self.jumpspeed = 0
        self.jump = False
        self.xv = 0
        self.yv = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.xv = -1
        if keys[pygame.K_d] and self.rect.x < 770:
            self.rect.x += self.speed
            self.xv = 1
        if keys[pygame.K_w]:
            if not self.jump:
                self.jump = True
                self.jumpspeed = -J_SPEED
        if self.jump:
            self.rect.y += self.jumpspeed
            self.jumpspeed += G
            if self.rect.y >= 550:
                self.rect.y = 550
                self.jump = False

    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.jump:
                    if self.jumpspeed < 0:
                        self.jumpspeed = 0
                        self.rect.top = p.rect.bottom
                    if self.jumpspeed > 0:
                        self.jump = False
                        self.rect.bottom = p.rect.top
                if self.rect.bottom > p.rect.top and self.rect.top < p.rect.bottom:
                    if self.xv > 0:
                        self.rect.right = p.rect.left
                    if self.xv < 0:
                        self.rect.left = p.rect.right


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((P_WIDTH, P_HEIGHT))
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect(x, y, P_WIDTH, P_HEIGHT)


