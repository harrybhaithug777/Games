import pygame
import random
import datetime

pygame.init()

# Creating game window
screen_width = 1200
screen_hight = 600
gameWindow = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Snakes By Harshit Chaudhary")
pygame.display.update()


# Creating background image
bgimg = pygame.image.load("Images\SnakeHome.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_hight)).convert_alpha()
bgimg2 = pygame.image.load("Images\SnakeMain.png")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_hight)).convert_alpha()
bgimg3 = pygame.image.load("Images\Game Over.png")
bgimg3 = pygame.transform.scale(bgimg3, (screen_width, screen_hight)).convert_alpha()



# Creating some specific variables outside of game loop
font = pygame.font.SysFont(None, 55)
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
clock = pygame.time.Clock()
FPS = random.randint(50, 70)




# Creating functions
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, size, size])

# Welcome Function
def welcome():
    exit_game = False


    while not exit_game:
        gameWindow.fill(Black)
        gameWindow.blit(bgimg, (0, 0))
        text_screen("Welcome to Snakes! Press Enter to Start", Red, 260, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameloop()
        pygame.display.update()
        clock.tick(FPS)


# Game Loop
def gameloop():
    pygame.mixer.music.load("Media\Losing My Mind - NEFFEX.mp3")
    pygame.mixer.music.play(-1)
    # Game specefic variables
    exit_game = False
    game_over = False
    black = (0, 0, 0)
    White = (255, 255, 255)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    snake_x = 45
    snake_y = 55
    snake_list = []
    snake_length = 1
    size = 10
    clock = pygame.time.Clock()
    velocity_x = 0
    velocity_y = 0
    init_velocity = 6
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_hight)
    food_size = 20
    score = 0
    FPS = random.randint(50, 70)

    while not exit_game:
        if game_over:
            gameWindow.fill(Red)
            gameWindow.blit(bgimg3, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                if event.key == pygame.K_LSHIFT:
                    welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score+=1
                        snake_length+=5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score+=1
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_hight)
                snake_length += 5


            gameWindow.fill(Black)
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("Score: "+ str(score * 10), Red, 5, 5)
            text_screen("Score: "+ str(score * 10), Red, 5, 5)
            pygame.draw.rect(gameWindow, Green, [food_x, food_y, food_size, food_size])
            text_screen("FPS: "+ str(FPS), Red, 5, 55)
            text_screen("X: "+ str(snake_x), Red, 1060, 5)
            text_screen("Y: "+ str(snake_y), Red, 1060, 55)
            


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            

            if head in snake_list[:-1]:
                game_over = True
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hight:
                game_over = True



            # pygame.draw.rect(gameWindow, Red, [snake_x, snake_y, size, size])
            plot_snake(gameWindow, Red, snake_list, size)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()
welcome()
