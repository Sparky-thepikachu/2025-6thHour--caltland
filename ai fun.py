










import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodging Game")

# Set clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Car settings
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 7

# Obstacle settings
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 7
obstacles = []

# Font
font = pygame.font.SysFont(None, 48)

def draw_car(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, car_width, car_height))

def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

def show_text(text, color, y_offset=0):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(WIDTH//2, HEIGHT//2 + y_offset))
    screen.blit(render, rect)

def game_loop():
    global car_x

    obstacles.clear()
    score = 0
    running = True
    game_over = False
    obstacle_timer = 0

    while running:
        clock.tick(FPS)
        screen.fill(GRAY)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
            car_x += car_speed

        # Create obstacles
        obstacle_timer += 1
        if obstacle_timer > 30:
            x_pos = random.randint(0, WIDTH - obstacle_width)
            obstacles.append(pygame.Rect(x_pos, -obstacle_height, obstacle_width, obstacle_height))
            obstacle_timer = 0

        # Move and remove obstacles
        for obs in list(obstacles):
            obs.y += obstacle_speed
            if obs.y > HEIGHT:
                obstacles.remove(obs)
                score += 1

        # Collision detection
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        for obs in obstacles:
            if car_rect.colliderect(obs):
                game_over = True

        # Draw
        draw_car(car_x, car_y)
        draw_obstacles(obstacles)

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Game over
        if game_over:
            show_text("GAME OVER", RED)
            show_text(f"Score: {score}", WHITE, 60)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        pygame.display.flip()

    pygame.quit()

game_loop()