#Space Invaders Multiplayer
#By Ahnaf, Wasif, Eram and Luka
############################
#Import Modules 
from __future__ import division
import random, pygame, math
from os import path
############################
# sound and imgages folder
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sfx')
###############################
WIDTH = 1080 #set screen width
HEIGHT = 500 #set screen height 
FPS = 60 #set frame per second
##############################
# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################
## initialize pygame and create window
pygame.init() 
pygame.mixer.init() # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock() # For syncing the FPS
###############################
font_name = pygame.font.match_font('arial') #set width
###############################
def main_menu(): #main menu class only displays the get ready text
    global screen #set screen global
    
    while True: #fill screen and render text
        screen.fill(BLACK)
        draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
        pygame.display.update()
        break #break and start main loop
################################
def draw_text(surf, text, size, x, y): 
    # selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) # True denotes the font to be anti-aliased 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
###############################
def draw_lives(surf, x, y, lives, img): #Draw player 1 lives
    for i in range(lives): #draws sprite according to how many lives there are
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
###############################
def draw_lives2(surf, x, y, lives, img): #Draw player 2 lives
    for i in range(lives): #draws sprite according to how many lives there are 
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
##############################
def newmob(): #spawn a new enemy
    mob_element = Mob() #set mob_element 
    all_sprites.add(mob_element) #add to all_sprites
    mobs.add(mob_element) #spawn the enemy
##############################
class Player(pygame.sprite.Sprite): #player 1 class
    def __init__(self): #initialize varibles
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 60)) #scale the player img down
        self.image.set_colorkey(BLACK) #set colorkey 
        self.rect = self.image.get_rect() #set the rectangle collider 
        self.radius = 20 #radius of collider
        self.rect.centerx = WIDTH / 2 #placement of sprite on the x-axis(half the width of the screen)
        self.rect.bottom = HEIGHT - 10 #placement of the sprite on the y-axis
        self.speedx = 0 #define speedx
        self.speedy = 0 #define speedy
        self.shoot_delay = 250 #delay on shooting 
        self.last_shot = pygame.time.get_ticks() #count time between shots
        self.lives = 3 #define lives
        
    def update(self):

        if self.lives == 3: #set the sprite according to how many lives remain 
            self.image = pygame.transform.scale(player_img, (50, 60))
        if self.lives == 2:
            self.image = pygame.transform.scale(player_dmg1, (50, 60))
        if self.lives == 1:
            self.image = pygame.transform.scale(player_dmg2, (50, 60))
            
        self.speedx = 0 #makes the player static in the screen by default.
        self.speedy = 0  
        # then we have to check whether there is an event hanlding being done for the arrow keys being pressed 

        # will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()     
        if keystate[pygame.K_LEFT]: #left key
            self.speedx = -12 #move -12px on the x-axis per frame 
        elif keystate[pygame.K_RIGHT]: #right key
            self.speedx = 12 #move 12px on the x-axis per frame
        elif keystate[pygame.K_UP]: #up key 
            self.speedy = -12 #move -12px on the y-axis per frame
        elif keystate[pygame.K_DOWN]: #down key
            self.speedy = 12 #move 12px on the y-axis per frame

        #Fire weapons by holding or pressing delete
        if keystate[pygame.K_DELETE]:
            self.shoot() #call shoot function

        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
        ## check for the borders at the top and bottom
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 227:
            self.rect.top = 227

        self.rect.x += self.speedx #sets collider position to the direction of movement on the x-axis
        self.rect.y += self.speedy #sets collider position to the direction of movement on the y-axis

    def shoot(self): #shooting function
        now = pygame.time.get_ticks() #starts timing when function is called
        if now - self.last_shot > self.shoot_delay: #uses math to check if the delay is over
            self.last_shot = now #resets counter
            bullet = Bullet(self.rect.centerx, self.rect.top) #draws bullet and sets it on its course 
            all_sprites.add(bullet) #adds the bullet to all_sprites group 
            bullets.add(bullet) #adds the bullet to the bullet group
            shooting_sound.play() #plays shoot sound
#####################################
class Player2(pygame.sprite.Sprite): #player2 class
    def __init__(self): #initialize variables 
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.transform.scale(player2_img, (75, 75))  #scale the player img down
        self.image.set_colorkey(BLACK) #set colorkey 
        self.rect = self.image.get_rect() #set collider
        self.radius = 20 #set radius 
        self.rect.centerx = WIDTH / 2 #placement of sprite on the x-axis(half the width of the screen)
        self.rect.top = HEIGHT - 450 #placement of the sprite on the y-axis
        self.speedx = 0 #define speedx
        self.speedy = 0 #define speedy
        self.shoot_delay = 250 #delay between shots
        self.last_shot = pygame.time.get_ticks() #count time between shots
        self.lives = 3 #define lives

    def update(self):

        if self.lives == 3: #set the sprite according to how many lives remain 
            self.image = pygame.transform.scale(player2_img, (75, 75))
            self.image.set_colorkey(BLACK)
        if self.lives == 2:
            self.image = pygame.transform.scale(player2_dmg1, (75, 75))
            self.image.set_colorkey(BLACK)
        if self.lives == 1:
            self.image = pygame.transform.scale(player2_dmg2, (75, 75))
            self.image.set_colorkey(BLACK)
        
        self.speedx = 0     ## makes the player static in the screen by default.
        self.speedy = 0
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 

        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()     
        if keystate[pygame.K_a]: #a key
            self.speedx = -10 #move -10px on the x-axis per frame 
        elif keystate[pygame.K_d]: #d key
            self.speedx = 10 #move 10px on the x-axis per frame 
        elif keystate[pygame.K_w]: #w key
            self.speedy = -10 #move -10px on the y-axis per frame 
        elif keystate[pygame.K_s]: #s key
            self.speedy = 10 #move 10px on the y-axis per frame 

        #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot() #call shot function 

        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT / 2.2:
            self.rect.bottom = HEIGHT / 2.2
        if self.rect.top < 0:
            self.rect.top = 0

        self.rect.x += self.speedx #sets collider position to the direction of movement on the x-axis
        self.rect.y += self.speedy #sets collider position to the direction of movement on the y-axis

    def shoot(self): #shooting function
        now = pygame.time.get_ticks() #starts timing when function is called
        if now - self.last_shot > self.shoot_delay: #uses math to check if the delay is over
            self.last_shot = now #resets counter
            bullet = Bullet2(self.rect.centerx, self.rect.bottom) #draws bullet and sets it on its course 
            all_sprites.add(bullet) #adds the bullet to all_sprites group
            bullets2.add(bullet) #adds the bullet to the bullet group
            shooting_sound.play() #plays shoot sound
##################################
class Buddy(pygame.sprite.Sprite): #Buddy Class
    def __init__(self): #initialize varibles
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (30, 40)) #scale the buddy img down
        self.image.set_colorkey(BLACK) #set colorkey 
        self.rect = self.image.get_rect() #set collider
        self.radius = 20 #set radius
        self.rect.centerx = WIDTH / 2 #placement of sprite on the x-axis(half the width of the screen)
        self.rect.bottom = HEIGHT - 60 #placement of the sprite on the y-axis
        self.speedx = 0 #define speedx
        self.speedy = 0 #define speedy
        self.shoot_delay = 250 #delay between shots
        self.last_shot = pygame.time.get_ticks() #count time between shots
        self.step = 0 #define step
        self.threshold = random.randrange(5,11) #threshold equals a random range
        self.lives = 2 #define lives
                
    def update(self):
        if self.step >= self.threshold: #random movement and shooting is set through these if statements 
            self.dir = random.randint(1,8)
            if self.dir == 1: 
                self.shoot()
            if self.dir == 2: 
                self.rect.x-=40;

            if self.dir == 3: 
                self.rect.x-=40;

            if self.dir == 4: 
                self.rect.x+=40;

            if self.dir == 5: 
                self.shoot()

            if self.dir == 6: 
                self.rect.x-=40;

            if self.dir == 7: 
                self.rect.x+=40;

            if self.dir == 8: 
                self.rect.x+=40;

            self.threshold = random.randrange(5,11)
            self.step = 0
        self.step += 1
        
        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        
    def shoot(self): #shooting function
        now = pygame.time.get_ticks() #starts timing when function is called
        if now - self.last_shot > self.shoot_delay: #uses math to check if the delay is over
            self.last_shot = now #resets counter
            bullet = Bullet(self.rect.centerx, self.rect.top) #draws bullet and sets it on its course 
            all_sprites.add(bullet) #adds the bullet to all_sprites group 
            bullets.add(bullet) #adds the bullet to the bullet group
            shooting_sound.play() #plays shoot sound
#########################################
class Mob(pygame.sprite.Sprite): #mob class
    def __init__(self): #initialize varibles
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(alien_images) #set sprite from a random image in a list
        self.image_orig.set_colorkey(BLACK) #set colorkey
        self.image = self.image_orig.copy() #set sprite as copy
        self.rect = self.image.get_rect() #set collider
        self.radius = int(self.rect.width *.90 / 2) #set radius
        self.rect.x = random.randrange(0, WIDTH - self.rect.width) #placement of sprite on the x-axis (randomized)
        self.rect.y = HEIGHT / 3 #placement of the sprite on the y-axis is height divided by 3
        self.speedy = random.randrange(-1, 1) #for randomizing the speed of the Mob
        self.lives = 2 #define lives
        self.speedx = random.randrange(-4, -1) #for randomizing the speed of the Mob

        self.rotation = 0 #define rotation
        self.rotation_speed = random.randrange(-8, 8) #randamize rotation speed
        self.last_update = pygame.time.get_ticks() #time when the rotation has to happen
        
    def rotate(self):
        time_now = pygame.time.get_ticks() #time is a timer
        if time_now - self.last_update > 50: #in milliseconds
            self.last_update = time_now #reset the clock
            self.rotation = (self.rotation + self.rotation_speed) % 360 #rotate 
            new_image = pygame.transform.rotate(self.image_orig, self.rotation) #apply the rotation to the sprite
            old_center = self.rect.center #the next redefine the center and collider of the sprite
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
                
    def update(self):
        self.rect.x += self.speedx #set rect.x
        self.rotate() #call rotate function

        if(self.rect.left < -25) or (self.rect.right > WIDTH + 20): #if the sprite travels of screen set the x and y to make the sprite come back from top of screen
            self.rect.x = random.randrange(935, WIDTH - self.rect.width)
    
        hits = pygame.sprite.spritecollide(self, bullets, 1) #collision with bullets
        for hit in hits:
            self.lives -= 1 #lose a life
            self.image_orig = random.choice(hitalien_images) #set sprite to new one
            self.image_orig.set_colorkey(BLACK) #set colorkey
            enemy_hit_sound.play() #play sound

        if self.lives <= 0: #when lives are equal to 0 kill it
            self.kill()
            enemy_hit_sound.play()
########################################
class Bullet(pygame.sprite.Sprite): #Bullet Class
    def __init__(self, x, y): #initialize variables
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img #set sprite
        self.image.set_colorkey(BLACK) #set colorkey
        self.rect = self.image.get_rect() #set collider
        ## place the bullet according to the current position of the player
        self.rect.bottom = y 
        self.rect.centerx = x 
        self.speedy = -10 #set speed

    def update(self):
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()
#################################################
class Bullet2(pygame.sprite.Sprite): #Bullet2 Class
    def __init__(self, x, y): #initialize variables
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet2_img #set sprite
        self.image.set_colorkey(BLACK) #set colorkey
        self.rect = self.image.get_rect() #set collider
        ## place the bullet according to the current position of the player
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = +10 #set speed

    def update(self):
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()
###################################################
# Load all game images
background = pygame.image.load(path.join(img_dir, 'space background.gif'))
background_rect = background.get_rect()
background2 = pygame.image.load(path.join(img_dir, 'humanwin.gif'))
background2_rect = background2.get_rect()
background3 = pygame.image.load(path.join(img_dir, 'losinggame.gif'))
background3_rect = background3.get_rect()

alien_images = []
alien_list = [
    "Darkbluealien.png", "PinkAlien.png", "OrangeAlien.png", "LightYellowAlien.png", "LightRedAlien.png", "LightPurpleAlien.png", "LightPinkAlien.png", "LightGreyAliens.png", "LightBrownAlien.png", "LightBlueAlien.png", "GreyAlien.png", "Greenalien.png", "DarkPurpleAlien.png", "DarkOrangeAlien.png", "DarkBrownAlien.png", "DarkGreyAlien.png", "DarkRedAlien.png", "LightGreenAlien.png", "DarkYellowAlien.png"
]

for image in alien_list:
    alien_images.append(pygame.image.load(path.join(img_dir, image)).convert())

hitalien_images = []
hitalien_list = [
    "aliensded1.png", "aliensded3.png", "aliensded4.png", "aliensded5.png", "aliensded6.png", "aliensded7.png", "aliensded9.png" 
]

for image in hitalien_list:
    hitalien_images.append(pygame.image.load(path.join(img_dir, image)).convert())

player_img = pygame.image.load(path.join(img_dir, 'ship2.png')).convert()
player_dmg1 = pygame.image.load(path.join(img_dir, 'ship5.png')).convert()
player_dmg2 = pygame.image.load(path.join(img_dir, 'ship6.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
player2_img = pygame.image.load(path.join(img_dir, 'spaceship.png')).convert()
player2_dmg1 = pygame.image.load(path.join(img_dir, 'spaceship2.png')).convert()
player2_dmg2 = pygame.image.load(path.join(img_dir, 'spaceship3.png')).convert()
player2_mini_img = pygame.transform.scale(player2_img, (30, 30))
player2_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'gunshot.png'))
bullet2_img = pygame.image.load(path.join(img_dir, 'lazer.png'))
###################################################
# Load all game sounds
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'lazer1.wav'))
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'fire2.wav'))
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
pygame.mixer.music.set_volume(0.2)      # simmered the sound down a little

player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'hit2.wav'))
enemy_hit_sound = pygame.mixer.Sound(path.join(sound_folder, 'hitalien.wav'))
###################################################
# group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
player2 = Player2()
all_sprites.add(player2)
buddy = Buddy()
all_sprites.add(buddy)

# spawn a group of enemies 
mobs = pygame.sprite.Group()
for i in range(10): #10 enemies 
    newmob()

# group for bullets
bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
#############################
# Game loop
running = True
menu_display = True
while running:
    if menu_display:
        main_menu()
        pygame.time.wait(1500)

        #Stop menu music
        pygame.mixer.music.stop()
        #Play the gameplay music
        pygame.mixer.music.load(path.join(sound_folder, 'Resistance - Galactic.mp3'))
        pygame.mixer.music.play(-1) # makes the gameplay sound in an endless loop
        
        menu_display = False
        
    # Process input/events
    clock.tick(FPS) # will make the loop run at the same speed all the time
    for event in pygame.event.get(): #gets all the events which have occured till now and keeps tab of them.
        # listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        #Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    #Update
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, bullets2, True, pygame.sprite.collide_circle) #checks for collisions between player1 and player2 bullets 
    for hit in hits: #when hit play sounnd and subtract a life
        player_die_sound.play()
        player.lives -= 1
   
    hits = pygame.sprite.spritecollide(player2, bullets, True, pygame.sprite.collide_circle) #checks for collisions between player2 and player1/buddy bullets 
    for hit in hits: #when hit play sounnd and subtract a life
        player_die_sound.play()
        player2.lives -= 1

    hits = pygame.sprite.spritecollide(buddy, bullets2, True, pygame.sprite.collide_circle) #checks for collisions between buddy and player2 bullets 
    for hit in hits: #when hit play sounnd and subtract a life
        player_die_sound.play()
        buddy.lives -= 1
        if buddy.lives == 0: #when buddy has no health kill him and         dispose of corpse outside of playable game 
            buddy.kill()
            buddy.rect.centerx = WIDTH + 100
            buddy.rect.top = HEIGHT - 1150
            
    # if a player has died end the game 
    if player.lives == 0:
        pygame.time.wait(200)
        running = False
    elif player2.lives == 0:
        pygame.time.wait(200)
        running = False

    #Draw/render
    screen.fill(BLACK)
    #draw the background
    screen.blit(background, background_rect)

    all_sprites.draw(screen)
    # Draw lives
    draw_lives(screen, WIDTH - 100, 5, player2.lives, player2_mini_img)
    draw_lives(screen, WIDTH - 1080, 480, player.lives, player_mini_img)

    #Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit() #quit game
