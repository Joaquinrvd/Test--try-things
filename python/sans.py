import pygame
import random
import sys

# === Initialize Pygame ===
pygame.init()

# === Screen Setup ===
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sans Boss Fight")

# === Clock ===
clock = pygame.time.Clock()
FPS = 60

# === Colors ===
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GREY = (180, 180, 180)

# === Font ===
font = pygame.font.SysFont("comicsans", 30)

# === Player Box ===
player = pygame.Rect(300, 400, 40, 40)
player_speed = 5
hp = 100

# === Bone Attack Class ===
class Bone:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 20), -40, 20, 60)
        self.speed = random.randint(4, 8)

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# === Blaster Attack Class ===
class Blaster:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(100, WIDTH - 100), -100, 40, 120)
        self.timer = 60  # delay before firing
        self.fire = False

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.fire = True
            self.rect.height = 300

    def draw(self, surface):
        color = BLUE if self.fire else GREY
        pygame.draw.rect(surface, color, self.rect)

# === Game Variables ===
bones = []
blasters = []
spawn_bone_timer = 0
spawn_blasters_timer = 0
game_over = False

# === Game Loop ===
running = True
while running:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # === Move Player ===
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
            player.x += player_speed
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.y < HEIGHT - player.height:
            player.y += player_speed

        # === Spawn Bones ===
        spawn_bone_timer += 1
        if spawn_bone_timer > 15:
            bones.append(Bone())
            spawn_bone_timer = 0

        # === Spawn Blasters ===
        spawn_blasters_timer += 1
        if spawn_blasters_timer > 180:
            blasters.append(Blaster())
            spawn_blasters_timer = 0

        # === Update Bones ===
        for bone in bones[:]:
            bone.update()
            if bone.rect.top > HEIGHT:
                bones.remove(bone)
            elif bone.rect.colliderect(player):
                bones.remove(bone)
                hp -= 10

        # === Update Blasters ===
        for blaster in blasters[:]:
            blaster.update()
            if blaster.rect.top > HEIGHT:
                blasters.remove(blaster)
            elif blaster.fire and blaster.rect.colliderect(player):
                hp -= 20
                blasters.remove(blaster)

        # === Game Over Check ===
        if hp <= 0:
            game_over = True

        # === Draw Everything ===
        pygame.draw.rect(screen, BLUE, player)
        for bone in bones:
            bone.draw(screen)
        for blaster in blasters:
            blaster.draw(screen)

        # === Draw HP ===
        hp_text = font.render(f"HP: {hp}", True, RED)
        screen.blit(hp_text, (10, 10))

    else:
        over_text = font.render("GAME OVER! Press ESC to quit", True, RED)
        screen.blit(over_text, (WIDTH//2 - 160, HEIGHT//2))
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()