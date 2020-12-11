import random
from math import tan

import pygame

pygame.init()
isRunning = True
#height = 800
#width = 600
# screenres = (800,600)
infoObject = pygame.display.Info()
height=infoObject.current_w
width=infoObject.current_h
xaxis = infoObject.current_w
yaxis = infoObject.current_h
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
#screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("SpaceShip3.png")
background = pygame.image.load("Bg.png")
background = pygame.transform.scale(background, (xaxis,yaxis))
pygame.display.set_icon(icon)

# Initial SpaceShip Location
global LocX
global LocY
LocX = 600
LocY = 530
KeyPress = False
KeyPressType = None
BulletFire = False
Level = 1
Multiplier = 1

# SpaceShip Types
Level1SpaceShip = pygame.image.load("SpaceShip1.png")
Level2SpaceShip = pygame.image.load("SpaceShip2.png")
Level3SpaceShip = pygame.image.load("SpaceShip3.png")
Level4SpaceShip = pygame.image.load("SpaceShip4.png")
Level5SpaceShip = pygame.image.load("SpaceShip5.png")
Level6SpaceShip = pygame.image.load("SpaceShip6.png")
Level7SpaceShip = pygame.image.load("SpaceShip7.png")
# Level8SpaceShip = pygame.image.load("SpaceShip8.png")

# EnemyShip Types
Level1Enemy = pygame.image.load("Enemy1.png")
Level2Enemy = pygame.image.load("Enemy2.png")
Level3Enemy = pygame.image.load("Enemy3.png")
Level4Enemy = pygame.image.load("Enemy4.png")

# Bullet Types
Level1Bullet = pygame.image.load("Bullet1.png")
Level2Bullet = pygame.image.load("Bullet2.png")
Level3Bullet = pygame.image.load("Bullet3.png")
Level4Bullet = pygame.image.load("Bullet4.png")
Level5Bullet = pygame.image.load("Bullet5.png")

# Fire Types
Level1Fire = pygame.image.load("fire.png")

# Menu Colour
Play = pygame.image.load("Play.png")
PlayC = pygame.image.load("PlayC.png")
Settings = pygame.image.load("Settings.png")
SettingsC = pygame.image.load("SettingsC.png")
About = pygame.image.load("About.png")
AboutC = pygame.image.load("AboutC.png")
Resume = pygame.image.load("Resume.png")
ResumeC = pygame.image.load("ResumeC.png")

# Player Score
score = 0
angle = 0



class SpaceShip:
    def __init__(self, Name, Damage=5, FireModeAuto=True, Rotate=False, Speed=10,
                 Teleportation=False, x=0, y=0, EnemyMoveRight=True, MoveLeftRight=False, MoveUpDown=False, ShowBullet=False):
        self.MoveUpDown = MoveUpDown
        self.MoveLeftRight = MoveLeftRight
        self.Name = Name
        self.EnemyMoveRight = EnemyMoveRight
        self.FireModeAuto = FireModeAuto
        self.Damage = Damage
        self.Rotate = Rotate
        self.Speed = Speed
        self.Teleportation = Teleportation
        self.x = x
        self.y = y
        self.ShowBullet = ShowBullet

    def telePortation(self):
        if self.Teleportation:
            self.x = random.randint(0, 740)
            self.y = random.randint(0, 290)

    def Draw(self):
        screen.blit(self.Name, (self.x, self.y))

    def AutoMove(self):
        pass

    def MoveRight(self):
        self.x += self.Speed
        if self.x > 730:
            self.x = 730

    def MoveLeft(self):
        self.x -= self.Speed
        print(self.x)
        if self.x < 0:
            self.x = 0

    def MoveUp(self):
        self.y -= self.Speed
        print(self.y)
        if self.y < 0:
            self.y = 0

    def MoveDown(self):
        self.y += self.Speed
        print(self.y)
        if self.y > 530:
            self.y = 530

    def Bullets(self, name = Level1Bullet , a = 0, b = 0 ):
        global score
        self.name = name
        global BulletFire
        screen.blit(self.name, (a, b))
        for obj in EnemyList:
            if obj.x - 26 < a < obj.x + 26 and obj.y - 26 <= b <= obj.y + 26:
                obj.Damage -= 1
                BulletFire = False
                screen.blit(Level1Fire, (a, b))
                # pygame.time.wait(130)
                if obj.Damage == 0:
                    score += 1
                    screen.blit(Level1Fire, (a, b))
                    EnemyList.remove(obj)


class Enemy(SpaceShip):
    def __init__(self, Name= None, ImageName=Level1Bullet, Angle=90, Pos=((int(height - 100)), int(width - 200)),
                 AutoRotation=False):
        super().__init__(Name)
        self.ImageName = ImageName
        self.Angle = Angle
        self.Pos = Pos
        self.AutoRotation = AutoRotation


    def Rotation(self ,angle):
        OriginalPos = self.Pos
        # pos = ((int(height - 100)), int(width - 200))
        image1 = pygame.image.load("SpaceShip6.png")
        #image = self.ImageName
        screen_rect = image1.get_rect()
        screen_rect.center = OriginalPos
        image = image1.copy()
        image_rect = image1.get_rect(center=screen_rect.center)
        image1 = pygame.transform.rotate(image1, angle)
        image_rect = image1.get_rect(center=image_rect.center)
        screen.blit(image1, image_rect)

    def EnemyBullets(self, a=0, b=0):
        self.a = a
        self.b = b
        m = tan(self.Angle)
        x = self.a
        y = m*x
        screen.blit(self.name, (x, y))
        self.a = self.a+1
#        SpaceShip.Bullets(Level1Bullet)
        #print(random.randrange(20, 50, 3))


    def Movement(self):
        if obj.MoveLeftRight:
            if obj.x < 740 and obj.EnemyMoveRight is True:
                obj.x += 1
            elif obj.x == 740:
                obj.y += 10
                obj.x = 739
                obj.EnemyMoveRight = False
            elif obj.x > 0 and obj.EnemyMoveRight is False:
                obj.x -= 1
            elif obj.x <= 0:
                obj.y += 10
                obj.EnemyMoveRight = True




# Name, Damage = 5, Rotate = False, Speed = 1, Teleportation = None, x = 0, y = 0

# initilize the game ,responsible for generating Spaceship
'''EnemyList = [(SpaceShip(Name=Level1Enemy, Damage=1 * Multiplier, Speed=5, x=random.randint(0, 740),
                        y=random.randint(0, 290))),
             (SpaceShip(Name=Level2Enemy, Damage=2 * Multiplier, Speed=10, x=random.randint(0, 740),
                        y=random.randint(0, 290))),
             (SpaceShip(Name=Level3Enemy, Damage=3 * Multiplier, Speed=15, x=random.randint(0, 740),
                        y=random.randint(0, 290))),
             (SpaceShip(Name=Level4SpaceShip, Damage=4 * Multiplier, Speed=20, x=random.randint(0, 740),
                        y=random.randint(0, 290))),
             (SpaceShip(Name=Level4Enemy, Damage=4 * Multiplier, Teleportation=True, Speed=20, x=random.randint(0, 740),
                        y=random.randint(0, 290)))]'''

EnemyList = []


def GenerateEnemyBulk(level=0, number=5):
    if level == 0:
        for i in range(number):
            EnemyList.append(SpaceShip(Name=Level1Enemy, Damage=1 * Multiplier, Speed=5, x=random.randint(0, 740),
                                       y=random.randint(0, 290)))
    if level == 1:
        for i in range(number):
            EnemyList.append(SpaceShip(Name=Level2Enemy, MoveLeftRight=True, Damage=2 * Multiplier, Speed=10,
                                       x=random.randint(0, 740),
                                       y=random.randint(0, 290)))
    if level == 2:
        for i in range(number):
            EnemyList.append(
                SpaceShip(Name=Level3Enemy, Damage=3 * Multiplier, MoveUpDown=True, Speed=15, x=random.randint(0, 740),
                          y=random.randint(0, 290)))

    if level == 3:
        for i in range(number):
            EnemyList.append(
                SpaceShip(Name=Level4Enemy, MoveLeftRight=True, MoveUpDown=True, Damage=4 * Multiplier, Speed=20,
                          x=random.randint(0, xaxis),
                          y=random.randint(0, yaxis)))


SpaceShipList = [(SpaceShip(Name=Level1SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0)),
                 (SpaceShip(Name=Level2SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0)),
                 (SpaceShip(Name=Level3SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0)),
                 (SpaceShip(Name=Level4SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0)),
                 (SpaceShip(Name=Level5SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0)),
                 (SpaceShip(Name=Level6SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0)),
                 (SpaceShip(Name=Level7SpaceShip, Damage=5, x=random.randrange(0, xaxis, 30), y=0))]
move = 1
i = 0
spceshipindex = 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
MoveCross = True


def OnScreenText():
    # Score TExt
    Scoretext = font.render('Score: ' + str(score), True, green)
    ScoretextRect = Scoretext.get_rect()
    screen.blit(Scoretext, ScoretextRect)
    # Level Text
    Leveltext = font.render('Level: ' + str(Level), True, green)
    LeveltextRect = Leveltext.get_rect()
    LeveltextRect.center = (60, 50)
    screen.blit(Leveltext, LeveltextRect)
    # Bullet Text
    BulletText = font.render('Bullet: ', True, green)
    BulletTextRect = BulletText.get_rect()
    BulletTextRect.center = (700, 20)
    screen.blit(BulletText, BulletTextRect)


ScreenNumber = 1
menuitm = 1
GenerateEnemyBulk(0, 5)
RotatedImage = Enemy()
Angle = 0


def Start():
    RotatedImage.Rotation(Angle)
    if menuitm == 1:
        screen.blit(PlayC, (100, 100))
    else:
        screen.blit(Play, (100, 100))
    if menuitm == 2:
        screen.blit(SettingsC, (100, 200))
    else:
        screen.blit(Settings, (100, 200))
    if menuitm == 3:
        screen.blit(AboutC, (100, 300))
    else:
        screen.blit(About, (100, 300))
    if menuitm == 4:
        pass
        # screen.blit(ResumeC, (100, 400))
    else:
        pass
        # screen.blit(Resume, (100, 400))


while isRunning:
    if i >= len(EnemyList):
        i = 0
    screen.fill((100, 0, 0))
    screen.blit(background, (0, 0))
    if ScreenNumber == 1:
        Start()
    if ScreenNumber == 2:
        SpaceShipList[spceshipindex].Draw()
        OnScreenText()

        # generateEnemy()
        if len(EnemyList) == 0:
            Level += 1
            if Level == 0:
                GenerateEnemyBulk(0, 5)
            if Level == 1:
                GenerateEnemyBulk(1, 4)
            if Level == 2:
                GenerateEnemyBulk(2, 3)
            if Level == 3:
                GenerateEnemyBulk(3, 2)

        for obj in EnemyList:
            # obj.telePortation()
            obj.Draw()
            if obj.MoveLeftRight:
                if obj.x < 740 and obj.EnemyMoveRight is True:
                    obj.x += 1
                elif obj.x == 740:
                    obj.y += 10
                    obj.x = 739
                    obj.EnemyMoveRight = False
                elif obj.x > 0 and obj.EnemyMoveRight is False:
                    obj.x -= 1
                elif obj.x <= 0:
                    obj.y += 10
                    obj.EnemyMoveRight = True
            if obj.MoveUpDown:
                if obj.y < 340 and obj.EnemyMoveRight is True:
                    obj.y += 1
                elif obj.y == 340:
                    obj.x += 10
                    obj.y = 339
                    obj.EnemyMoveRight = False
                elif obj.y > 0 and obj.EnemyMoveRight is False:
                    obj.y -= 1
                elif obj.y <= 0:
                    obj.x += 10
                    obj.EnemyMoveRight = True
            if MoveCross:
                pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if ScreenNumber == 1:
                    if menuitm == 1:
                        menuitm = 2
                    elif menuitm == 2:
                        menuitm = 3
                    elif menuitm == 3:
                        menuitm = 4
                    elif menuitm == 4:
                        menuitm = 1
                elif ScreenNumber == 2:
                    KeyPressType = "Left"
                    SpaceShipList[spceshipindex].MoveLeft()
            if event.key == pygame.K_RIGHT:
                if ScreenNumber == 1:
                    if menuitm == 1:
                        menuitm = 4
                    elif menuitm == 2:
                        menuitm = 1
                    elif menuitm == 3:
                        menuitm = 2
                    elif menuitm == 4:
                        menuitm = 3
                elif ScreenNumber == 2:
                    KeyPressType = "Right"
                    SpaceShipList[spceshipindex].MoveRight()
            if event.key == pygame.K_UP:
                if ScreenNumber == 1:
                    if menuitm == 1:
                        menuitm = 4
                    elif menuitm == 2:
                        menuitm = 1
                    elif menuitm == 3:
                        menuitm = 2
                    elif menuitm == 4:
                        menuitm = 3
                elif ScreenNumber == 2:
                    KeyPressType = "Up"
                    SpaceShipList[spceshipindex].MoveUp()
            if event.key == pygame.K_DOWN:
                if ScreenNumber == 1:
                    if menuitm == 1:
                        menuitm = 2
                    elif menuitm == 2:
                        menuitm = 3
                    elif menuitm == 3:
                        menuitm = 4
                    elif menuitm == 4:
                        menuitm = 1
                elif ScreenNumber == 2:
                    KeyPressType = "Down"
                    SpaceShipList[spceshipindex].MoveDown()
            if event.key == pygame.K_RETURN:
                if ScreenNumber == 1:
                    ScreenNumber = 2
                elif ScreenNumber == 2:
                    ScreenNumber == 1
            if event.key == pygame.K_SPACE and not BulletFire:
                KeyPressType = "Bullet"
                bulletx = SpaceShipList[spceshipindex].x
                bullety = SpaceShipList[spceshipindex].y
                BulletFire = True
                SpaceShipList[spceshipindex].Bullets(Level1Bullet, bulletx, bullety)

            KeyPress = True
        if event.type == pygame.KEYUP:
            KeyPressType = None
            KeyPress = False

        # enemy(EnemyX, EnemyY)

        # Ship Movement Continuous
    if KeyPress:
        if KeyPressType == "Up":
            SpaceShipList[spceshipindex].MoveUp()
        if KeyPressType == "Down":
            SpaceShipList[spceshipindex].MoveDown()
        if KeyPressType == "Left":
            SpaceShipList[spceshipindex].MoveLeft()
        if KeyPressType == "Right":
            SpaceShipList[spceshipindex].MoveRight()
    if BulletFire and bullety > 0:
        bullety -= 20
        SpaceShipList[spceshipindex].Bullets(Level1Bullet, bulletx, bullety)
    else:
        BulletFire = False

    # Check Results
    i += 1
    pygame.display.update()
