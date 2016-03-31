import pygame
import os
from pygame.locals import *


def levelOne():
    winWidth = 960
    winHeight = 540
    halfWidth = int(winWidth / 2)
    halfHeight = int(winHeight / 2)
    displaySize = (winWidth, winHeight)
    cameraSlack = 30
    fps = 30
    fpsTime = pygame.time.Clock()
    pygame.mixer.music.load(os.path.join('.', 'bin', 'InThere.wav'))
    pygame.mixer.music.play(-1, 0.0)

    white = (255, 255, 255)
    darkGray = (25, 25, 25)
    lightGray = (200, 200, 200)
    black = (0, 0, 0)
    grayBlue = (24, 79, 94)
    darkBlue = (54, 53, 151)
    darkGreen = (0, 133, 3)
    darkPurple = (74, 0, 121)
    darkRed = (136, 9, 0)

    def main():
        pygame.init()
        screen = pygame.display.set_mode(displaySize, FULLSCREEN)
        pygame.display.set_caption("Level N/A")
        up = down = left = right = False
        bg = pygame.image.load(os.path.join('.', 'bin', 'Cave Backdrop.png')).convert_alpha()
        bg = pygame.Surface((32,32))
        bg.convert()
        bg.fill((5, 5, 5))
        entities = pygame.sprite.Group()
        player = Player(32, 32)
        platforms = []
        x = y = 0

        level = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "P                                          P",
            "P     yay, alpha!              E           P",
            "P   unstable stuff is fun!     E           P",
            "P                    PPPPPPPPPPP           P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P    PPPPPPPP                              P",
            "P            P                             P",
            "P             P            PPPPPPP         P",
            "P              PPPPPPPPP                   P",
            "P                                          P",
            "P         PPPPPPP                          P",
            "P        PPP                               P",
            "P       PPPP          PPPPPP               P",
            "P                                          P",
            "P   PPPPPPPPPPP             E              P",
            "P                           E              P",
            "P                 PPPPPPPPPPP              P",
            "P                PPPPPPPPPPPP              P",
            "P               PPPPPPPPPPPPP              P",
            "P          PPPPPPPPPPPPPPPPPP              P",
            "P                                          P",
            "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"]

        # build the level
        for row in level:
            for block in row:
                if block == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if block == "F":
                    f = Platform(x, y)
                    f.isFloor = True
                    platforms.append(f)
                    entities.add(f)
                if block == "E":
                    e = ExitBlock(x, y)
                    platforms.append(e)
                    entities.add(e)
                x += 32
            y += 32
            x = 0
        totalLevelWidth  = len(level[0])*32
        totalLevelHeight = len(level)*32
        camera = Camera(complexCamera, totalLevelWidth, totalLevelHeight)
        entities.add(player)

        while True:
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("Goodbye!")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("Escape key pressed. See ya later!")
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
            # draw background
            for y in range(32):
                for x in range(32):
                    screen.blit(bg, (x * 32, y * 32))
            camera.update(player)
            # update player, draw everything else
            player.update(up, down, left, right, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
            pygame.display.update()
            fpsTime.tick(fps)

    class Camera(object):

        def __init__(self, cameraFunc, width, height):
            self.cameraFunc = cameraFunc
            self.state = pygame.Rect(0, 0, width, height)

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def update(self, target):
            self.state = self.cameraFunc(self.state, target.rect)

    def simpleCamera(camera, targetRect):
        l, t, _, _ = targetRect
        _, _, w, h = camera
        return pygame.Rect(-l+halfWidth, -t+halfHeight, w, h)

    def complexCamera(camera, targetRect):
        l, t, _, _, = targetRect
        _, _, w, h = camera
        l, t, _, _, = -l+halfWidth, -t+halfHeight, w, h
        l = min(0, l)                           # Stop scrolling at the left
        l = max(-(camera.width-winWidth), l)   # Stop scrolling at the right
        t = max(-(camera.height-winHeight), t) # Stop scrolling at the bottom
        t = min(0, t)                           # Stop scrolling at the top
        return pygame.Rect(l, t, w, h)

    class Entity(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

    class Player(Entity):

        def __init__(self, x, y):
            Entity.__init__(self)
            self.xVelocity = 0
            self.yVelocity = 0
            self.x = x
            self.y = y
            self.onGround = False
            self.image = pygame.image.load(os.path.join('.', 'bin', 'YouLessPix_platform.png')).convert_alpha()
            self.rect = pygame.Rect(self.x, self.y, 42, 60)

        def update(self, up, down, left, right, platforms):
            if up:
                # Only jump if on the ground
                if self.onGround:
                    self.yVelocity -= 16

                print(self.image.get_size())

                self.image =  pygame.transform.scale(pygame.image.load(os.path.join('.', 'bin', 'sprite_1.png')).convert_alpha(), (99, 99))

                print(self.image.get_size())

                self.image =  pygame.transform.scale(pygame.image.load(os.path.join('.', 'bin', 'sprite_1.png')).convert_alpha(), (99, 99))

                self.image =  pygame.transform.scale(pygame.image.load(os.path.join('.', 'bin', 'sprite_1.png')).convert_alpha(), (99, 99))

                self.image =  pygame.transform.scale(pygame.image.load(os.path.join('.', 'bin', 'sprite_1.png')).convert_alpha(), (99, 99))

                self.image =  pygame.transform.scale(pygame.image.load(os.path.join('.', 'bin', 'sprite_1.png')).convert_alpha(), (99, 99))

                #self.image =  pygame.transform.scale(pygame.image.load(os.path.join('.', 'bin', 'sprite_1.png')).convert_alpha(), (42, 60))

            if down:
                pass
            if left:
                self.xVelocity = -8
            if right:
                self.xVelocity = 8
            if not self.onGround:
                # Only accelerate with gravity if in the air
                self.yVelocity += 1.2
                # Max falling speed
                if self.yVelocity > 200:
                    self.yVelocity = 200
            if not(left or right):
                self.xVelocity = 0
            # Increment in x direction
            self.rect.left += self.xVelocity
            # Do x-axis collisions
            self.collide(self.xVelocity, 0, platforms)
            # Increment in y direction
            self.rect.top += self.yVelocity
            # Assuming we're in the air
            self.onGround = False;
            # Do y-axis collisions
            self.collide(0, self.yVelocity, platforms)

        def collide(self, xVelocity, yVelocity, platforms):
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):
                    if isinstance(p, ExitBlock):
                        pygame.event.post(pygame.event.Event(QUIT))
                    if xVelocity > 0:
                        self.rect.right = p.rect.left
                    if xVelocity < 0:
                        self.rect.left = p.rect.right
                    if yVelocity > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yVelocity = 0
                    if yVelocity < 0:
                        self.rect.top = p.rect.bottom
                        self.rect.top += 1.2    # Jump stops when you hit a block with your head.
                        self.yVelocity = 0

    class Platform(Entity):

        def __init__(self, x, y):
            Entity.__init__(self)
            self.image = pygame.Surface((32, 32))
            self.image.blit(pygame.image.load(os.path.join('.', 'bin'
            , 'Cave Tiles.png')), (0, 0))
            self.image.convert()
            self.rect = pygame.Rect(x, y, 32, 32)
            self.isFloor = False

        def update(self):
            pass

    class ExitBlock(Platform):
        def __init__(self, x, y):
            Platform.__init__(self, x, y)
            self.image.fill(pygame.Color("darkGray"))
    main()
