from pygame import *
mixer.init()
window = display.set_mode((1000, 600))
display.set_caption('Некая хрень')
background = transform.scale(image.load('background.jpg'), (1000, 600))

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_speed, p_box, p_x, p_y):
        super().__init__()
        self.c_image = crap11 = transform.scale(image.load(p_image), p_box)
        self.c_speed = p_speed
        self.c_hit = self.c_image.get_rect()
        self.c_x = p_x
        self.c_y = p_y

    def hello(self):
        window.blit(self.c_image, (self.c_x, self.c_y)) 
    
class Model1(GameSprite):
    def update1(self):
        button = key.get_pressed()
        if button[K_UP] and self.c_y >= 30:
            self.c_y -= self.c_speed
        if button[K_DOWN] and self.c_y <= 500:
            self.c_y += self.c_speed
    def update2(self):
        button = key.get_pressed()
        if button[K_w] and self.c_y >= 30:
            self.c_y -= self.c_speed
        if button[K_s] and self.c_y <= 500:
            self.c_y += self.c_speed

# class Model2(GameSprite):
#     leeft = False
#     def flight(self):
#         if crap21.colliderect(crap12):
#             leeft = True
#         while leeft = False:
#             self.c_x += self.c_speed()
        

        

game = True

kreml = time.Clock()
FPS = 60

crap11 = Model1('hero.png', 20, (20, 170), 980, 250)
crap12 = Model1('hero.png', 20, (20, 170), 10, 250)
# crap21 = model2('cyborg.png', 40, (20, 20), 500, 250)
while game:
    window.blit(background, (0, 0))
    crap11.update1()
    crap11.hello()
    crap12.update2()
    crap12.hello()
    # crap21.flight()
    # crap21.hello()
    kreml.tick(FPS)
    for e in event.get():
            if e.type == QUIT:
                game = False
    display.update()