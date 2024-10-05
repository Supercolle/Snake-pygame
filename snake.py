import pygame
import random
import sys
import time



width = 800
height = 600

pygame.init()

root = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

fps = pygame.time.Clock()


snake_list= [[100,50],[87,50]]
snake_pos =[100,50]
#snake_len = 2


score = 0 


def game_over():
    my_font = pygame.font.SysFont('IMPACT', 90)
    game_over_surface = my_font.render('GAME OVER', True, 'white')
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2,height/4)
    root.fill('black')
    root.blit(game_over_surface, game_over_rect)
    show_score(0, 'green', 'impact', 15)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (width/2, (height/2)+50)
    else:
        score_rect.midtop = (width/2, (height/2)+50)
    root.blit(score_surface, score_rect)

##############################################################################
#---> RANDOM SQUARE FOOD
food_pos = [random.randrange(50, 750, 13), random.randrange(50, 550, 13)]  
food_spawn = True

direction = 'RIGHT'
change_direction = direction

vel = 15

running = True

while running:
    root.fill('black')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
##############################################################################
#---->BASIS FOR CHANGE DIRECTION         
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            change_direction = 'LEFT'
            
        elif event.key == pygame.K_RIGHT:
            change_direction = 'RIGHT'
            
        elif event.key == pygame.K_UP:
            change_direction = 'UP'
            
        elif event.key == pygame.K_DOWN:
            change_direction = 'DOWN'
            
##########################################################################
#----> MOVEMENT CONTROL
    if change_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'


##########################################################################
#----> SNAKE MOVEMENT
    if direction == 'UP':
        snake_pos[1] -= 5
    elif direction == 'DOWN':
        snake_pos[1] += 5
    elif direction == 'RIGHT':
        snake_pos[0] += 5
    elif direction == 'LEFT':
        snake_pos[0] -= 5


    

#########################################################################
#----> UPDATE SNAKE LIST
    snake_list.insert(0,list(snake_pos))


#########################################################################
#----> CHECK IF HE EATS FOOD AND UPDATE THE QUEUE
    if abs(snake_pos[0] - food_pos[0]) < 13 and abs(snake_pos[1] - food_pos[1]) < 13:
        food_spawn = False 
        score += 1 
    else:
        snake_list.pop()


#########################################################################
#---->RESPOWN FOOD AFTER BEING EATEN
    if not food_spawn:
        food_pos = [random.randrange(10, 750, 13), random.randrange(10, 550, 13)]
        food_spawn = True


    for pos in snake_list:
        pygame.draw.rect(root,'green',pygame.Rect(pos[0],pos[1],13,13))
        
#########################################################################
#----> COLLISION

    if snake_pos[0] == (width) - 5:
        game_over()
    elif snake_pos[0] == 5:
        game_over()
    elif snake_pos[1] == (height) - 5:
        game_over()
    elif snake_pos[1] == 5:
        game_over()
#########################################################################
#---->BODY COLLISION CONTROL 
    for block in snake_list[1:]:  
        if snake_pos == block:
            game_over()


    
    
    pygame.draw.rect(root,'white',pygame.Rect(food_pos[0],food_pos[1],13,13))

    fps.tick(60)
    pygame.display.update()