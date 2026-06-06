import pygame

_ = pygame.init()

screen = pygame.display.set_mode((1000, 800))

isRunning = True

# Player
y: int = 600
dino = pygame.Rect(480, y, 60, 60)
# Speed vars
speed: float = -1500.0
velocity: float = 0
g: float = 9.8


def isOnGround(y: float) -> bool:
    return y == 600.0


def isntNearGround(y: float, v: float) -> bool:
    return 600 - y >= v


def velocityCalc(y: float, v: float) -> float:
    if not isOnGround(dino.y):
        v += g
    if not isntNearGround(dino.y, v):
        v = 600 - dino.y
    return v


clock = pygame.time.Clock()
while isRunning:
    _ = screen.fill((0, 0, 0))
    dt_ms = clock.tick(32)
    dt = dt_ms / 1000.0
    _ = pygame.draw.rect(screen, (225, 225, 225), dino)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and isOnGround(dino.y):
            velocity = speed * dt
    velocity = velocityCalc(dino.y, velocity)
    dino.move_ip(0, velocity)
    pygame.display.flip()
