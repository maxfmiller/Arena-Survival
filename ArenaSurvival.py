import pygame 
import sys
import time


'''
Variables
'''

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

speed = 2
TITLE = 'Arena Survival'
FramePerSec = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480
ACC = 0.75
FRIC = -0.12
FPS = 60
global displaysurface
global running
mouse = pygame.mouse.get_pos()

'''
Player
'''


class Player(pygame.sprite.Sprite):

    def __init__(self):
        #inherits Sprite attributes from pygame parent class
        super().__init__() 
        #initialize attributes to represent the player
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect()
        
        self.pos = vec((100, 300))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
    def move(self):
        #player movement including directions, user control, and friction.
        self.acc = vec(0, 0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACC  
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc    
        
        #prevents player from moving off screen
        if self.pos.x >= WIDTH:
            self.pos.x = WIDTH - 1
        if self.pos.x <= 0:
            self.pos.x = 1
        if self.pos.y >= HEIGHT:
            self.pos.y = HEIGHT - 1
            
        self.rect.midbottom = self.pos
    
    def update(self):
        #collision between platforms and player
        hits = pygame.sprite.spritecollide(P1 , platforms, False)
        
        if P1.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
        
        if P1.vel.y < 0: 
            if hits:                
                    self.pos.y = hits[0].rect.bottom +30
                    self.vel.y = 0
                    self.jumping = False
    
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:    
            self.vel.y = -13            
 
 
'''
Enemy Sprites
'''
   
           
class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((30, 30))
            self.surf.fill((252, 3, 3))
            self.rect = self.surf.get_rect(center = (50, 100))
            
            self.pos = vec((100, 300))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.path = None    
    
    def movement(self,):
        #find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(P1.rect.x - self.rect.x,
                                      P1.rect.y - self.rect.y)
        dirvect.normalize()
        #move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(speed)
        self.rect.move_ip(dirvect)

    def damage(self):
        #if player collides with enemy, game ends
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            time.sleep(0.2)
            gameover()
    
            
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((30, 30))
            self.surf.fill((252, 3, 3))
            self.rect = self.surf.get_rect(center = (550, 100))
            
            self.pos = vec((100, 300))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.path = None    
    
    def movement(self):
        dirvect = pygame.math.Vector2(P1.rect.x - 30 - self.rect.x,
                                      P1.rect.y - 30 - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(speed)
        self.rect.move_ip(dirvect) 
     
    def damage(self):
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            time.sleep(0.2)
            gameover()


class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((30, 30))
            self.surf.fill((252, 3, 3))
            self.rect = self.surf.get_rect(center = (550, 200))
           
            self.pos = vec((100, 300))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.path = None    
    
    def movement(self):
        dirvect = pygame.math.Vector2(P1.rect.x + 30 - self.rect.x,
                                      P1.rect.y + 30 - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(speed)
        self.rect.move_ip(dirvect) 
   
    def damage(self):
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            time.sleep(0.2)
            gameover()    


class Trap1(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((30, 30))
            self.surf.fill((252, 3, 3))
            self.rect = self.surf.get_rect(center = (185, 350))
           
            self.pos = vec((100, 300))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.path = None    
            
    def damage(self):
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            time.sleep(0.2)
            gameover()    


class Trap2(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((30, 30))
            self.surf.fill((252, 3, 3))
            self.rect = self.surf.get_rect(center = (470, 150))
            
            self.pos = vec((100, 300))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.path = None    
            
    def damage(self):
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            time.sleep(0.2)
            gameover()  


class Trap3(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((30, 30))
            self.surf.fill((252,3,3))
            self.rect = self.surf.get_rect(center = (320, 250))
           
            self.pos = vec((100, 300))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.path = None    
            
    def damage(self):
        hits = pygame.sprite.spritecollide(self, player, False)
        if hits:
            time.sleep(0.2)
            gameover()  


'''
Platforms
'''   


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((37, 64, 36))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))


class Platform2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill((55, 55, 55))
        self.rect = self.surf.get_rect(center = (220, 350))    


class Platform3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill((55, 55, 55))
        self.rect = self.surf.get_rect(center = (320, 250)) 


class Platform4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill((55, 55, 55))
        self.rect = self.surf.get_rect(center = (470, 150))   


class Platform5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill((55, 55, 55))
        self.rect = self.surf.get_rect(center = (420, 350))    


class Platform6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill((55, 55, 55))
        self.rect = self.surf.get_rect(center = (170, 150))   


'''
Score
'''


class Score(object):
    def __init__(self):
        self.count = 0
        self.font = pygame.font.SysFont("GurmukhiMN", 20, True, False)
        self.text = self.font.render("Score: "+str(self.count), True, 1, 'WHITE')

    def show_score(self, screen):
        screen.blit(self.text, (10 , 10))

    def score_up(self):
        #increases score once per tick
        self.count += 1
        self.text = self.font.render("Score: "+str(self.count), True, 1, 'WHITE')


'''
Sprite Groupings
'''

PT1 = Ground()
PT2 = Platform2()
PT3 = Platform3()
PT4 = Platform4()
PT5 = Platform5()
PT6 = Platform6()
P1 = Player() 
E1 = Enemy1()
E2 = Enemy2()
E3 = Enemy3()
T1 = Trap1()
T2 = Trap2()
T3 = Trap3()

player = pygame.sprite.Group()
player.add(P1)

Scorevar = Score()

platforms = pygame.sprite.Group()
platforms.add(PT1)
platforms.add(PT2)
platforms.add(PT3)
platforms.add(PT4)
platforms.add(PT5)
platforms.add(PT6)

enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
enemies.add(E3)
enemies.add(T1)
enemies.add(T2)
enemies.add(T3)

'''
Game Loop
'''

# define a main function
def main():    
    # initialize the pygame module
    pygame.init()
    
    # creating the surface 
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    smallfont = pygame.font.SysFont('GurmukhiMN', 30)
    # define a variable to control the main loop
    running = True

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(PT1)
    all_sprites.add(PT2)
    all_sprites.add(PT3)
    all_sprites.add(PT4)
    all_sprites.add(PT5)
    all_sprites.add(PT6)
    
    # main loop
    while running:
        
        #draws sprite on display
        displaysurface.fill((81, 177, 222))
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
        
        Scorevar.show_score(displaysurface)
        Scorevar.score_up()
     
     #spawns enemies sprites   
        if Scorevar.count > 150:
            all_sprites.add(E1)
            E1.movement()
            E1.damage()
        
        if Scorevar.count > 500:
            all_sprites.add(T1)
            T1.damage()
                
        if Scorevar.count > 750:
            all_sprites.add(E2)
            E2.movement()     
            E2.damage()
            
        if Scorevar.count > 1000:
            all_sprites.add(T2)
            T2.damage()
            
        if Scorevar.count > 1250:
            all_sprites.add(E3)
            E3.movement()
            E3.damage()
         
        if Scorevar.count > 1500:
            all_sprites.add(T3)
            T3.damage()  
        
        #enables player functions
        P1.move()
        P1.update()
        
        
        pygame.display.update()
        FramePerSec.tick(FPS)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # assign keys for state change
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                P1.jump()

'''
Menu Screen
'''

def menu():
    # initialize the pygame module
    pygame.init()
    
    # creating the surface 
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    titlefont = pygame.font.SysFont('GurmukhiMN', 56)
    smallfont = pygame.font.SysFont('GurmukhiMN', 30)
    titletext = titlefont.render('Arena Survival', True, 'WHITE')
    begintext = smallfont.render('PRESS P TO BEGIN!', True, 'WHITE')
    # define a variable to control the main loop
    running = True    
    
    while running:
        
        #draws sprite on display
        displaysurface.fill((0,0,0))
        displaysurface.blit(titletext, (140, 60))
        displaysurface.blit(begintext, (190, 300))
        pygame.display.update()
        FramePerSec.tick(FPS)
        
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # assign keys for state change
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key != pygame.K_q and event.key == pygame.K_p:
                objective()     

'''
Objective Screen
'''

def objective():
    
    pygame.init()
    
    #surface 
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    titlefont = pygame.font.SysFont('GurmukhiMN', 56)
    smallfont = pygame.font.SysFont('GurmukhiMN', 22)
    titletext = titlefont.render('YOUR OBJECTIVE', True, 'WHITE')
    smalltext1 = smallfont.render('Survive as long as possible in the arena!', True, 'WHITE')
    smalltext2 = smallfont.render('Avoid the RED enemies and traps as they appear!', True, 'WHITE')
    smalltext3 = smallfont.render('You can press Q to quit at any time', True, 'WHITE')
    smalltext4 = smallfont.render('Use the arrow keys to move your player around', True, 'WHITE')
    smalltext5 = smallfont.render('Press P to Continue', True, 'WHITE')
  
    running = True    
    
    while running:
        
        #draws sprite on display
        displaysurface.fill((0,0,0))
        displaysurface.blit(titletext, (60, 60))
        displaysurface.blit(smalltext3, (60, 200))
        displaysurface.blit(smalltext2, (60, 250))
        displaysurface.blit(smalltext1, (60, 300))
        displaysurface.blit(smalltext4, (60, 150))
        displaysurface.blit(smalltext5, (190, 400))
        pygame.display.update()
        FramePerSec.tick(FPS)
        
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key != pygame.K_q and event.key == pygame.K_p:
                main()     

'''
Game Over Screen
'''

def gameover():
    pygame.init()
    
    #surface 
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    titlefont = pygame.font.SysFont('GurmukhiMN', 56)
    smallfont = pygame.font.SysFont('GurmukhiMN', 26)
    smallfont2 = pygame.font.SysFont('GurmukhiMN', 32)
    titletext = titlefont.render('GAME OVER', True, 'WHITE')
    smalltext1 = smallfont.render(str(Scorevar.count), True, 'WHITE')
    smalltext2 = smallfont2.render('Your Final Score:', True, 'WHITE')
    smalltext3 = smallfont.render('Thanks for Playing!', True, 'WHITE')
    smalltext4 = smallfont.render('Press Q to quit', True, 'WHITE')

    running = True    
    
    while running:
        
        #draws sprite on display
        displaysurface.fill((0,0,0))
        displaysurface.blit(titletext, (160, 60))
        displaysurface.blit(smalltext3, (210, 160))
        displaysurface.blit(smalltext2, (200, 250))
        displaysurface.blit(smalltext1, (300, 300))
        displaysurface.blit(smalltext4, (230, 400))
        pygame.display.update()
        FramePerSec.tick(FPS)
        
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
                                  
# if you import this as a module then nothing is executed
if __name__=="__main__":
    menu()
