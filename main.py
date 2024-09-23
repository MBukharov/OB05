import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
MONSTER_WIDTH, MONSTER_HEIGHT = 80, 80
HERO_WIDTH, HERO_HEIGHT = 100, 100
MONSTER_SPEED = 5

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Monsters")

# Загрузка изображения монстра
monster_image = pygame.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
#monster_image.fill((255, 0, 0))  # Замените это на загрузку реального изображения, например:
# monster_image = pygame.image.load('monster.png').convert_alpha()

class Monster:
    def __init__(self,image):
        self.x = random.randint(0, WIDTH - MONSTER_WIDTH)
        self.y = -2*MONSTER_HEIGHT
        self.image = image
        self.visible = False
    def update(self):
        self.y += MONSTER_SPEED
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Hero:
    def __init__(self,image):
        self.x = int(WIDTH/2 - HERO_WIDTH/2)
        self.y = HEIGHT - HERO_HEIGHT - 20
        self.image = image
        self.visible = True
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


monsters = []
for i in range(1,12):
    monster = Monster(pygame.image.load(f"img/m{i}.png"))
    monsters.append(monster)

hero = Hero(pygame.image.load("img/hero.png"))

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Добавление нового монстра
        if random.randint(1, 20) == 1:
            monster_number = random.randint(0, len(monsters) - 1)
            monsters[monster_number].visible = True

        # Обновление положения монстров
        for monster in monsters[:]:
            if monster.visible:
                monster.update()
            if monster.y > HEIGHT:
                monster.visible = False
                monster.y = -2*MONSTER_HEIGHT

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

        # Отрисовка
        screen.fill((200, 200, 200))  # Очистка экрана
        for monster in monsters:
            monster.draw(screen)

        hero.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()