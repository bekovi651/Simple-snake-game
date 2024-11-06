

#импортируем модули
import pygame
import random




games_count = 1
record = 0
def load():
    global games_count,record
    file = open('statistic.txt','r+')
    statictic = file.read().split(",")
    file.close()
    record = int(statictic[0])
    games_count = int(statictic[1])
def save():
    global games_count,record
    file = open('statistic.txt','r+')
    file.write(f'{record},{games_count}')
    file.close()
    




#инициальзируем
pygame.init()


#Задаем константы
HEIGHT = 600#высота
FRAME_COLOR = (0, 255, 204) #Цвет заливки нашего окна
RECT_COLOR = (255, 255, 255)
OTHER_RECT_COLOR = (204, 255, 255)
SIZE_RECT = 20
COUNT_RECTS = 20
RETURN = 1
WIGHT = SIZE_RECT * COUNT_RECTS + 2 * SIZE_RECT + RETURN * SIZE_RECT
HEADER_RECT = 70
HEADER_COLOR = (0, 204, 153)
COLOR_SNAKE = (0, 102, 0)
FOOD_COLOR = (255, 0, 0)
def draw_rect(color, row, column):
    pygame.draw.rect(app, color, [SIZE_RECT+column*SIZE_RECT+RETURN*(column+1),HEADER_RECT+SIZE_RECT+row*SIZE_RECT+RETURN*(row+1),SIZE_RECT, SIZE_RECT])


#Инициализируем звуковой модуль
pygame.mixer.init()

#Загружаем музыку
soundtrack = pygame.mixer.Sound("soundtrack.mp3")
eat = pygame.mixer.Sound("eat.mp3")


#Рисуем окно
app = pygame.display.set_mode((WIGHT, HEIGHT))

#Задаем заголовок программы
pygame.display.set_caption('Hangry Snake')

#Для того, чтобы окно не закрывалось, создаем игровой цикл
   


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def inside(self):
        return 0 <= self.x < COUNT_RECTS and 0 <= self.y < COUNT_RECTS
    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y
def random_food_block():
    x = random.randint(0, COUNT_RECTS - 1)
    y = random.randint(0, COUNT_RECTS - 1)
    food_block = Snake(x, y)
    while food_block in snake_rect:
        food_block.x = random.randint(0, COUNT_RECTS - 1)
        food_block.y = random.randint(0, COUNT_RECTS - 1)
    return food_block




game = True
load()
way = 0

def draw_head(snake_rect):
    global way,COLOR_SNAKE
    draw_rect(COLOR_SNAKE, snake_rect[-1].x, snake_rect[-1].y)
    x = SIZE_RECT+snake_rect[-1].y*SIZE_RECT+RETURN*(snake_rect[-1].y+1)
    y = HEADER_RECT+SIZE_RECT+snake_rect[-1].x*SIZE_RECT+RETURN*(snake_rect[-1].x+1)
    if way == 0:
        
        pygame.draw.rect(app, (0,0,0), [8 + x,3 + y,4,4])
        pygame.draw.rect(app, (0,0,0), [8 + x,13+y,4,4])
        pygame.draw.rect(app, FOOD_COLOR, [15 + x,3 + y,2,14])
    elif way == 1:
        pygame.draw.rect(app, (0,0,0), [3 + x,8 + y,4,4])
        pygame.draw.rect(app, (0,0,0), [13 + x,8+y,4,4])
        pygame.draw.rect(app, FOOD_COLOR, [3 + x,15 + y,14,2])
    elif way == 3:
        pygame.draw.rect(app, (0,0,0), [3 + x,12 + y,4,4])
        pygame.draw.rect(app, (0,0,0), [13 + x,12+y,4,4])
        pygame.draw.rect(app, FOOD_COLOR, [3 + x,5 + y,14,2])
    if way == 2:
        
        pygame.draw.rect(app, (0,0,0), [8 + x,3 + y,4,4])
        pygame.draw.rect(app, (0,0,0), [8 + x,13+y,4,4])
        pygame.draw.rect(app, FOOD_COLOR, [3 + x,3 + y,2,14])


while game:
    way = 0
    game_over = False
    is_game_started = False 
    snake_rect = [Snake(9,9)]

    food = random_food_block()
    x_row = 0
    y_col = 1
    result = 0
    time = pygame.time.Clock()


    soundtrack.play(loops=-1)
    block = False
    if not is_game_started:
        while not is_game_started:
            app.fill(FRAME_COLOR)
            pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIGHT, HEADER_RECT])
            for row in range(COUNT_RECTS):
                for column in range(COUNT_RECTS):
                    if (row + column) % 2 == 0:
                        color = RECT_COLOR
                    else:
                        color = OTHER_RECT_COLOR
                    draw_rect(color, row, column)
            
            

            
            draw_head(snake_rect)
            
            text_menu = pygame.font.SysFont('sand', 40).render('Нажмите кнопку, чтобы начать', 0, (0,0,0))
            app.blit(text_menu, (SIZE_RECT, 30))
            pygame.display.update()
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    game_over = True
                    game = False
                    is_game_started = True
                    save()
                    
                
                elif event.type == pygame.KEYDOWN:
                    if not is_game_started:
                        is_game_started = True
    
        
    while not game_over:
        block = False
                
    #Создаем цикл for для обработки событий, в конкретном случае обрабатываем закрытие окна
        change_head = True
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_over = True
                game = False
                is_game_started = False
                save()
                
            
            elif event.type == pygame.KEYDOWN:
                
                if not block:
                    if event.key == pygame.K_UP and y_col != 0:
                        x_row = -1
                        y_col = 0
                        block = True
                        way = 3
                        
                    elif event.key == pygame.K_DOWN and y_col != 0:
                        x_row = 1
                        y_col = 0
                        block = True
                        way = 1
                    elif event.key == pygame.K_RIGHT and x_row != 0:
                        x_row = 0
                        y_col = 1
                        block = True
                        way = 0
                    elif event.key == pygame.K_LEFT and x_row != 0:
                        x_row = 0
                        y_col = -1
                        block = True
                        way = 2
        app.fill(FRAME_COLOR)
        pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIGHT, HEADER_RECT])
        


        for row in range(COUNT_RECTS):
            for column in range(COUNT_RECTS):
                if (row + column) % 2 == 0:
                    color = RECT_COLOR
                else:
                    color = OTHER_RECT_COLOR
                draw_rect(color, row, column)
        draw_rect(FOOD_COLOR, food.x, food.y)
        x = SIZE_RECT+food.y*SIZE_RECT+RETURN*(food.y+1)
        y = HEADER_RECT+SIZE_RECT+food.x*SIZE_RECT+RETURN*(food.x+1)
        pygame.draw.rect(app, (150,75,0), [x +9,y , 4,2])
        pygame.draw.rect(app, (0,170,0), [x +9,y+2 , 4,2])
        pygame.draw.rect(app, (0,170,0), [x +8,y +4 , 4,4])

        
        for i in range(len(snake_rect)):
            draw_rect(COLOR_SNAKE, snake_rect[i].x, snake_rect[i].y)
            x = SIZE_RECT+snake_rect[i].y*SIZE_RECT+RETURN*(snake_rect[i].y+1)
            y = HEADER_RECT+SIZE_RECT+snake_rect[i].x*SIZE_RECT+RETURN*(snake_rect[i].x+1)
            pygame.draw.rect(app, (0, 60, 0), [8 + x,8 + y,4,4])
            
        draw_head(snake_rect)
            
                

        head = snake_rect[-1]

        
            


        if food == head:
            result += 1
            eat.play()
            snake_rect.append(food)
            food = random_food_block()
            if record < result:
                    record = result
                    save()



        

        if not head.inside():
            game_over = True
            games_count += 1
            save()
        if change_head == True:
            new_head = Snake(head.x + x_row, head.y + y_col)
            snake_rect.append(new_head)
            snake_rect.pop(0)
        text_result = pygame.font.SysFont('sand', 50).render(f'Очки: {result}', 0, RECT_COLOR)
        app.blit(text_result, (SIZE_RECT, SIZE_RECT))
        text_result = pygame.font.SysFont('sand', 50).render(f'Рекорд: {record}', 0, RECT_COLOR)
        app.blit(text_result, (240, SIZE_RECT))
        text_result = pygame.font.SysFont('sand', 50).render(f'Игр сыгранно: {games_count}', 6, RECT_COLOR)
        app.blit(text_result, (SIZE_RECT, 540))
        pygame.display.update()
        time.tick(2)
        for rect in range(len(snake_rect)-1):
            if new_head == snake_rect[rect]:
                game_over = True
                games_count += 1
                if record < result:
                    record = result

        block = False
    soundtrack.stop()
    pygame.mixer.music.unload() 

    while game_over and game:
        mouse = pygame.mouse.get_pos() 
        
        


                    
        app.fill(FRAME_COLOR)
        for row in range(COUNT_RECTS):
            for column in range(COUNT_RECTS):
                if (row + column) % 2 == 0:
                    color = RECT_COLOR
                else:
                    color = OTHER_RECT_COLOR
                draw_rect(color, row, column)
        pygame.draw.rect(app, (0,0,0), [20,20,190, 40])
        pygame.draw.rect(app, (0,0,0), [250,20,190, 40])
        pygame.draw.rect(app, (255,255,255), [21,21,188, 38])
        pygame.draw.rect(app, (255,255,255), [251,21,188, 38])
        pygame.draw.rect(app, (255,255,255), [43,113,374, 374])
        
        text_result = pygame.font.SysFont('sand', 50).render(f'Очки: {result}', 0, (0,0,0))
        app.blit(text_result, (100, 250))
        text_result = pygame.font.SysFont('sand', 60).render(f"Вы проиграли!", 0, (0,0,0))
        app.blit(text_result, (60, 180))
        text_result = pygame.font.SysFont('sand', 50).render(f'Рекорд: {record}', 0, (0,0,0))
        app.blit(text_result, (100, 310))
        text_result = pygame.font.SysFont('sand', 50).render(f'Игр сыгранно: {games_count}', 6, (0,0,0))
        app.blit(text_result, (100, 370))



        text_result = pygame.font.SysFont('sand', 40).render(f"Ещё раз!", 0, (0,0,0))
        app.blit(text_result, (45, 28))
        text_result = pygame.font.SysFont('sand', 40).render(f"Выйти", 0, (0,0,0))
        app.blit(text_result, (300, 28))

        pygame.display.update()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                save()
                game = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if 250 <= mouse[0] <= 440 and 20 <= mouse[1] <= 60: 
                    game = False
                    
                    save()
                elif 20 <= mouse[0] <= 210 and 20 <= mouse[1] <= 60: 
                    
                    game_over = False
                    save()



             
#Прекращаем проигрывание музыки и освобождаем ресурсы

pygame.mixer.music.unload() 
pygame.quit()

        



