import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
MONSTER_WIDTH, MONSTER_HEIGHT = 60, 60
HERO_WIDTH, HERO_HEIGHT = 70, 70
MONSTER_SPEED = 5

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Выживи среди монстров")

# Загрузка изображения монстра
#monster_image = pygame.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
#monster_image.fill((255, 0, 0))  # Замените это на загрузку реального изображения, например:
# monster_image = pygame.image.load('monster.png').convert_alpha()

class Monster:
    def __init__(self,image):
        self.x = random.randint(0, WIDTH - MONSTER_WIDTH)
        self.y = -2*MONSTER_HEIGHT
        self.image = image
    def update(self):
        self.y += MONSTER_SPEED
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Hero:
    def __init__(self,image):
        self.x = int(WIDTH/2 - HERO_WIDTH/2)
        self.y = HEIGHT - HERO_HEIGHT - 50
        self.image = image
        self.visible = True
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


list_of_monster_images = []
for i in range(1,12):
    list_of_monster_images.append(pygame.image.load(f"img/m{i}.png").convert_alpha())

hero = Hero(pygame.image.load("img/hero.png"))
game_over_image = pygame.image.load("img/gameover.png").convert_alpha()

monsters = []

def draw_game_over_screen(seconds_survived):
    screen.fill((0, 0, 0))
    screen.blit(game_over_image,
                (WIDTH // 2 - game_over_image.get_width() // 2, HEIGHT // 2 - game_over_image.get_height() // 2 - 50))

    font = pygame.font.SysFont(None, 48)
    text = font.render(f"Время выживания: {seconds_survived} секунд", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 50))

    button_font = pygame.font.SysFont(None, 36)
    button_text = button_font.render("Restart", True, (255, 255, 255))
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)
    pygame.draw.rect(screen, (0, 128, 0), button_rect)
    screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                              button_rect.y + (button_rect.height - button_text.get_height()) // 2))

    pygame.display.flip()

    return button_rect

def main():
    clock = pygame.time.Clock()
    run = True
    game_over = False
    start_ticks = pygame.time.get_ticks()  # Запоминаем начальное время

    while run:
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Обновляем счетчик времени
            seconds_survived = (pygame.time.get_ticks() - start_ticks) // 1000

            # Добавление нового монстра
            if random.randint(1, 25) == 1:
                monster_number = random.randint(0, len( list_of_monster_images) - 1)
                monsters.append(Monster( list_of_monster_images[monster_number]))

            # Обновление положения монстров
            for monster in monsters[:]:
                monster.update()
                if monster.y > HEIGHT:
                    monsters.remove(monster)

            #Перемещение героя
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and hero.x > 0:
                hero.x -= 5
            if keys[pygame.K_RIGHT] and hero.x < WIDTH - HERO_WIDTH:
                hero.x += 5
            if keys[pygame.K_UP] and hero.y > 0:
                hero.y -= 5
            if keys[pygame.K_DOWN] and hero.y < HEIGHT - HERO_HEIGHT:
                hero.y += 5

            #Обработка столкновения монстров

            for monster in monsters[:]:
                if hero.x < monster.x + MONSTER_WIDTH and hero.x + HERO_WIDTH > monster.x and hero.y < monster.y + MONSTER_HEIGHT and hero.y + HERO_HEIGHT > monster.y:
                    game_over = True

            # Отрисовка
            screen.fill((200, 200, 200))  # Очистка экрана
            for monster in monsters:
                monster.draw(screen)

            hero.draw(screen)

            # Отображение счета
            font = pygame.font.SysFont(None, 36)
            text = font.render(f"Время выживания: {seconds_survived} секунд", True, (0, 0, 0))
            screen.blit(text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)
        else:
            button_rect = draw_game_over_screen(seconds_survived)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        monsters.clear()
                        hero.x = int(WIDTH / 2 - HERO_WIDTH / 2)
                        hero.y = HEIGHT - HERO_HEIGHT - 50
                        start_ticks = pygame.time.get_ticks()
                        game_over = False


if __name__ == "__main__":
    main()