import pygame
import random


# Init game
pygame.init()
eat_sound = pygame.mixer.Sound('sounds/eat.mp3')
game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')
pygame.mixer.music.set_volume(30)

# Основные цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка V2')


# Функция для отрисовки змейки
def draw_snake(surface, snake, color):
    for segment in snake:
        pygame.draw.rect(surface, color, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


# Функция для отрисовки яблока
def draw_apple(surface, apple):
    pygame.draw.rect(surface, RED, (apple[0], apple[1], CELL_SIZE, CELL_SIZE))


# Запуск игры для 2 игроков
def start_2p_game():
    snake1 = [(200, 200)]
    snake2 = [(600, 400)]
    direction1 = ""
    direction2 = ""
    apple = (random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE, 
             random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)
    score1 = 1
    score2 = 1
    clock = pygame.time.Clock()
    snake_started = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    snake_started = not snake_started
                else:
                    if event.key == pygame.K_UP and direction1 != "DOWN":
                        direction1 = "UP"
                    elif event.key == pygame.K_DOWN and direction1 != "UP":
                        direction1 = "DOWN"
                    elif event.key == pygame.K_LEFT and direction1 != "RIGHT":
                        direction1 = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction1 != "LEFT":
                        direction1 = "RIGHT"
                    elif event.key == pygame.K_w and direction2 != "DOWN":
                        direction2 = "UP"
                    elif event.key == pygame.K_s and direction2 != "UP":
                        direction2 = "DOWN"
                    elif event.key == pygame.K_a and direction2 != "RIGHT":
                        direction2 = "LEFT"
                    elif event.key == pygame.K_d and direction2 != "LEFT":
                        direction2 = "RIGHT"
                    if not snake_started:
                        snake_started = True

        if snake_started:
            new_head1 = (snake1[0][0], snake1[0][1])
            new_head2 = (snake2[0][0], snake2[0][1])
            if direction1 == "UP":
                new_head1 = (new_head1[0], new_head1[1] - CELL_SIZE)
            elif direction1 == "DOWN":
                new_head1 = (new_head1[0], new_head1[1] + CELL_SIZE)
            elif direction1 == "LEFT":
                new_head1 = (new_head1[0] - CELL_SIZE, new_head1[1])
            elif direction1 == "RIGHT":
                new_head1 = (new_head1[0] + CELL_SIZE, new_head1[1])
            if direction2 == "UP":
                new_head2 = (new_head2[0], new_head2[1] - CELL_SIZE)
            elif direction2 == "DOWN":
                new_head2 = (new_head2[0], new_head2[1] + CELL_SIZE)
            elif direction2 == "LEFT":
                new_head2 = (new_head2[0] - CELL_SIZE, new_head2[1])
            elif direction2 == "RIGHT":
                new_head2 = (new_head2[0] + CELL_SIZE, new_head2[1])

            if (new_head1[0] < 0 or new_head1[0] >= SCREEN_WIDTH or
                new_head1[1] < 0 or new_head1[1] >= SCREEN_HEIGHT or
                new_head1 in snake1 or new_head1 in snake2) and direction1:
                if new_head1[0] >= SCREEN_WIDTH - 20 and new_head1[1] >= SCREEN_HEIGHT - 20:
                    new_head1 = (new_head1[0] - CELL_SIZE, new_head1[1] - CELL_SIZE)
                    direction1 = "UP"
                if new_head1[0] < 0:
                    new_head1 = (new_head1[0] + CELL_SIZE, new_head1[1])
                    direction1 = "DOWN"
                elif new_head1[0] >= SCREEN_WIDTH:
                    new_head1 = (new_head1[0] - CELL_SIZE, new_head1[1])
                    direction1 = "DOWN"
                elif new_head1[1] < 0:
                    new_head1 = (new_head1[0], new_head1[1] + CELL_SIZE)
                    direction1 = "LEFT"
                elif new_head1[1] >= SCREEN_HEIGHT:
                    new_head1 = (new_head1[0], new_head1[1] - CELL_SIZE)
                    direction1 = "RIGHT"
                elif new_head1 in snake1 or new_head1 in snake2:
                    return (
                        "Зелёный проиграл!",
                        score1,
                        score2
                    )

            if (new_head2[0] < 0 or new_head2[0] >= SCREEN_WIDTH or
                new_head2[1] < 0 or new_head2[1] >= SCREEN_HEIGHT or
                new_head2 in snake2 or new_head2 in snake1) and direction2:
                if new_head2[0] >= SCREEN_WIDTH - 20 and new_head2[1] >= SCREEN_HEIGHT - 20:
                    new_head2 = (new_head2[0] - CELL_SIZE, new_head2[1] - CELL_SIZE)
                    direction2 = "UP"
                if new_head2[0] < 0:
                    new_head2 = (new_head2[0] + CELL_SIZE, new_head2[1])
                    direction2 = "DOWN"
                elif new_head2[0] >= SCREEN_WIDTH:
                    new_head2 = (new_head2[0] - CELL_SIZE, new_head2[1])
                    direction2 = "DOWN"
                elif new_head2[1] < 0:
                    new_head2 = (new_head2[0], new_head2[1] + CELL_SIZE)
                    direction2 = "LEFT"
                elif new_head2[1] >= SCREEN_HEIGHT:
                    new_head2 = (new_head2[0], new_head2[1] - CELL_SIZE)
                    direction2 = "RIGHT"
                elif new_head2 in snake2 or new_head2 in snake1:
                    return (
                        "Оранжевый проиграл!",
                        score1,
                        score2
                    )
            touch1 = False
            touch2 = False
            if new_head1 == apple:
                apple = (random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE, 
                        random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)
                score1 += 1
                touch1 = True
                eat_sound.play()
            elif new_head2 == apple:
                apple = (random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE, 
                        random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)
                score2 += 1
                touch2 = True
                eat_sound.play()
            if not touch1:
                snake1.pop()
            if not touch2:
                snake2.pop()
            snake1.insert(0, new_head1)
            snake2.insert(0, new_head2)

        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 80)
        text1 = font.render(str(score1), True, GREEN)
        screen.blit(text1, ( SCREEN_WIDTH - text1.get_width(),0))
        text2 = font.render(str(score2), True, ORANGE)
        screen.blit(text2, (0,0))
        draw_snake(screen, snake1, GREEN)
        draw_snake(screen, snake2, ORANGE)
        draw_apple(screen, apple)
        pygame.display.flip()
        clock.tick(12)


# Запуск игры для 1 игрока
def start_1p_game():
    snake1 = [(200, 200)]
    direction1 = ""
    apple = (random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE, 
             random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)
    score1 = 1
    clock = pygame.time.Clock()
    snake_started = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    snake_started = not snake_started
                else:
                    if event.key == pygame.K_UP and direction1 != "DOWN":
                        direction1 = "UP"
                    elif event.key == pygame.K_DOWN and direction1 != "UP":
                        direction1 = "DOWN"
                    elif event.key == pygame.K_LEFT and direction1 != "RIGHT":
                        direction1 = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction1 != "LEFT":
                        direction1 = "RIGHT"
                    if not snake_started:
                        snake_started = True

        if snake_started:
            new_head1 = (snake1[0][0], snake1[0][1])
            if direction1 == "UP":
                new_head1 = (new_head1[0], new_head1[1] - CELL_SIZE)
            elif direction1 == "DOWN":
                new_head1 = (new_head1[0], new_head1[1] + CELL_SIZE)
            elif direction1 == "LEFT":
                new_head1 = (new_head1[0] - CELL_SIZE, new_head1[1])
            elif direction1 == "RIGHT":
                new_head1 = (new_head1[0] + CELL_SIZE, new_head1[1])

            if (new_head1[0] < 0 or new_head1[0] >= SCREEN_WIDTH or
                new_head1[1] < 0 or new_head1[1] >= SCREEN_HEIGHT or
                new_head1 in snake1 ) and direction1:
                if new_head1[0] >= SCREEN_WIDTH - 20 and new_head1[1] >= SCREEN_HEIGHT - 20:
                    new_head1 = (new_head1[0] - CELL_SIZE, new_head1[1] - CELL_SIZE)
                    direction1 = "UP"
                if new_head1[0] < 0:
                    new_head1 = (new_head1[0] + CELL_SIZE, new_head1[1])
                    direction1 = "DOWN"
                elif new_head1[0] >= SCREEN_WIDTH:
                    new_head1 = (new_head1[0] - CELL_SIZE, new_head1[1])
                    direction1 = "DOWN"
                elif new_head1[1] < 0:
                    new_head1 = (new_head1[0], new_head1[1] + CELL_SIZE)
                    direction1 = "LEFT"
                elif new_head1[1] >= SCREEN_HEIGHT:
                    new_head1 = (new_head1[0], new_head1[1] - CELL_SIZE)
                    direction1 = "RIGHT"
                elif new_head1 in snake1:
                    return (
                        "Проиграл!",
                        score1,
                    )

            touch1 = False
            if new_head1 == apple:
                apple = (random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE, 
                        random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)
                score1 += 1
                touch1 = True
                eat_sound.play()
            if not touch1:
                snake1.pop()
            snake1.insert(0, new_head1)

        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 80)
        text1 = font.render(str(score1), True, GREEN)
        screen.blit(text1, ( SCREEN_WIDTH - text1.get_width(),0))
        draw_snake(screen, snake1, GREEN)
        draw_apple(screen, apple)
        pygame.display.flip()
        clock.tick(12)

    
def get_players():
    while True:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 25)
        text = font.render(f"Привет! Это игра Змейка. Нажми 1 или 2, чтобы выбрать кол-во игроков", True, RED)
        screen.blit(text, (SCREEN_WIDTH / 6 - 30, SCREEN_HEIGHT / 3))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2
# Главная функция
def main():
    need_exit = False
    while not need_exit:
        again = True
        need_players = get_players()
        while again:
            if need_players == 1:
                game_over_text, score1 = start_1p_game()
            else:
                game_over_text, score1, score2 = start_2p_game()
            game_over_sound.play(0)
            need_break = False
            while not need_break:
                screen.fill(WHITE)
                font = pygame.font.SysFont(None, 25)
                if need_players == 2:
                    text = font.render(f"{game_over_text} Счёт: {score2}:{score1}. Нажмите ENTER для продолжения или Q для выхода.", True, RED)
                else:
                    text = font.render(f"{game_over_text} Счёт: {score1}. Нажмите ENTER для продолжения или Q для выхода в главное меню.", True, RED)
                screen.blit(text, (SCREEN_WIDTH / 6 - 100, SCREEN_HEIGHT / 3))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.QUIT:
                            need_exit = True
                        if event.key == pygame.K_q:
                            again = False
                            need_break = True
                        if event.key == pygame.K_RETURN:
                            need_break = True
                        break
    pygame.quit()


if __name__ == "__main__":
    main()