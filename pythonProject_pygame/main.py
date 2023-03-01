import pygame
import enemy_block
import main_menu
import button
import time
import random


pause = False
options = False
bullet_killed = False
her0_invisible = False

bullets = []
enemy_bullets = []
player = []
enemy_m = []
lives = 3

vex1 = enemy_block.enemygen()[1] + 50
vey1 = enemy_block.enemygen()[2] + 50

pygame.init()
size = (1280, 720)
fps = 360
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

enemy_health = 1000
start_time = time.time()
start_time1 = time.time()

hero1 = pygame.image.load("data/XW1.gif")
hero2 = pygame.image.load("data/XW2.gif")

vx1, vy1 = 0, 620
vx2, vy2 = 580, 620

running = True

# img
resume_img = pygame.image.load("img/Resume.png").convert_alpha()
option_img = pygame.image.load("img/Options.png").convert_alpha()
quit_img = pygame.image.load("img/Quit.png").convert_alpha()
start_img = pygame.image.load("img/Start.png").convert_alpha()
back_img = pygame.image.load("img/Back.png").convert_alpha()
# buttons
resume_button = button.Button(640, 125, resume_img, 1)
option_button = button.Button(640, 200, option_img, 1)
quit_button = button.Button(640, 275, quit_img, 1)
start_button = button.Button(550, 125, start_img, 1)
back_button = button.Button(640, 275, back_img, 1)


class Hero2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(vx2, vy2))
        player.append(self.rect)

    def create_bullet1(self):
        return hero2Bullet1(vx2 + 50, vy2)

    def create_bullet2(self):
        return hero2Bullet1(vx2, vy2)

    def create_bullet3(self):
        return hero2Bullet1(vx2 + 25, vy2)

    def create_bullet4(self):
        return hero2Bullet1(vx2 + 75, vy2)

    def create_bullet5(self):
        return hero2Bullet1(vx2 + 100, vy2)

    def update(self):
        self.rect.center = (vx2 + 54, vy2 + 54)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(vex1, vey1))
        enemy_m.append(self.rect)

    def create_bullet1(self):
        return EnemyBullet11(vex1, vey1)

    def create_bullet2(self):
        return EnemyBullet11(vex1 + 30, vey1)

    def create_bullet3(self):
        return EnemyBullet11(vex1 - 30, vey1)

    def create_bullet4(self):
        return EnemyBullet11(vex1 + 60, vey1)

    def create_bullet5(self):
        return EnemyBullet11(vex1 - 60, vey1)

    def create_bullet6(self):
        return EnemyBullet12(vex1 - 30, vey1)

    def create_bullet7(self):
        return EnemyBullet12(vex1 + 30, vey1)

    def update(self):
        if enemy_health > 700:
            self.rect.center = (vex1, vey1)
        else:
            self.rect.center = (enemy_block.enemygen()[1] + 50, enemy_block.enemygen()[2] + 50)


class hero2Bullet1(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((5, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(ex + 4, ey))
        bullets.append(self.rect)

    def update(self):
        self.rect.y -= 1.2

        if self.rect.y < 0:
            if self.rect in bullets:
                bullet_group.remove(self.rect)
                bullets.remove(self.rect)
            self.kill()

        if bullet_killed:
            bullet_group.remove(self.rect)
            bullets.remove(self.rect)
            self.kill()


class EnemyBullet11(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.y -= -1

        if self.rect.y > 720:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()


class EnemyBullet12(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.y -= -1
        self.rect.x += 1
        if self.rect.y > 720:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()


class EnemyBullet13(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((5, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.y -= -1
        self.rect.x -= 1
        if self.rect.y > 720:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()


player2 = Hero2()
player_group = pygame.sprite.Group()
player_group.add(player2)

bullet_group = pygame.sprite.Group()

enemyBullet_group = pygame.sprite.Group()

enemy = Enemy()
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

while running:
    k = 0
    enemies = 0
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_f]:
            bullet_group.add(player2.create_bullet1())
            bullet_group.add(player2.create_bullet2())
            bullet_group.add(player2.create_bullet3())
            bullet_group.add(player2.create_bullet4())
            bullet_group.add(player2.create_bullet5())

    enemy0 = enemy_block.enemygen()[0]
    x = enemy_block.enemygen()[1]
    y = enemy_block.enemygen()[2]

    for bullet in bullets:
        for enemy in enemy_group:
            if bullet.colliderect(enemy):
                enemy_health -= 0.1
                print(enemy_health)
                bullet_group.remove(bullet)
                bullets.remove(bullet)
    if time.time() - start_time < 3 and start_time != 0:
        her0_invisible = False

    for e_bullet in enemy_bullets:
        for hero in player_group:
            if e_bullet.colliderect(hero) and time.time() - start_time >= 3:
                start_time = time.time()

                lives -= 1
                print(lives)
                her0_invisible = True
                vx2, vy2 = vex1, 620

    for hero1 in player:
        for enemy1 in enemy_m:
            if hero1.colliderect(enemy1) and time.time() - start_time >= 3:
                lives -= 1
                vex1 = 540
                vx2, vy2 = 540, 620

    if pause and not main_menu:
        pygame.display.set_caption("Pause Menu")
        if resume_button.draw(screen):
            pause = False
        if option_button.draw(screen):
            pause = False
            options = True
        if quit_button.draw(screen):
           running = False
    elif main_menu:
        pygame.display.set_caption("Main Menu")
        if start_button.draw(screen):
            main_menu = False
        if option_button.draw(screen):
            main_menu = False
            options = True
    elif options:
        pygame.display.set_caption("Options")
        if back_button.draw(screen):
            options = False
            main_menu = True

    else:

        if keys[pygame.K_a] and vx2 > -15:
            if lives == 3:
                vx2 -= 1.2
                if enemy_health > 700:
                    vex1 -= 1.2
            elif lives == 2:
                vx2 -= 1.3
                if enemy_health > 700:
                    vex1 -= 1.3
            else:
                vx2 -= 1.5
                if enemy_health > 700:
                    vex1 -= 1.3
            if keys[pygame.K_g]:
                vx2 += 0.4
        if keys[pygame.K_d] and vx2 < 1180:
            if lives == 3:
                if enemy_health > 700:
                    vex1 += 1.2
                vx2 += 1.2
            elif lives == 2:
                if enemy_health > 700:
                    vex1 += 1.3
                vx2 += 1.3
            else:
                if enemy_health > 700:
                    vex1 += 1.3
                vx2 += 1.5
            if keys[pygame.K_g]:
                vx2 -= 0.4
        if keys[pygame.K_w] and vy2 > 0:
            if lives == 3:

                vy2 -= 1.2
            elif lives == 2:
                vy2 -= 1.3
            else:
                vy2 -= 1.5
            if keys[pygame.K_g]:
                vy2 += 0.4
        if keys[pygame.K_s] and vy2 < 700:
            if lives == 3:
                vy2 += 1.2
            elif lives == 2:
                vy2 += 1.3
            else:
                vy2 += 1.5
            if keys[pygame.K_g]:
                vy2 -= 0.4
        if keys[pygame.K_SPACE]:
            pause = True
        if enemy_health > 950:
            if 1 <= time.time() - start_time1 <= 2:
                start_time1 = time.time()
                enemyBullet_group.add(enemy.create_bullet1())
                enemyBullet_group.add(enemy.create_bullet2())
                enemyBullet_group.add(enemy.create_bullet3())
                enemyBullet_group.add(enemy.create_bullet4())
                enemyBullet_group.add(enemy.create_bullet5())
                enemyBullet_group.add(enemy.create_bullet6())
                enemyBullet_group.add(enemy.create_bullet7())
        elif enemy_health > 700:
            if 0.5 <= time.time() - start_time1 <= 1:
                start_time1 = time.time()
                enemyBullet_group.add(enemy.create_bullet1())
                enemyBullet_group.add(enemy.create_bullet2())
                enemyBullet_group.add(enemy.create_bullet3())
                enemyBullet_group.add(enemy.create_bullet4())
                enemyBullet_group.add(enemy.create_bullet5())
                enemyBullet_group.add(enemy.create_bullet6())
                enemyBullet_group.add(enemy.create_bullet7())
        pygame.display.set_caption("Game")
        enemies += 1

        player_group.draw(screen)
        bullet_group.draw(screen)
        enemy_group.draw(screen)
        enemyBullet_group.draw(screen)

        player_group.update()
        bullet_group.update()
        enemy_group.update()
        enemyBullet_group.update()

        screen.blit(enemy0, (vex1, vey1))
        screen.blit(hero2, (vx2, vy2))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
