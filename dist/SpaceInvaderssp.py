#Space Invaders Singleplayer
#By Ahnaf, Wasif, Eram and Luka
############################
#Import Modules 
from __future__ import division
import pygame
import random
from os import path
from Score_Module import highscore #import score module
############################################
## assets folder
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sfx')
###############################
#set screen size and fps
WIDTH = 1080 
HEIGHT = 500
FPS = 60
########################################
# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################
# initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()     ## For syncing the FPS
###############################
font_name = pygame.font.match_font('arial')
################################
def main_menu(): #main menu class only displays the get ready text
    global screen #set screen global
    
    while True: #fill screen and render text
        screen.fill(BLACK)
        draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
        pygame.display.update()
        break #break and start main loop
###########################################    
def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) #True denotes the font to be anti-aliased 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
##################################################33
def draw_lives(surf, x, y, lives, img): #Draw player lives
    for i in range(lives): #draws sprite according to how many lives there are
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
#################################################
def newmob(): #spawn a new enemy
    mob_element = Mob() #set mob_element 
    all_sprites.add(mob_element) #add to all_sprites
    mobs.add(mob_element) #spawn the enemy
##################################################
def newmobshoot(): #spawn a new enemy that shoots
    mob_element2 = Mob_shoot() #set mob_element2 
    all_sprites.add(mob_element2) #add to all_sprites
    mobs.add(mob_element2) #spawn the enemy
##############################################
def buddyspawn(): #spawn buddy
    buddy = Buddy() #set buddy
    all_sprites.add(buddy) #add to all_sprites
#############################################
class Player(pygame.sprite.Sprite):  #player class
    def __init__(self): #initialize varibles
        pygame.sprite.Sprite.__init__(self)
        ## scale the player img down
        self.image = pygame.transform.scale(player_img, (50, 60))  #scale the player img down
        self.image.set_colorkey(BLACK) #set colorkey 
        self.rect = self.image.get_rect() #set the rectangle collider 
        self.radius = 20 #radius of collider
        self.rect.centerx = WIDTH / 2 #placement of sprite on the x-axis(half the width of the screen)
        self.rect.bottom = HEIGHT - 10 #placement of the sprite on the y-axis
        self.speedx = 0 #define speedx
        self.speedy = 0 #define speedy
        self.shoot_delay = 150 #delay on shooting
        self.last_shot = pygame.time.get_ticks() #count time between shots
        self.lives = 3 #define lives
        self.power = 1 #define power
        self.power_timer = pygame.time.get_ticks() #power timer

    def update(self):
        #change sprite according to lives
        if self.lives == 3:
            self.image = pygame.transform.scale(player_img, (50, 60))
        if self.lives == 2:
            self.image = pygame.transform.scale(player_dmg1, (50, 60))
        if self.lives == 1:
            self.image = pygame.transform.scale(player_dmg2, (50, 60))
            
        ## time out for powerups    
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        self.speedx = 0 ## makes the player static in the screen by default.
        self.speedy = 0
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 

        ## will give back a list of the keys which happen to be pressed down at that moment
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
        if self.rect.top < 0:
            self.rect.top = 0

        self.rect.x += self.speedx #sets collider position to the direction of movement on the x-axis
        self.rect.y += self.speedy #sets collider position to the direction of movement on the y-axis

    def shoot(self): #shooting function
        now = pygame.time.get_ticks() #starts timing when function is called
        if now - self.last_shot > self.shoot_delay: #uses math to check if the delay is over
            self.last_shot = now #resets counter
            if self.power == 1: #when power=1 shoot 1 bullet
                bullet = Bullet(self.rect.centerx, self.rect.top) #draws bullet and sets it on its course 
                all_sprites.add(bullet) #adds the bullet to all_sprites group 
                bullets.add(bullet) #adds the bullet to the bullet group
                shooting_sound.play() #plays shoot sound
            if self.power == 2: #when power = 2 shoot 2
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()

            if self.power >= 3: #when power equals 3 shoot 2 normal and 1 big
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                missile1 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(missile1)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(missile1)
                shooting_sound.play()
                missile_sound.play()

    def powerup(self): #when collided with shoot powerup
        self.power += 1
        self.power_time = pygame.time.get_ticks()
################################################
class Buddy(pygame.sprite.Sprite): #Buddy Class
    def __init__(self): #initialize varibles
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(buddy_img, (40, 50)) #scale the buddy img down
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
        
        # check for the borders at the left and right, top and bottom
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
            
        hits = pygame.sprite.spritecollide(self, mobs, True, pygame.sprite.collide_circle) #collision       ## gives back a list, True makes the mob element disappear
        for hit in hits: #when hit kill the enemy, spawn a new one
            newmob()
            player_die_sound.play() #play sound 
            self.lives -= 1 #lose a life
            enemy_hit_sound.play() #play sound

        hits = pygame.sprite.spritecollide(self, enemybullets, True, pygame.sprite.collide_circle) #checks for collisions between player1 and player2 bullets 
        for hit in hits: #when hit play sounnd and subtract a life
            pygame.display.update()
            player_die_sound.play()
            self.lives -= 1
            
        if self.lives == 0: #when buddy has no health kill him and dispose of corpse outside of playable game 
            self.kill()
            self.rect.centerx = WIDTH + 100
            self.rect.top = HEIGHT - 1150
        
    def shoot(self): #shooting function
        now = pygame.time.get_ticks() #starts timing when function is called
        if now - self.last_shot > self.shoot_delay: #uses math to check if the delay is over
            self.last_shot = now #resets counter
            bullet = Bullet(self.rect.centerx, self.rect.top) #draws bullet and sets it on its course 
            all_sprites.add(bullet) #adds the bullet to all_sprites group 
            bullets.add(bullet) #adds the bullet to the bullet group
            shooting_sound.play() #plays shoot sound
#########################################
# defines the enemies
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(alien_images) #set sprite from a random image in a list
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width) #placement of sprite on the x-axis (randomized)
        self.rect.y = random.randrange(-150, -100) #placement of the sprite on the y-axis
        self.speedy = random.randrange(5, 20)        ## for randomizing the speed of the Mob
        self.lives = 2
        
        ## randomize the movements a little more 
        self.speedx = random.randrange(-3, 3)

        ## adding rotation to the mob element
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()  ## time when the rotation has to happen
        
    def rotate(self):
        time_now = pygame.time.get_ticks() #time is a timer
        if time_now - self.last_update > 50: # in milliseconds
            self.last_update = time_now
            self.rotation = (self.rotation + self.rotation_speed) % 360  #rotate 
            new_image = pygame.transform.rotate(self.image_orig, self.rotation) #apply the rotation to the sprite
            old_center = self.rect.center #the next redefine the center and collider of the sprite
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()#call rotate function
        self.rect.x += self.speedx #set rect.x
        self.rect.y += self.speedy  #set rect.y
        ## now what if the mob element goes out of the screen
        #if the sprite travels of screen set the x and y to make the sprite come back from top of screen
        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)        ## for randomizing the speed of the Mob

        hits = pygame.sprite.spritecollide(self, bullets, 1) #collision with bullets
        for hit in hits:
            global score #get score
            self.lives -= 1 #lose a life
            self.image_orig = random.choice(hitalien_images) #set sprite to new one
            self.image_orig.set_colorkey(BLACK) #set colorkey
            score += 50 #add score
            enemy_hit_sound.play()#play sound

        if self.lives <= 0: #when lives are equal to 0 kill it
            score += 100 #add score
            self.kill() #kill it
            if random.random() > 0.9: #random chance to spawn a powerup
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
                enemy_hit_sound.play()
            newmob()#new enemy
##################################################
class Mob_shoot(pygame.sprite.Sprite): #same thing as the mob but shoots 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = shootalien_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-70, -50)
        self.speedy = 1     ## for randomizing the speed of the Mob
        self.lives = 2
        self.powerdown_timer = pygame.time.get_ticks()
        self.shoot_delay = 350
        self.last_shot = pygame.time.get_ticks()
        self.step = 0
        self.threshold = random.randrange(5,20)
        
        ## randomize the movements a little more 
        self.speedx = random.randrange(-3, 3)

    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            enemybullet = Enemybullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(enemybullet)
            enemybullets.add(enemybullet)
            shooting_sound.play()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.step >= self.threshold:
            self.dir = random.randint(1,2)
            if self.dir == 1: 
                self.shoot()
            if self.dir == 2: 
                self.rect.x-=0;
            self.threshold = random.randrange(5,20)
            self.step = 0
        self.step += 1
        ## now what if the mob element goes out of the screen

        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-70, -50)
            self.speedy = 1       ## for randomizing the speed of the Mob

        hits = pygame.sprite.spritecollide(self, bullets, 1)
        for hit in hits:
            global score
            self.lives -= 1
            self.image_orig = random.choice(hitalien_images)
            self.image_orig.set_colorkey(BLACK)
            score += 50
            enemy_hit_sound.play()

        if self.lives <= 0:
            score += 100
            self.kill()
            if random.random() > 0.9:
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
                enemy_hit_sound.play()
            newmobshoot()
                    
## defines the sprite for Powerups
class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['gun', 'life', 'buddy'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.center = center
        self.speedy = 5

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.top > HEIGHT:
            self.kill()

## defines the sprite for bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()

        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop

## defines the sprite for bullets
class Enemybullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemybullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = 8

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()

        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop

## FIRE ZE MISSILES
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


###################################################
## Load all game images

background = pygame.image.load(path.join(img_dir, 'space background.gif'))
background_rect = background.get_rect()
## ^^ draw this rect first

shootalien_img = pygame.image.load(path.join(img_dir, 'alienspaceship.png')).convert()
player_img = pygame.image.load(path.join(img_dir, 'ship2.png')).convert()
buddy_img = pygame.image.load(path.join(img_dir, 'buddy.png')).convert()
player_dmg1 = pygame.image.load(path.join(img_dir, 'ship5.png')).convert()
player_dmg2 = pygame.image.load(path.join(img_dir, 'ship6.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'gunshot.png'))
missile_img = pygame.image.load(path.join(img_dir, 'fire.png'))
enemybullet_img = pygame.image.load(path.join(img_dir, 'laserplayer2.png'))
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

## load power ups
powerup_images = {}
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bullet powerups.png')).convert()
powerup_images['life'] = pygame.image.load(path.join(img_dir, 'lifepowerup.png')).convert()
powerup_images['buddy'] = pygame.image.load(path.join(img_dir, 'supporterpowerup.png')).convert()
###################################################
### Load all game sounds
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'lazer1.wav'))
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'fire2.wav'))
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
## main background music
#pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.2)      ## simmered the sound down a little

player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'hit2.wav'))
enemy_hit_sound = pygame.mixer.Sound(path.join(sound_folder, 'hitalien.wav'))
###################################################

## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

## spawn a group of mob
mobs = pygame.sprite.Group()
for i in range(3):      
    newmob()
    
for i in range(2):      
    newmobshoot()

## group for bullets
bullets = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

#### Score board variable
score = 0
#############################
## Game loop
running = True
menu_display = True
paused = False
while running:
    if menu_display:
        main_menu()
        pygame.time.wait(1500)
        menu_display = False

        #Stop menu music
        pygame.mixer.music.stop()
        #Play the gameplay music
        pygame.mixer.music.load(path.join(sound_folder, 'Resistance - Galactic.mp3'))
        pygame.mixer.music.play(-1)     ## makes the gameplay sound in an endless loop
        
        menu_display = False
        
    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        ## Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_p:
                paused = not paused
        # ## event for shooting the bullets
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function

    #2 Update
    if paused == False:
        all_sprites.update()


        ## check if a bullet hit a mob
        ## now we have a group of bullets and a group of mob
          ## spawn a new mob

        ## ^^ the above loop will create the amount of mob objects which were killed spawn again
        #########################

        ## check if the player collides with the mob
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
        for hit in hits:
            enemy_hit_sound.play()
            newmob()
            player_die_sound.play()
            player.lives -= 1
        
        hits = pygame.sprite.spritecollide(player, enemybullets, True, pygame.sprite.collide_circle) #checks for collisions between player1 and player2 bullets 
        for hit in hits: #when hit play sounnd and subtract a life
            pygame.display.update()
            player_die_sound.play()
            player.lives -= 1

     ## if the player hit a power up
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'gun':
                player.powerup()
            if hit.type == 'life' and player.lives <= 5:
                player.lives += 1
            if hit.type == 'buddy':
                buddyspawn()

        ## if player died and the explosion has finished, end game
        if player.lives == 0:
            pygame.time.wait(300)
            screen.fill(BLACK)
            draw_text(screen, str("Final Score :"), 32, WIDTH / 2.3, 250) 
            draw_text(screen, str(score), 32, WIDTH / 1.8, 250) 
            highscore(screen, 'scores.txt', score) #call highscore module
            running = False

        #3 Draw/render
        screen.fill(BLACK)
        ## draw the stargaze.png image
        screen.blit(background, background_rect)

        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)     ## 10px down from the screen
        # Draw lives
        draw_lives(screen, WIDTH - 1080, 10, player.lives, player_mini_img)


        ## Done after drawing everything to the screen
        pygame.display.flip()
    if paused == True:
         draw_text(screen, str("Paused"), 32, WIDTH / 2, 250)     ## 10px down from the screen
    pygame.display.update()
        
pygame.quit()
