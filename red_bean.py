import pygame as pg
import random

#define color
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)


class Block(pg.sprite.Sprite):


    def __init__(self, color, width, height):
        super().__init__()

        #create block
        self.image = pg.Surface([width, height])
        self.image.fill(color)

        #the object size
        self.rect = self.image.get_rect()

   
pg.init()


#design the screen size
w = 700
h = 400
screen = pg.display.set_mode([w, h])

#block group
block_list = pg.sprite.Group()

#block and player group
all_sprites_list = pg.sprite.Group()


#create block
for i in range(50):

    #a block
    block = Block(BLACK, 20, 15)

    #location of block
    block.rect.x = random.randrange(w)
    block.rect.y = random.randrange(h)

    #add to group
    block_list.add(block)
    all_sprites_list.add(block)



#Create player
player = Block(RED, 20, 15)
all_sprites_list.add(player)

#Loop until clicks the close button
done = False

#Used to manage fps

clock = pg.time.Clock()


score = 0


#---------- Main Progam ----------


while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    #the background 
    screen.fill(WHITE)

    #get the mouse position (return a list of two numbers)
    pos = pg.mouse.get_pos()

    #player = mouse position
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    #controll collide event
    blocks_hit_list = pg.sprite.spritecollide(player, block_list, True)

    #collide score
    for block in blocks_hit_list:
        score += 1
        #player.enlarge(10)
        print("Score : ",score)


    
    all_sprites_list.draw(screen)


    #update the draw
    pg.display.update()


    #fps
    clock.tick(60)
    
pg.quit()





























