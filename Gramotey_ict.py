import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна игры
width, height = 400, 600
screen = pygame.display.set_mode((width, height))

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# ФПС
clock = pygame.time.Clock()

# Параметры игрока
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 10

# Параметры препятствий
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 14
obstacle_x = random.randint(0, width - obstacle_width)
obstacle_y = -obstacle_height


# Функция для отрисовки игрока
def draw_player(x, y):
    pygame.draw.rect(screen, black, (x, y, player_size, player_size))


# Функция для отрисовки препятствия
def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, (x, y, obstacle_width, obstacle_height))
    x += 50
    y += 50
    pygame.draw.rect(screen, red, (x, y, obstacle_width, obstacle_height))
    x += 50
    y += 50
    pygame.draw.rect(screen, red, (x, y, obstacle_width, obstacle_height))


# Главный игровой цикл
game_over = False
while not game_over:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Движение препятствия
    obstacle_y += obstacle_speed

    # Перезапуск препятствия после выхода за границу
    if obstacle_y > height:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, width - obstacle_width)


    # Логическое выражение для проверки столкновения
    if (player_x < obstacle_x + obstacle_width and
            player_x + player_size > obstacle_x and
            player_y < obstacle_y + obstacle_height and
            player_y + player_size > obstacle_y):
        game_over = True
        print("Игра окончена!")

    # Отрисовка игрока и препятствия
    draw_player(player_x, player_y)
    draw_obstacle(obstacle_x, obstacle_y)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
