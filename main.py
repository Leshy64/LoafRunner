import pygame

_ = pygame.init()
screen = pygame.display.set_mode((1000, 800))

isRunning = True

# Background
bg = pygame.image.load("res/bg1.png")
bg = pygame.transform.scale(bg, (1000, 570))
road = pygame.image.load("res/road.png")
road = pygame.transform.scale(road, (1000, 230))
bgX: float = 0
bgSpeed: float = 17


def moveBackground() -> None:
    global bgX
    bgX -= bgSpeed
    _ = screen.blit(bg, (bgX, 0))
    _ = screen.blit(bg, (bgX + 1000, 0))
    _ = screen.blit(road, (bgX, 570))
    _ = screen.blit(road, (bgX + 1000, 570))
    if bgX <= -1000:
        bgX = 0


# Player
loafX: float = 100.0
loafY: float = 500.0
baseY: float = 500.0
loaf = pygame.image.load("res/loaf.png")
loaf = pygame.transform.scale(loaf, (270, 160))
loaf_rect = loaf.get_rect(topleft=(0, 0))
loaf_inflX = -20
loaf_inflY = -10
loaf_hitbox = loaf_rect.inflate(loaf_inflX, loaf_inflY)

pygame.display.set_icon(loaf)
pygame.display.set_caption("Loaf runner")

# Speed vars
loafJump: float = -2000.0
velocity: float = 0
g: float = 5.0


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
    loaf_rect.topleft = (100, round(loafY))
    loaf_hitbox.topleft = (100 - loaf_inflX, round(loafY) - loaf_inflY)
    # _ = pygame.draw.rect(screen, (0, 255, 0), loaf_hitbox, 2)
    _ = screen.blit(loaf, loaf_rect)


# Enemy
volk = pygame.image.load("res/volk.png")
volk = pygame.transform.scale(volk, (280, 130))
volkX: int = 1100
volkSpeed: int = round(bgSpeed + 8.0)
volk_rect = volk.get_rect(topleft=(600, 0))
volk_inflX: int = -40
volk_inflY: int = -20
volk_hitbox = volk_rect.inflate(volk_inflX, volk_inflY)


def moveEnemy() -> None:
    global volkX
    global bgSpeed
    volkX -= volkSpeed
    volk_rect.topleft = (volkX, 530)
    volk_hitbox.topleft = (volkX - volk_inflX - 10, 530 - volk_inflX)
    _ = screen.blit(volk, (volkX, 530))
    _  #  = pygame.draw.rect(screen, (0, 255, 0), volk_hitbox, 2)
    if volkX <= -280:
        volkX = 1100


def gameOver():
    global isRunning
    isRunning = False


clock = pygame.time.Clock()
while isRunning:
    # _ = screen.fill((0, 0, 0))
    dt_ms = clock.tick(32)
    dt = dt_ms / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and isOnGround(loafY):
            velocity = loafJump * dt
    if loaf_hitbox.colliderect(volk_hitbox):
        print("hit")
        gameOver()
    moveBackground()
    moveEnemy()
    movePlayer(loafY)
    pygame.display.flip()
