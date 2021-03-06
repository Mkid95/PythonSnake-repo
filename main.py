import random
import pygame
"""
Basic snake game made using pygame
"""
pygame.init()
length = 5 #initial length of the snake
RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3 #constants to define directions initial direction is RIGHT
MOVE = 50 # the rate at which movement is calculated in ms
speed = 20
direction = RIGHT
move_event = pygame.USEREVENT + 1
screen = pygame.display.set_mode((840, 600))
pygame. display.set_caption("Snake")
clock = pygame.time
snakeImg = pygame.image.load('snek.png')
appleImg = pygame.image.load('python.png')
picture = pygame.transform.scale(snakeImg, (20, 20))
apple = pygame.transform.scale(appleImg, (20, 20))
snakeX, snakeY, foodX, foodY = 0, 0, 0, 0
trail = [] #array of snake's trail or body. Only stores coordinates


def spawn_snake():
    global snakeX
    snakeX = 0
    global snakeY
    snakeY = 0
    global trail
    trail = []
    global direction
    direction = RIGHT
    global length
    length = 5


def draw_snake():
    screen.blit(picture, (snakeX, snakeY))
    for i in trail:
        screen.blit(picture, (i[0], i[1]))


def spawn_food():
    global foodX
    foodX = random.randrange(42)*20
    global foodY
    foodY = random.randrange(30)*20
    for i in trail:
        if foodX == i[0] and foodY == i[1]:
            spawn_food()


def die():
    largeText = pygame.font.SysFont("arial", 100)
    TextSurf = largeText.render('Game Over', False, (0, 0, 0))
    draw_snake()
    screen.blit(apple, (foodX, foodY))
    screen.blit(TextSurf, (170, 200))
    pygame.display.update()
    clock.wait(1000)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                paused = False
    spawn_food()
    spawn_snake()

#Core game loop initiates here


spawn_food()
pygame.time.set_timer(move_event, MOVE)
change_direction = False
running = True
while running:
    screen.fill((128, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and change_direction == False:
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
                change_direction = True
            if event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
                change_direction = True
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
                change_direction = True
            if event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
                change_direction = True
        if event.type == move_event: #movement event moves the snake and checks if the movement kills the player or if the player has eaten the food.
            trail.append((snakeX, snakeY))
            if direction == RIGHT:
                snakeX += speed
            if direction == LEFT:
                snakeX -= speed
            if direction == DOWN:
                snakeY += speed
            if direction == UP:
                snakeY -= speed
            change_direction = False
            for i in trail:
                if snakeX == i[0] and snakeY == i[1]:
                    die()
            if snakeX > 840 or snakeY > 600 or snakeX < 0 or snakeY < 0:
                die()
            if snakeX == foodX and snakeY == foodY:
                length += 3
                spawn_food()
            if len(trail) > length:
                trail.pop(0)
    draw_snake()
    screen.blit(apple, (foodX, foodY))
    pygame.display.update()
