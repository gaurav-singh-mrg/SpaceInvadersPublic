import random
import sys
import threading
from math import tan

import pygame
from pygame import threads

pygame.init()
isRunning = True
FullScreen = False
Debug = True

if FullScreen :
    infoObject = pygame.display.Info()
    height = infoObject.current_w
    width = infoObject.current_h
    xaxis = infoObject.current_w - 64
    yaxis = infoObject.current_h - 64
    #print("x", xaxis)
    #print("y", yaxis)
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
else :
    height = 800
    width = 600
    xaxis = height - 64
    yaxis = width - 64
    #print("x", xaxis)
    #print("y", yaxis)
    screenres = (800, 600)
    screen = pygame.display.set_mode((height, width))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("SpaceShip3.png")
background = pygame.image.load("Bg.png")
background = pygame.transform.scale(background, (height, width))
pygame.display.set_icon(icon)

# Initial SpaceShip Location
KeyPress = False
KeyPressType = None
BulletFire = False

move = 1
spceshipindex = 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
fontsize = 50
font1 = pygame.font.Font('GoodUnicornRegular-Rxev.ttf', fontsize)
font = pygame.font.Font('ka1.ttf', fontsize)
MoveCross = True


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
Level1Bullet = font1.render('  ||  ', True, white)
# Level1Bullet = pygame.image.load("Bullet1.png")
Level2Bullet = pygame.image.load("Bullet2.png")
Level3Bullet = pygame.image.load("Bullet3.png")
Level4Bullet = pygame.image.load("Bullet4.png")
Level5Bullet = pygame.image.load("Bullet5.png")

# Fire Types
Level1Fire = pygame.image.load("fire.png")

# Player Score
score = 0

EnemyList = []
# LEVEL
Level = 0
EnemyNumber = 2
BulletsFired = []
EnemyBulletsFired = []

ScreenNumber = 1
menuitm = 1

Angle = 90
# Variable Declaration
GameOver = False
clock = pygame.time.Clock()
TimeElapsed = 0


class SpaceShip :
    def __init__(self, Name, Damage=5, FireModeAuto=True, Rotate=False, Speed=10,
                 Teleportation=False, x=0, y=0, EnemyMoveRight=True, MoveLeftRight=False, MoveUpDown=False,
                 ShowBullet=True, Angle=90, BulletName=Level1Bullet, FireName=Level1Fire) :
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
        self.Angle = Angle
        self.BulletName = BulletName
        self.FireName = FireName

    def telePortation(self) :
        if self.Teleportation :
            self.x = random.randint(0, xaxis)
            self.y = random.randint(0, yaxis)

    def Draw(self) :
        # print("==",self.Name,self.x , self.y)
        screen.blit(self.Name, (self.x, self.y))

    def MoveRight(self) :
        self.x += self.Speed
        print(self.x, self.y)
        if self.x > xaxis :
            self.x = xaxis
            self.EnemyMoveRight = False

    def MoveLeft(self) :
        self.x -= self.Speed
        print(self.x, self.y)
        if self.x < 0 :
            self.x = 0
            self.EnemyMoveRight = True

    def MoveUp(self) :
        self.y -= self.Speed
        print(self.x, self.y)
        if self.y < 0 :
            self.y = 0
            self.EnemyMoveRight = False

    def MoveDown(self) :
        self.y += self.Speed
        print(self.x, self.y)
        if self.y > yaxis :
            self.y = yaxis
            self.EnemyMoveRight = True

    def Rotation(self) :
        OriginalPos = self.Pos
        # pos = ((int(height - 100)), int(width - 200))
        # image1 = pygame.image.load("SpaceShip6.png")
        image1 = self.Name
        # image = self.ImageName
        screen_rect = image1.get_rect()
        screen_rect.center = OriginalPos
        image = image1.copy()
        image_rect = image1.get_rect(center=screen_rect.center)
        image1 = pygame.transform.rotate(image1, self.Angle)
        image_rect = image1.get_rect(center=image_rect.center)
        screen.blit(image1, image_rect)

    def Movement(self) :
        if self.MoveLeftRight :
            if self.EnemyMoveRight :
                self.MoveRight()
            else :
                self.MoveLeft()
        if obj.MoveUpDown :
            if self.EnemyMoveRight :
                self.MoveUp()
            else :
                self.MoveDown()


class Enemy(SpaceShip) :
    def __init__(self, Name=None, ImageName=Level1Bullet, Angle=90, Pos=((int(height - 100)), int(width - 200)),
                 AutoRotation=False) :
        super().__init__(Name)
        self.ImageName = ImageName
        self.Angle = Angle
        self.Pos = Pos
        self.AutoRotation = AutoRotation

    def Rotation(self, angle) :
        OriginalPos = self.Pos
        # pos = ((int(height - 100)), int(width - 200))
        image1 = pygame.image.load("SpaceShip6.png")
        # image = self.ImageName
        screen_rect = image1.get_rect()
        screen_rect.center = OriginalPos
        image = image1.copy()
        image_rect = image1.get_rect(center=screen_rect.center)
        image1 = pygame.transform.rotate(image1, angle)
        image_rect = image1.get_rect(center=image_rect.center)
        screen.blit(image1, image_rect)

    def EnemyBullets(self, a=0, b=0) :
        self.a = a
        self.b = b
        m = int(tan(self.Angle))
        x = self.a
        y = int(m * x)
        screen.blit(self.BulletName, (x, y))
        self.a = self.a + 10

    def Movement(self) :
        if self.x == xaxis :
            self.y -= 1
            self.MoveRight()
        if self.y == 0 :
            self.x -= 1
            self.MoveDown()
        if self.x == 0 :
            self.y += 1
            self.MoveLeft()
        if self.y == yaxis :
            self.x += 1
            self.MoveUp()


def GenerateEnemyBulk(level, generateEnemyNumber, Multiplier=1) :
    global spceshipindex
    if level == 1 :
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level1Enemy,
                          ShowBullet=True,
                          Damage=1 * Multiplier,
                          Speed=1,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        spceshipindex += 1
    if level == 2 :
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level2Enemy,
                          MoveLeftRight=True,
                          Damage=2 * Multiplier,
                          Speed=10,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        spceshipindex += 1
    if level == 3 :
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level3Enemy,
                          Damage=3 * Multiplier,
                          MoveUpDown=True,
                          Speed=15,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        spceshipindex += 1

    if level == 4 :
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level4Enemy,
                          MoveLeftRight=True,
                          MoveUpDown=True,
                          Damage=4 * Multiplier,
                          Speed=20,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        spceshipindex += 1
    if level > 4 :
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level1Enemy,
                          ShowBullet=True,
                          Damage=1 * Multiplier,
                          Speed=1,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level2Enemy,
                          MoveLeftRight=True,
                          Damage=2 * Multiplier,
                          Speed=2,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level3Enemy,
                          Damage=3 * Multiplier,
                          MoveUpDown=True,
                          Speed=3,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        for i in range(generateEnemyNumber) :
            EnemyList.append(
                SpaceShip(Name=Level4Enemy,
                          MoveLeftRight=True,
                          MoveUpDown=True,
                          Damage=4 * Multiplier,
                          Speed=5,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))
        spceshipindex = 6

    global Level
    global EnemyNumber
    Level += 1
    EnemyNumber = Level * 2
    sys.exit()


class Weapons :
    def __init__(self, WeaponX, WeaponY, WeaponName=Level1Bullet, FireName=Level1Fire) :
        self.WeaponName = WeaponName
        self.FireName = FireName
        self.WeaponX = WeaponX
        self.WeaponY = WeaponY

    def Bullets(self, BulletName=Level1Bullet) :
        global score
        global BulletFire
        global ScreenNumber
        screen.blit(BulletName, (self.WeaponX, self.WeaponY))
        if BulletName == Level1Bullet :
            for obj in EnemyList :
                if obj.x - 26 < self.WeaponX < obj.x + 26 and obj.y - 26 <= self.WeaponY <= obj.y + 26 :
                    obj.Damage -= 1
                    BulletFire = False
                    screen.blit(self.FireName, (self.WeaponX, self.WeaponY))
                    if obj.Damage == 0 :
                        score += 1
                        screen.blit(self.FireName, (self.WeaponX, self.WeaponY))
                        self.WeaponY = 0
                        EnemyList.remove(obj)
        else :
            if SpaceShipList[spceshipindex].x - 26 < self.WeaponX < SpaceShipList[spceshipindex].x + 26 and \
                    SpaceShipList[spceshipindex].y - 26 <= self.WeaponY <= SpaceShipList[spceshipindex].y + 26 :
                SpaceShipList[spceshipindex].Damage -= 1
                # BulletFire = False
                screen.blit(self.FireName, (self.WeaponX, self.WeaponY))
                if SpaceShipList[spceshipindex].Damage == 0 :
                    # score += 1
                    screen.blit(self.FireName, (self.WeaponX, self.WeaponY))
                    self.WeaponY = 0
                    # EnemyList.remove(obj)
                    ScreenNumber = 3


SpaceShipList = [(SpaceShip(Name=Level1SpaceShip, Damage=10, x=random.randrange(0, xaxis, 30), y=yaxis)),
                 (SpaceShip(Name=Level2SpaceShip, Damage=11, x=random.randrange(0, xaxis, 30), y=yaxis)),
                 (SpaceShip(Name=Level3SpaceShip, Damage=12, x=random.randrange(0, xaxis, 30), y=yaxis)),
                 (SpaceShip(Name=Level4SpaceShip, Damage=13, x=random.randrange(0, xaxis, 30), y=yaxis)),
                 (SpaceShip(Name=Level5SpaceShip, Damage=15, x=random.randrange(0, xaxis, 30), y=yaxis)),
                 (SpaceShip(Name=Level6SpaceShip, Damage=16, x=random.randrange(0, xaxis, 30), y=yaxis)),
                 (SpaceShip(Name=Level7SpaceShip, Damage=17, x=random.randrange(0, xaxis, 30), y=yaxis))]

ScreenText = []

SpaceInvaders = font.render('SPACE INVADERS', True, white)
Playtext = font.render('Play', True, white)
PlaytextC = font.render('PLAY', True, blue)
Settingstext = font.render('Setting', True, white)
SettingstextC = font.render('SETTING', True, blue)
Abouttext = font.render('About', True, white)
AbouttextC = font.render('ABOUT', True, blue)
Quittext = font.render('Quit', True, white)
QuittextC = font.render('QUIT', True, blue)
YouwinText = font.render('WINNER', True, white)

BulletText = font1.render('  []  ', True, white)
BulletText1 = font1.render('/\\ ', True, white)
BulletText2 = font1.render(' || ', True, white)
BulletText3 = font1.render(' | ', True, white)
BulletText4 = font1.render('|~|', True, white)
BulletText5 = font1.render('|.|', True, white)
BulletText6 = font1.render('::', True, white)
BulletText7 = font1.render('.', True, white)


def OnScreenText() :
    font = pygame.font.Font('GoodUnicornRegular-Rxev.ttf', 32)
    # Score Text
    Scoretext = font.render('Score: ' + str(score), True, green)
    screen.blit(Scoretext, (0, 0))
    # Level Text
    Leveltext = font.render('Level: ' + str(Level), True, green)
    screen.blit(Leveltext, (0, 50))
    # Bullet Text
    BulletText = font.render('Bullet: ', True, green)
    screen.blit(BulletText, (xaxis - 60, 60))
    # Damage Text
    DamageText = font.render('Damage: ' + str(SpaceShipList[spceshipindex].Damage), True, green)
    screen.blit(DamageText, (xaxis - 60, 0))


def Start() :
    # RotatedImage.Rotation(Angle)
    # Angle +=1
    screen.blit(SpaceInvaders, (int(xaxis / 2 - 250), 0))
    if menuitm == 1 :
        screen.blit(PlaytextC, (int(xaxis / 2), int(yaxis / 2 - 100)))
    else :
        screen.blit(Playtext, (int(xaxis / 2), int(yaxis / 2 - 100)))
    if menuitm == 2 :
        screen.blit(SettingstextC, (int(xaxis / 2), int(yaxis / 2)))
    else :
        screen.blit(Settingstext, (int(xaxis / 2), int(yaxis / 2)))
    if menuitm == 3 :
        screen.blit(AbouttextC, (int(xaxis / 2), int(yaxis / 2 + 100)))
    else :
        screen.blit(Abouttext, (int(xaxis / 2), int(yaxis / 2 + 100)))
    if menuitm == 4 :
        screen.blit(QuittextC, (int(xaxis / 2), int(yaxis / 2 + 200)))
    else :
        screen.blit(Quittext, (int(xaxis / 2), int(yaxis / 2 + 200)))


def youlose() :
    YouloseText = font.render('You Loss', True, white)
    screen.blit(YouloseText, (int(xaxis / 2 - 100), int(yaxis / 2)))


def MenuUP() :
    global menuitm
    if menuitm == 1 :
        menuitm = 4
    elif menuitm == 2 :
        menuitm = 1
    elif menuitm == 3 :
        menuitm = 2
    elif menuitm == 4 :
        menuitm = 3


def MenuDOWN() :
    global menuitm
    if menuitm == 1 :
        menuitm = 2
    elif menuitm == 2 :
        menuitm = 3
    elif menuitm == 3 :
        menuitm = 4
    elif menuitm == 4 :
        menuitm = 1


while isRunning :
    # background
    #screen.fill((100, 0, 0))
    screen.blit(background, (0, 0))
    # timer logic
    dt = clock.tick()
    TimeElapsed += dt
    if ScreenNumber == 1 :
        Start()
    if ScreenNumber == 2 or ScreenNumber == 3 :
        SpaceShipList[spceshipindex].Draw()
        OnScreenText()
        #     RotatedImage.Rotation(Angle)
        #     RotatedImage.Movement()
        if len(EnemyList) == 0 :
            GenerateEnemyThread = threading.Thread(target=GenerateEnemyBulk, args=(Level, EnemyNumber)).start()

        for obj in EnemyList :
            # obj.telePortation()
            obj.Draw()
            obj.Movement()
            NewTime = random.randrange(0, 97000) // 1000
            # print("0000", NewTime)
            if TimeElapsed > NewTime * 900 :
                if obj.ShowBullet :
                    EnemyBulletsFired.append(Weapons(WeaponX=obj.x, WeaponY=obj.y))
                TimeElapsed = 0
            if obj.x - 26 < SpaceShipList[spceshipindex].x < obj.x + 26 and \
                    obj.y - 26 <= SpaceShipList[spceshipindex].y <= obj.y + 26 :
                ScreenNumber = 3

    if ScreenNumber == 3 :
        youlose()
        GameOver = True

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            isRunning = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                if ScreenNumber == 1 :
                    MenuDOWN()
                elif ScreenNumber == 2 :
                    KeyPressType = "Left"
                    SpaceShipList[spceshipindex].MoveLeft()
            if event.key == pygame.K_RIGHT :
                if ScreenNumber == 1 :
                    MenuUP()
                elif ScreenNumber == 2 :
                    KeyPressType = "Right"
                    SpaceShipList[spceshipindex].MoveRight()
            if event.key == pygame.K_UP :
                if ScreenNumber == 1 :
                    MenuUP()
                elif ScreenNumber == 2 :
                    KeyPressType = "Up"
                    SpaceShipList[spceshipindex].MoveUp()
            if event.key == pygame.K_DOWN :
                if ScreenNumber == 1 :
                    MenuDOWN()
                elif ScreenNumber == 2 :
                    KeyPressType = "Down"
                    SpaceShipList[spceshipindex].MoveDown()
            if event.key == pygame.K_RETURN :
                if ScreenNumber == 1 :
                    if menuitm == 1 :  # play menu
                        ScreenNumber = 2
                        GameOver = False
                    if menuitm == 2 :
                        pass
                    if menuitm == 3 :
                        pass
                    if menuitm == 4 :
                        isRunning = False  # quit menu
                elif ScreenNumber == 2 :
                    ScreenNumber = 1
                elif ScreenNumber == 3 :
                    ScreenNumber = 1
                    GameOver = False
            if event.key == pygame.K_SPACE :
                BulletsFired.append(
                    Weapons(WeaponX=SpaceShipList[spceshipindex].x, WeaponY=SpaceShipList[spceshipindex].y))
                if not BulletFire :
                    KeyPressType = "Bullet"
                    BulletFire = True

            KeyPress = True
        if event.type == pygame.KEYUP :
            KeyPressType = None
            KeyPress = False

    # Ship Movement Continuous
    if KeyPress and not GameOver :
        if KeyPressType == "Up" :
            SpaceShipList[spceshipindex].MoveUp()
        if KeyPressType == "Down" :
            SpaceShipList[spceshipindex].MoveDown()
        if KeyPressType == "Left" :
            SpaceShipList[spceshipindex].MoveLeft()
        if KeyPressType == "Right" :
            SpaceShipList[spceshipindex].MoveRight()

    # Bullet Fire
    if ScreenNumber == 2 :
        for obj in BulletsFired :
            if obj.WeaponY > 0 :
                obj.WeaponY -= 5
                obj.Bullets()
            else :
                BulletsFired.remove(obj)
                BulletsFire = False

        for obj in EnemyBulletsFired :
            if obj.WeaponY < yaxis :
                obj.WeaponY += 10
                # print("---", len(EnemyBulletsFired))
                obj.Bullets(BulletName=BulletText)
            else :
                EnemyBulletsFired.remove(obj)
                BulletsFire = False

    # Limit FrameRate of Game
    # pygame.time.Clock().tick_busy_loop(120) #uses more CPU
    pygame.time.Clock().tick(120)
    # Check Results
    pygame.display.update()
