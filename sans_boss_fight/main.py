import pygame
import os

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sans Boss Fight")

# Load images
assets_path = os.path.join("assets", "images")
sans_img = pygame.image.load(os.path.join(assets_path, "sans.png"))
heart_img = pygame.image.load(os.path.join(assets_path, "heart.png"))
sans_img = pygame.transform.scale(sans_img, (100, 100))
heart_img = pygame.transform.scale(heart_img, (32, 32))

# Heart position
heart_x = WIDTH // 2
heart_y = HEIGHT - 100
speed = 5

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        heart_x -= speed
    if keys[pygame.K_RIGHT]:
        heart_x += speed
    if keys[pygame.K_UP]:
        heart_y -= speed
    if keys[pygame.K_DOWN]:
        heart_y += speed

    screen.fill((0, 0, 0))
    screen.blit(sans_img, (WIDTH // 2 - 50, 50))
    screen.blit(heart_img, (heart_x, heart_y))
    pygame.display.flip()

pygame.quit()
