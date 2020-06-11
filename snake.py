import pygame, sys, time, random


#color

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)


#frame size
frame_size_x = 720
frame_size_y = 480
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Snake")


score = 0


#Snake
snake_pos = [300, 300]
snake_body = [[300, 300], [290, 300], [280, 300]]
direction = "RIGHT"
change_to = direction
speed = 10

#Point
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True


#Fps
fps_controller = pygame.time.Clock()
flag = 0


#Accelerate
def accelerate():
    global score
    global speed
    global flag
    if speed <= 27 and flag == 1:
        speed += 1
        flag = 0


#Show Score
def show_Score(choice, color, font, size):
    global score
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 2)
    game_window.blit(score_surface, score_rect)


#Show "restart"
def restart(color, font, size):
    restart_font = pygame.font.SysFont(font, size)
    restart_surface = restart_font.render('Press SPACE to restart', True, color)
    restart_rect = restart_surface.get_rect()
    restart_rect.midtop = (frame_size_x / 2, frame_size_y / 1.4)
    game_window.blit(restart_surface, restart_rect)
    



#Game Over
def gameover():
    global score
    global RED
    gameover_Font = pygame.font.SysFont('arial.ttf', 54)
    gameover_surface = gameover_Font.render('Game Over!!', True, RED)
    gameover_rect = gameover_surface.get_rect()
    gameover_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(BLACK)
    game_window.blit(gameover_surface, gameover_rect)
    show_Score(0, RED, 'times', 20)
    restart(BLUE, 'times', 30)
    pygame.display.flip() #更新視窗



    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                #time.sleep(1)
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #更新至初始狀態
                    global snake_pos
                    global snake_body
                    global direction
                    global change_to
                    global speed
                    speed = 10
                    score = 0
                    snake_pos = [300, 300]
                    snake_body = [[300, 300], [290, 300], [280, 300]]
                    direction = 'UP'
                    change_to = direction
                    time.sleep(1)
                    pygame.display.update()
                    main()
                    break



#Snake
class Snake:
    def __init__(self):
        pass
    
    #確認移動方向與控制者執行方向是否相反
    def make_sure(self):
        global direction
        global change_to
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'   
    

    #蛇變大
    def growing(self):
        global snake_body
        global score
        global food_spawn
        global flag
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            flag = 1
            food_spawn = False
        else:
            snake_body.pop()


    #移動
    def moving(self):
        global direction
        global snack_pos
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10


#吃的
class Food:
    
    def __init__(self):
        pass

    #食物的位置
    def spawing(self):
        global food_spawn
        global food_pos
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn = True

def main():
    pygame.init()
    global change_to
    global snake_body
    global snake_pos
    global flag


    while True:
        game_window.fill(BLACK)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:

                #按esc跳出
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)

                # w s a d 或 ↑ ↓ ← → 移動
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'

        snake = Snake()
        food = Food()

        snake.make_sure()
        snake.moving()
        snake.growing()
        food.spawing()


        #畫出蛇身
        for pos in snake_body:
            #snake body .draw.rect(視窗, 顏色, xy座標)
            pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))


        #畫出食物
        pygame.draw.rect(game_window, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))


        #Game Over Case
        #撞到邊界
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
            gameover()
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            gameover()

        #撞到自己
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                gameover()
            show_Score(1, WHITE, 'consolas', 20)

        #更新視窗
        pygame.display.update()

        #fps ->控制難度
        global speed
        accelerate()
        fps_controller.tick(speed)


if __name__ == '__main__':
    main()
    pygame.quit()











