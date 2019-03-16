import pygame, sys
from pygame.locals import *
from random import randint
import os
import pygame

inventory = ["nothing"]


# colors
black = (0, 0, 0)
blue = (255, 60, 0)
epic = (255, 0, 255)
green = (100, 255, 100)


# Window size
width = 880
Length = 1020

# Starting score for the player
current_score = 0

# Direction
UP = 8
DOWN = 2
LEFT = 4
RIGHT = 6

pause = False

# block (size of 1 block)
block = [20, 20]

# Snake
snake = [[30, 120], [10, 120]]

snake_head = [30, 120]

x = randint(0, 20)
y = randint(0, 19)

food = 0
while True:
    x1 = randint(0, 20)
    y1 = randint(0, 17)
    foodXY = [int(x1 * 40) + 10, int(y1 * 40) + 120]
    if snake.count(foodXY) == 0:
        food = 1
        break

bomb = 0
while True:
    bx1 = randint(0, 20)
    by1 = randint(0, 17)
    bombXY = [int(bx1 * 40) + 20, int(by1 * 40) + 220]
    break

# Direction
Direction = DOWN

dead = 0

current_score = 0

# Creates the background object
background = pygame.display.set_mode((width, Length), 0, 32)

# Window caption
pygame.display.set_caption('Snake')

# set up
pygame.init()
mainClock = pygame.time.Clock()

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font("font.ttf", 30)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (100, 255, 100)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "font1.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30


def main_menu():
    menu = True
    menu_items = ["Easy", "Medium", "Hard", "Insane", "Quit"]
    selected_menu = 0

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Main Menu UI
            screen.fill(green)
            title = text_format("SNAKE", font, 90, (0, 255 , 0))
            title_rect = title.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))

            for index, menu_item in enumerate(menu_items):
                if selected_menu == index:
                    current_text = text_format(menu_item, font, 75, white)
                else:
                    current_text = text_format(menu_item, font, 75, black)

                text_rect = current_text.get_rect()
                screen.blit(current_text, (screen_width / 2 - (text_rect[2] / 2), 200 + index * 50))
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_menu = selected_menu + 1
                if selected_menu >= len(menu_items):
                    selected_menu = 0

                if event.key == pygame.K_UP:
                    selected_menu = selected_menu - 1
                    if selected_menu < 0:
                        selected_menu = len(menu_items) - 1

                if event.key == pygame.K_RETURN:
                    menu = False
                    if selected_menu == 0:
                        inventory.append("Easy")
                        game()
                    if selected_menu == 1:
                        inventory.append("Medium")
                        game()
                    if selected_menu == 2:
                        inventory.append("Hard")
                        game()
                    if selected_menu == 3:
                        inventory.append("Insane")
                        game()
                    if selected_menu == 4:
                        pygame.quit()
                        quit()

            pygame.display.update()
            clock.tick(FPS)


def game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    UP = 8
    DOWN = 2
    LEFT = 4
    RIGHT = 6

    speed = 10

    dead = 0
    Direction = DOWN
    # colors
    black = (0, 0, 0)
    blue = (255, 60, 0)
    epic = (255, 0, 255)
    green = (100, 255, 100)

    # Window size
    width = 880
    Length = 1020

    # Starting score for the player
    current_score = 0

    # block (size of 1 block)
    block = [20, 20]

    # Snake
    snake = [[30, 120], [10, 120]]
    snake_head = [30, 120]

    x = randint(0, 20)
    y = randint(0, 19)

    food = 0
    while True:
        x1 = randint(0, 20)
        y1 = randint(0, 17)
        foodXY = [int(x1 * 40) + 10, int(y1 * 40) + 120]
        if snake.count(foodXY) == 0:
            food = 1
            break

    bomb = 0
    while True:
        bx1 = randint(0, 20)
        by1 = randint(0, 17)
        bombXY = [int(bx1 * 40) + 20, int(by1 * 40) + 220]
        break

    # Direction
    Direction = DOWN

    dead = 0

    current_score = 0

    # Creates the background object
    background = pygame.display.set_mode((width, Length), 0, 32)
    high_score = load_current_high_score()
    
    while 1 + 1 == 2:
        # See if QUIT has occured
        for event in pygame.event.get():
            if event.type == QUIT:
                break


            if event.type == KEYDOWN:
                # check if for keypress
                if ((event.key == K_LEFT or event.key == ord('a'))
                        and Direction != RIGHT):
                    Direction = LEFT
                elif ((event.key == K_RIGHT or event.key == ord('d'))
                      and Direction != LEFT):
                    Direction = RIGHT
                elif ((event.key == K_UP or event.key == ord('w'))
                      and Direction != DOWN):
                    Direction = UP
                elif ((event.key == K_DOWN or event.key == ord('s'))
                      and Direction != UP):
                    Direction = DOWN

            # press ESC to exit game
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()

        # Calculate snake head movment
        if Direction == RIGHT:
            snake_head[0] += 20
            if snake_head[0] > width - 20:
                dead = 1
        elif Direction == LEFT:
            snake_head[0] -= 20
            if snake_head[0] < 10:
                dead = 1
        elif Direction == UP:
            snake_head[1] -= 20
            if snake_head[1] < 110:
                dead = 1
        elif Direction == DOWN:
            snake_head[1] += 20
            if snake_head[1] > Length - 30:
                dead = 1

        # If we eat ourselves we die
        if snake.count(snake_head) > 0:
            dead = 1

        # Create new block for snakes body
        if food == 0:
            while True:
                x1 = randint(0, 20)
                y1 = randint(0, 17)
                foodXY = [int(x1 * 20) + 10, int(y1 * 20) + 120]
                if snake.count(foodXY) == 0:
                    food = 1
                    break

        # Insert a snake_head
        snake.insert(0, list(snake_head))

        # Se a snake_head tiver as mms coordenadas que a food entao...
        if snake_head[0] == foodXY[0] and snake_head[1] == foodXY[1]:
            food = 0
            current_score += 5
            pygame.display.set_caption("Snake made by ME!!!|Score: " + str(current_score))
        else:
            # remove the tail
            snake.pop()

        if snake_head[0] == bombXY[0] and snake_head[1] == bombXY[1]:
            dead = 1

        # fill in background
        background.fill(green)

        # draw scoreboard
        pygame.draw.rect(background, (0, 0, 0), Rect([10, 10], [860, 100]), 1)

        # Text
        font = pygame.font.Font("font.ttf", 30)
        text = font.render("Current score: " + str(current_score), 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.left = 75
        textpos.top = 30
        background.blit(text, textpos)

        if "Easy" in inventory:
            speed = 5

        if "Medium" in inventory:
            speed = 12

        if "Hard" in inventory:
            speed = 20

        if "Insane" in inventory:
            speed = 30

        text1 = font.render("High score: " + str(high_score), 1, (0, 0, 0))
        textpos1 = text1.get_rect()
        textpos1.left = 75
        textpos1.top = 60
        background.blit(text1, textpos1)

        # Draw the snake
        for x in snake:
            pygame.draw.rect(background, black, Rect(x, block))

        # Draw the food
        pygame.draw.rect(background, (100, 200, 100), Rect(foodXY, block))
        pygame.draw.rect(background, (255, 200, 100), Rect(bombXY, block))

        # Draws objects on the screen
        pygame.display.update()
        mainClock.tick(speed)  # FPS

        if dead == 1:
            break

    save_high_score(high_score, current_score)


def load_current_high_score():
    file_name = get_high_score_file_name()

    high_score = 0

    try:
        high_score_file = open(file_name, "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        # If there is a error while reading file
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(high_score, current_score):
    if current_score > high_score:
        # Save to disk
        file_name = get_high_score_file_name()
        try:
            # Write the file to disk
            high_score_file = open(file_name, "w")
            high_score_file.write(str(current_score))
            high_score_file.close()
        except IOError:
            # Can't write to the file
            print("Unable to save the high score.")


def get_high_score_file_name():
    if "Easy" in inventory:
        file_name = "easy.txt"
    if "Medium" in inventory:
        file_name = "medium.txt"
    if "Hard" in inventory:
        file_name = "hard.txt"
    if "Insane" in inventory:
        file_name = "insane.txt"
    return file_name

def game_over():
    menu = True
    menu_items = ["Play again", "Credits", "Quit"]
    selected_menu = 0
    if "Easy" in inventory:
        inventory.remove("Easy")

    if "Medium" in inventory:
        inventory.remove("Medium")
    
    if "Hard" in inventory:
        inventory.remove("Hard")

    if "Insane" in inventory:
        inventory.remove("Insane")

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Main Menu UI
            screen.fill(green)
            title = text_format("SNAKE", font, 90, (0, 255 , 0))
            title_rect = title.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))

            for index, menu_item in enumerate(menu_items):
                if selected_menu == index:
                    current_text = text_format(menu_item, font, 75, white)
                else:
                    current_text = text_format(menu_item, font, 75, black)

                text_rect = current_text.get_rect()
                screen.blit(current_text, (screen_width / 2 - (text_rect[2] / 2), 200 + index * 50))
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_menu = selected_menu + 1
                if selected_menu >= len(menu_items):
                    selected_menu = 0

                if event.key == pygame.K_UP:
                    selected_menu = selected_menu - 1
                    if selected_menu < 0:
                        selected_menu = len(menu_items) - 1

                if event.key == pygame.K_RETURN:
                    menu = False
                    if selected_menu == 0:
                        main_menu()
                    if selected_menu == 1:
                        credits() 
                    if selected_menu == 2:
                        pygame.quit()
                        quit()

            pygame.display.update()
            clock.tick(FPS)

def credits():
    menu = True
    menu_items = ["Play again", "Credits", "Quit"]
    selected_menu = 0
    

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Main Menu UI
            screen.fill(green)
            title = text_format("SNAKE", font, 90, (0, 255 , 0))
            title_rect = title.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))

            for index, menu_item in enumerate(menu_items):
                if selected_menu == index:
                    current_text = text_format(menu_item, font, 75, white)
                else:
                    current_text = text_format(menu_item, font, 75, black)

                text_rect = current_text.get_rect()
                screen.blit(current_text, (screen_width / 2 - (text_rect[2] / 2), 200 + index * 50))
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_menu = selected_menu + 1
                if selected_menu >= len(menu_items):
                    selected_menu = 0

                if event.key == pygame.K_UP:
                    selected_menu = selected_menu - 1
                    if selected_menu < 0:
                        selected_menu = len(menu_items) - 1

                if event.key == pygame.K_RETURN:
                    menu = False
                    if selected_menu == 0:
                        main_menu()
                    if selected_menu == 1:
                        credits() 
                    if selected_menu == 2:
                        pygame.quit()
                        quit()

            pygame.display.update()
            clock.tick(FPS)

main_menu()
while 1 + 1 == 2:
    game_over()