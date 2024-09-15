import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (200, 227, 167)
RED = (255, 0, 0)
PURPLE = (160, 32, 240)
PINK = (223, 10, 172)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sneakySnake")

# Snake properties
snake_block = 20
snake_speed = 10
speed_increase = 20

# Font
font_style = pygame.font.SysFont(None, 50)

def display_message(msg, color):
    msg_surf = font_style.render(msg, True, color)
    screen.blit(msg_surf, [SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3])

'''
def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_speed = 10

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()
    clock.tick(snake_speed)

    # Main Game Loop
    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Updating Snake Position
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(GREEN)
        pygame.draw.rect(screen, PINK, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for Collision with Itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Render Snake
        for segment in snake_List:
            pygame.draw.rect(screen, PURPLE, [segment[0], segment[1], snake_block, snake_block])

    

        # Check if Snake has Eaten the Food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            snake_speed += speed_increase
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()


'''






def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()

    # Main Game Loop
    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Updating Snake Position
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for Collision with Itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Render Snake
        for segment in snake_List:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        # Check if Snake has Eaten the Food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            snake_speed += speed_increase

        clock.tick(snake_speed)

    pygame.quit()
    quit()