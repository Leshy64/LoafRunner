import pygame

_ = pygame.init()
screen = pygame.display.set_mode((1000, 800))

isRunning = True

# Player
loafX: float = 100.0
loafY: float = 500.0
baseY: float = 500.0
loaf = pygame.image.load("res/loaf.png")
loaf = pygame.transform.scale(loaf, (270, 160))

pygame.display.set_icon(loaf)
pygame.display.set_caption("Loaf runner")

# Speed vars
speed: float = -2000.0
velocity: float = 0
g: float = 9.8


# Player movement
def isOnGround(y: float) -> bool:
    global loafY
    return y == baseY


def isntNearGround(y: float, v: float) -> bool:
    global baseY
    return baseY - y >= v


def velocityCalc(y: float, v: float) -> float:
    global g
    global loafY
    if not isOnGround(y):
        v += g
        print(f"Velocity: {v}")
    if not isntNearGround(y, v):
        v = baseY - y
        print(f"Velocity: {v}")
    return v


def movePlayer(y: float) -> None:
    global velocity
    global loafY
    velocity = velocityCalc(y, velocity)
    loafY += velocity
    _ = screen.blit(loaf, (loafX, loafY))


clock = pygame.time.Clock()
while isRunning:
    _ = screen.fill((0, 0, 0))
    dt_ms = clock.tick(32)
    dt = dt_ms / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and isOnGround(loafY):
            velocity = speed * dt
    movePlayer(loafY)
    pygame.display.flip()
