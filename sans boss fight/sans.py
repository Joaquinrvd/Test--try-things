import pygame
import random
import os

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sans Boss Fight")

# Load Assets
ASSET = lambda name: os.path.join("assets", name)

player_img = pygame.image.load(ASSET("player.png"))
sans_img = pygame.image.load(ASSET("sans.png"))
bone_img = pygame.image.load(ASSET("bone.png"))
blaster_img = pygame.image.load(ASSET("gaster_blaster.png"))

hit_sound = pygame.mixer.Sound(ASSET("hit.wav"))
blast_sound = pygame.mixer.Sound(ASSET("blaster.wav"))
pygame.mixer.music.load(ASSET("megalo.ogg"))

font = pygame.font.Font(ASSET("font.ttf"), 24)

# Game Constants
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game Objects
player = pygame.Rect(WIDTH//2, HEIGHT-80, 30, 30)
bones = []
blasters = []
health = 100

clock = pygame.time.Clock()
pygame.mixer.music.play(-1)

# Functions
def spawn_bone():
    x = random.randint(0, WIDTH-30)
    bones.append(pygame.Rect(x, 0, 10, 40))

def spawn_blaster():
    y = random.randint(100, HEIGHT-100)
    blasters.append(pygame.Rect(WIDTH, y, 60, 40))

def draw_window():
    screen.fill((0, 0, 0))
    screen.blit(sans_img, (WIDTH//2 - 45, 10))
    screen.blit(player_img, player)

    for bone in bones:
        screen.blit(bone_img, bone)

    for blaster in blasters:
        screen.blit(blaster_img, blaster)

    # Health Bar
    pygame.draw.rect(screen, RED, (10, 10, health * 2, 20))
    health_text = font.render(f"HP: {health}", True, WHITE)
    screen.blit(health_text, (10, 35))

    if health <= 0:
        game_over_text = font.render("YOU DIED", True, RED)
        screen.blit(game_over_text, (WIDTH//2 - 60, HEIGHT//2))

    pygame.display.update()

# Main Game Loop
run = True
frame = 0

while run:
    clock.tick(FPS)
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 4
    if keys[pygame.K_RIGHT]: player.x += 4
    if keys[pygame.K_UP]: player.y -= 4
    if keys[pygame.K_DOWN]: player.y += 4

    # Clamp position
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    # Spawn Attacks
    if frame % 30 == 0: spawn_bone()
    if frame % 90 == 0:
        spawn_blaster()
        blast_sound.play()

    # Move Bones
    for bone in bones:
        bone.y += 6
        if bone.colliderect(player):
            hit_sound.play()
            health -= 5
            bones.remove(bone)

    bones = [b for b in bones if b.y < HEIGHT]

    # Move Blasters
    for blaster in blasters:
        blaster.x -= 10
        if blaster.colliderect(player):
            hit_sound.play()
            health -= 10
            blasters.remove(blaster)

    blasters = [b for b in blasters if b.x > -60]

    draw_window()

pygame.quit()
