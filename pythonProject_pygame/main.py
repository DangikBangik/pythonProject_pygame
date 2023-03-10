from pygame import mixer
import pygame
import enemy_block
import main_menu
import button
import time
import random


pause = False
game_over = False
options = False
p_options = False
bullet_killed = False
her0_invisible = False
game = False
game_win = False
music = True

bullets = []
ultimates = []
enemy_bullets = []
player = []
enemy_m = []
lives = 3
ultimate = 0

vex1 = enemy_block.enemygen()[1] + 105
vey1 = enemy_block.enemygen()[2] + 50

pygame.init()
mixer.init()
size = (1280, 720)
fps = 360
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
mixer.music.load("data/1.mp3")

enemy_health = 1000
start_time = time.time()
start_time1 = time.time()
start_time2 = time.time()

hero2 = pygame.image.load("data/XW1.gif")
hero1 = pygame.image.load("data/XW2.gif")

vx1, vy1 = 0, 620
vx2, vy2 = 580, 620

running = True

# img
resume_img = pygame.image.load("img/Resume.png").convert_alpha()
option_img = pygame.image.load("img/Options.png").convert_alpha()
quit_img = pygame.image.load("img/Quit.png").convert_alpha()
start_img = pygame.image.load("img/Start.png").convert_alpha()
restart_img = pygame.image.load("img/Restart.png").convert_alpha()
back_img = pygame.image.load("img/Back.png").convert_alpha()
b_laser = pygame.image.load("data/b_laser.bmp").convert_alpha()
audio_img = pygame.image.load("img/Audio.png").convert_alpha()
# buttons
resume_button = button.Button(640, 125, resume_img, 1)
option_button = button.Button(550, 200, option_img, 1)
option_button1 = button.Button(640, 200, option_img, 1)
quit_button = button.Button(550, 275, quit_img, 1)
quit_button1 = button.Button(640, 275, quit_img, 1)
start_button = button.Button(550, 125, start_img, 1)
restart_button = button.Button(550, 125, restart_img, 1)
back_button = button.Button(300, 275, back_img, 1)
audio_button = button.Button(300, 200, audio_img, 1)


crash_sound = pygame.mixer.Sound("data/ds.mp3")
game_over_sound = pygame.mixer.Sound("data/game_over.mp3")
main_menu_sound = pygame.mixer.Sound("data/mm.mp3")
game_over_sound.set_volume(0.2)
main_menu_sound.set_volume(0.2)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


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

    def create_ultimate(self):
        return Ultimate(vx2 + 50, vy2)

    def update(self):
        self.rect.center = (vx2 + 54, vy2 + 54)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.image.set_alpha(0)
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

    def create_bullet8(self):
        return EnemyBullet13(vex1 - 30, vey1)

    def create_bullet9(self):
        return EnemyBullet13(vex1 + 30, vey1)

    def create_bullet11(self):
        return EnemyBullet15(vex1 + random.randint(260, 270), 0)

    def create_bullet12(self):
        return EnemyBullet15(vex1 + random.randint(500, 510), 0)

    def create_bullet13(self):
        return EnemyBullet15(vex1 + random.randint(620, 630), 0)

    def create_bullet14(self):
        return EnemyBullet15(vex1 + random.randint(560, 570), 0)

    def create_bullet15(self):
        return EnemyBullet15(vex1 + random.randint(440, 450), 0)

    def create_bullet16(self):
        return EnemyBullet15(vex1 + random.randint(380, 390), 0)

    def create_bullet17(self):
        return EnemyBullet15(vex1 + random.randint(320, 330), 0)

    def create_bullet18(self):
        return EnemyBullet14(vex1 - random.randint(260, 270), 0)

    def create_bullet19(self):
        return EnemyBullet14(vex1 - random.randint(500, 510), 0)

    def create_bullet20(self):
        return EnemyBullet14(vex1 - random.randint(620, 630), 0)

    def create_bullet21(self):
        return EnemyBullet14(vex1 - random.randint(560, 570), 0)

    def create_bullet22(self):
        return EnemyBullet14(vex1 - random.randint(440, 450), 0)

    def create_bullet23(self):
        return EnemyBullet14(vex1 - random.randint(380, 390), 0)

    def create_bullet24(self):
        return EnemyBullet14(vex1 - random.randint(320, 330), 0)

    def create_bullet251(self):
        return EnemyBullet21(1280, vy2)

    def create_bullet252(self):
        return EnemyBullet21(1280, vy2 + 25)

    def create_bullet253(self):
        return EnemyBullet21(1280, vy2 - 25)

    def create_bullet254(self):
        return EnemyBullet21(1280, vy2 + 50)

    def create_bullet255(self):
        return EnemyBullet21(1280, vy2 - 50)

    def create_bullet261(self):
        return EnemyBullet22(0, vy2)

    def create_bullet262(self):
        return EnemyBullet22(0, vy2 + 25)

    def create_bullet263(self):
        return EnemyBullet22(0, vy2 - 25)

    def create_bullet264(self):
        return EnemyBullet22(0, vy2 + 50)

    def create_bullet265(self):
        return EnemyBullet22(0, vy2 - 5)

    def update(self):
        self.rect.center = (vex1, vey1)


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


class Ultimate(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect(center=(ex + 4, ey))
        ultimates.append(self.rect)

    def update(self):
        self.rect.y -= 1.2

        if self.rect.y < 0:
            if self.rect in ultimates:
                ultimate_group.remove(self.rect)
                ultimates.remove(self.rect)
            self.kill()

        if bullet_killed:
            ultimate_group.remove(self.rect)
            ultimates.remove(self.rect)
            self.kill()


class EnemyBullet11(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
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
        if bullet_killed:
            self.kill()


class EnemyBullet12(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
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
        if bullet_killed:
            self.kill()


class EnemyBullet13(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
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
        if bullet_killed:
            self.kill()


class EnemyBullet14(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.y += 1
        self.rect.x += 1
        if self.rect.y > 720:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()
        if bullet_killed:
            self.kill()


class EnemyBullet15(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.y += 1
        self.rect.x -= 1
        if self.rect.y > 720:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()
        if bullet_killed:
            self.kill()


class EnemyBullet21(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.x -= 1
        if self.rect.y < 0:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()
        if bullet_killed:
            self.kill()


class EnemyBullet22(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(ex, ey))
        enemy_bullets.append(self.rect)

    def update(self):
        self.rect.x += 1
        if self.rect.x > 1280:
            if self.rect in enemy_bullets:
                enemyBullet_group.remove(self.rect)
                enemy_bullets.remove(self.rect)
            self.kill()
        if bullet_killed:
            self.kill()


player2 = Hero2()
player_group = pygame.sprite.Group()
player_group.add(player2)

bullet_group = pygame.sprite.Group()

ultimate_group = pygame.sprite.Group()

enemyBullet_group = pygame.sprite.Group()

enemy = Enemy()
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

while running:
    k = 0
    enemies = 0
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()

    if lives < 0:
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_f]:
            bullet_group.add(player2.create_bullet1())
            bullet_group.add(player2.create_bullet2())
            bullet_group.add(player2.create_bullet3())
            bullet_group.add(player2.create_bullet4())
            bullet_group.add(player2.create_bullet5())

        if enemy_health < 900:
            ultimate += 1
        if enemy_health < 800:
            ultimate += 1
        if enemy_health < 700:
            ultimate += 1
        if enemy_health < 600:
            ultimate += 1
        if enemy_health < 500:
            ultimate += 1
        if enemy_health < 400:
            ultimate += 1
        if enemy_health < 300:
            ultimate += 1
        if enemy_health < 50:
            ultimate += 1
        if enemy_health == 1000:
            ultimate = 0

        if keys[pygame.K_l]:
            enemy_health -= 300

        if keys[pygame.K_p]:
            lives = -1

    enemy0 = enemy_block.enemygen()[0]
    x = enemy_block.enemygen()[1]
    y = enemy_block.enemygen()[2]

    for bullet in bullets:
        for enemy in enemy_group:
            if bullet.colliderect(enemy):
                enemy_health -= 0.5
                print(enemy_health)
                bullet_group.remove(bullet)
                bullets.remove(bullet)

    for ult in ultimates:
        for enemy in enemy_group:
            if ult.colliderect(enemy):
                enemy_health -= 50
                print(enemy_health)
                ultimate_group.remove(ult)
                ultimates.remove(ult)

    if time.time() - start_time < 3 and start_time != 0:
        her0_invisible = False

    for e_bullet in enemy_bullets:
        for hero in player_group:
            if e_bullet.colliderect(hero) and time.time() - start_time >= 3:
                start_time = time.time()
                crash_sound.play()
                lives -= 1
                print(lives)
                her0_invisible = True

    for hero1 in player:
        for enemy1 in enemy_m:
            if hero1.colliderect(enemy1) and time.time() - start_time >= 3:
                lives -= 1

    if pause and not main_menu:
        pygame.display.set_caption("Pause Menu")
        if resume_button.draw(screen):
            pause = False
            game = True
        if option_button1.draw(screen):
            pause = False
            p_options = True
            options = True
        if quit_button1.draw(screen):
           running = False
    elif main_menu:
        bullet_killed = False
        main_menu_sound.play(-1)
        lives = 3
        pygame.display.set_caption("Main Menu")
        if start_button.draw(screen):
            main_menu_sound.stop()
            main_menu = False
            game = True
            if music:
                mixer.music.play(-1)
        if option_button.draw(screen):
            main_menu = False
            options = True
        if quit_button.draw(screen):
           running = False
    elif game_over:
        game = False
        pygame.display.set_caption("Game Over")
        bullet_killed = True
        mixer.music.stop()
        if music:
            game_over_sound.play(-1)
        if restart_button.draw(screen):
            bullet_killed = False
            vx2, vy2 = 580, 620
            vex1 = enemy_block.enemygen()[1] + 105
            vey1 = enemy_block.enemygen()[2] + 50
            lives = 3
            enemy_health = 1000
            main_menu = False
            game = True
            game_over_sound.stop()
            if music:
                mixer.music.play(-1)
            game_over = False
        if back_button.draw(screen):
            game_over_sound.stop()
            if music:
                main_menu_sound.play(-1)
            enemy_health = 1000
            lives = 3
            game_over = False
            game = False
            main_menu = True
    elif game_win:
        pygame.display.set_caption("Game Over")
        mixer.music.stop()
        bullet_killed = True
        game_over_sound.play()
        if restart_button.draw(screen):
            lives = 3
            enemy_health = 1000
            main_menu = False
            game = True
            game_over_sound.stop()
            if music:
                mixer.music.play()
            game_over = False
            bullet_killed = False
        if back_button.draw(screen):
            enemy_health = 1000
            lives = 3
            game_over = False
            game = False
            main_menu = True
    elif options and not main_menu:
        pygame.display.set_caption("Options")
        if audio_button.draw(screen):
            if music:
                music = False
            else:
                music = True
        if music and options:
            image954 = pygame.Surface((20, 20))
            image954.fill((0, 255, 0))
            rect954 = image954.get_rect(center=(1150, 50))
            screen.blit(image954, rect954)
        elif not music and options:
            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1150, 50))
            screen.blit(image954, rect954)
        if back_button.draw(screen):
            if p_options:
                pause = True
                options = False
                p_options = False
            else:
                main_menu = True
                options = False

    elif game:

        if keys[pygame.K_a] and vx2 > -15:
            if lives == 3:
                vx2 -= 1.2
                if enemy_health >= 0:
                    vex1 -= 1.2
            elif lives == 2:
                vx2 -= 1.3
                if enemy_health >= 0:
                    vex1 -= 1.3
            else:
                vx2 -= 1.5
                if enemy_health >= 0:
                    vex1 -= 1.5
            if keys[pygame.K_g]:
                if enemy_health >= 0:
                    vex1 += 0.4
                vx2 += 0.4
        if keys[pygame.K_d] and vx2 < 1180:
            if lives == 3:
                if enemy_health >= 0:
                    vex1 += 1.2
                vx2 += 1.2
            elif lives == 2:
                if enemy_health >= 0:
                    vex1 += 1.3
                vx2 += 1.3
            else:
                if enemy_health >= 0:
                    vex1 += 1.5
                vx2 += 1.5
            if keys[pygame.K_g]:
                if enemy_health >= 0:
                    vex1 -= 0.4
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
        if keys[pygame.K_s] and vy2 < 633:
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
        if keys[pygame.K_r]:
            pause = False
            options = False
            main_menu = False
        if keys[pygame.K_t]:
            fps = 60
        else:
            fps = 360

        if time.time() - start_time1 >= 2:
            start_time1 = time.time()

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
                enemyBullet_group.add(enemy.create_bullet8())
                enemyBullet_group.add(enemy.create_bullet9())
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
                enemyBullet_group.add(enemy.create_bullet8())
                enemyBullet_group.add(enemy.create_bullet9())
        elif enemy_health > 300:
            if 1 <= time.time() - start_time1 <= 2:
                start_time1 = time.time()
                enemyBullet_group.add(enemy.create_bullet1())
                enemyBullet_group.add(enemy.create_bullet2())
                enemyBullet_group.add(enemy.create_bullet3())
                enemyBullet_group.add(enemy.create_bullet4())
                enemyBullet_group.add(enemy.create_bullet5())
                enemyBullet_group.add(enemy.create_bullet7())
                enemyBullet_group.add(enemy.create_bullet9())
                enemyBullet_group.add(enemy.create_bullet11())
                enemyBullet_group.add(enemy.create_bullet12())
                enemyBullet_group.add(enemy.create_bullet13())
                enemyBullet_group.add(enemy.create_bullet14())
                enemyBullet_group.add(enemy.create_bullet15())
                enemyBullet_group.add(enemy.create_bullet16())
                enemyBullet_group.add(enemy.create_bullet17())
                enemyBullet_group.add(enemy.create_bullet18())
                enemyBullet_group.add(enemy.create_bullet19())
                enemyBullet_group.add(enemy.create_bullet20())
                enemyBullet_group.add(enemy.create_bullet21())
                enemyBullet_group.add(enemy.create_bullet22())
                enemyBullet_group.add(enemy.create_bullet23())
                enemyBullet_group.add(enemy.create_bullet24())
        else:
            if 1 <= time.time() - start_time1 <= 2:
                start_time1 = time.time()
                enemyBullet_group.add(enemy.create_bullet1())
                enemyBullet_group.add(enemy.create_bullet2())
                enemyBullet_group.add(enemy.create_bullet3())
                enemyBullet_group.add(enemy.create_bullet4())
                enemyBullet_group.add(enemy.create_bullet5())
                enemyBullet_group.add(enemy.create_bullet7())
                enemyBullet_group.add(enemy.create_bullet9())
                enemyBullet_group.add(enemy.create_bullet11())
                enemyBullet_group.add(enemy.create_bullet12())
                enemyBullet_group.add(enemy.create_bullet13())
                enemyBullet_group.add(enemy.create_bullet14())
                enemyBullet_group.add(enemy.create_bullet15())
                enemyBullet_group.add(enemy.create_bullet16())
                enemyBullet_group.add(enemy.create_bullet17())
                enemyBullet_group.add(enemy.create_bullet18())
                enemyBullet_group.add(enemy.create_bullet19())
                enemyBullet_group.add(enemy.create_bullet20())
                enemyBullet_group.add(enemy.create_bullet21())
                enemyBullet_group.add(enemy.create_bullet22())
                enemyBullet_group.add(enemy.create_bullet23())
                enemyBullet_group.add(enemy.create_bullet24())
                enemyBullet_group.add(enemy.create_bullet251())
                enemyBullet_group.add(enemy.create_bullet252())
                enemyBullet_group.add(enemy.create_bullet261())
                enemyBullet_group.add(enemy.create_bullet262())


        if ultimate <= 0:
            hero2 = pygame.image.load("data/XW1.gif")
        else:
            hero2 = pygame.image.load("data/XW2.gif")

        pygame.display.set_caption("Game")
        enemies += 1

        if enemy_health > 0:
            image954 = pygame.Surface((enemy_health, 15))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(640, 0))
            screen.blit(image954, rect954)

        if lives == 3:
            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1150, 50))
            screen.blit(image954, rect954)

            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1180, 50))
            screen.blit(image954, rect954)

            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1210, 50))
            screen.blit(image954, rect954)
        elif lives == 2:
            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1150, 50))
            screen.blit(image954, rect954)

            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1180, 50))
            screen.blit(image954, rect954)
        elif lives == 1:
            image954 = pygame.Surface((20, 20))
            image954.fill((255, 0, 0))
            rect954 = image954.get_rect(center=(1150, 50))
            screen.blit(image954, rect954)

        player_group.draw(screen)
        bullet_group.draw(screen)
        ultimate_group.draw(screen)
        enemy_group.draw(screen)
        enemyBullet_group.draw(screen)

        player_group.update()
        bullet_group.update()
        ultimate_group.update()
        enemy_group.update()
        enemyBullet_group.update()

        screen.blit(enemy0, (vex1 - 50, vey1 - 45))
        screen.blit(hero2, (vx2, vy2))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
