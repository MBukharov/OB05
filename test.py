import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
MONSTER_WIDTH, MONSTER_HEIGHT = 50, 50
MONSTER_SPEED = 5

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Monsters")

# Загрузка изображения монстра
monster_image = pygame.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
#monster_image.fill((255, 0, 0))  # Замените это на загрузку реального изображения, например:
#monster_image = pygame.image.load('img/m1.png').convert_alpha()

class Monster:
    def __init__(self,image):
        self.x = random.randint(0, WIDTH - MONSTER_WIDTH)
        self.y = -MONSTER_HEIGHT
        self.image = image

    def update(self):
        self.y += MONSTER_SPEED

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

list_of_monsters = []
for i in range(1,12):
    list_of_monsters.append(f"img/m{i}.png")

class Hero:
    def __init__(self,image):
        self.x = int(WIDTH/2 - HERO_WIDTH/2)
        self.y = HEIGHT - HERO_HEIGHT - 20
        self.image = image
        self.visible = True
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

hero = Hero(pygame.image.load("img/hero.png"))

def main():
    clock = pygame.time.Clock()
    monsters = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Добавление нового монстра
        if random.randint(1, 10) == 1:
            monster_number = random.randint(0, len(list_of_monsters) - 1)
            monsters.append(Monster(pygame.image.load(list_of_monsters[monster_number]).convert_alpha()))

        # Обновление положения монстров
        for monster in monsters[:]:
            monster.update()
            if monster.y > HEIGHT:
                monsters.remove(monster)

        # Отрисовка
        screen.fill((0, 0, 0))  # Очистка экрана
        for monster in monsters:
            monster.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
   main()