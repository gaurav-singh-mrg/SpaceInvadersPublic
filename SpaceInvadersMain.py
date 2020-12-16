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
xaxis = infoObject.current_w - 64
yaxis = infoObject.current_h -64
print("x",xaxis)
print("y",yaxis)
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
#screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("SpaceShip3.png")
background = pygame.image.load("Bg.png")
background = pygame.transform.scale(background, (infoObject.current_w,infoObject.current_h))
pygame.display.set_icon(icon)

# Initial SpaceShip Location
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



class SpaceShip:
    def __init__(self, Name, Damage=5, FireModeAuto=True, Rotate=False, Speed=10,
                 Teleportation=False, x=0, y=0, EnemyMoveRight=True, MoveLeftRight=False, MoveUpDown=False,
                 ShowBullet=False, Angle=90, BulletName=Level1Bullet, FireName=Level1Fire,BulletX=0,BulletY=0):
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
        self.BulletX = BulletX
        self.BulletY = BulletY

    def telePortation(self):
        if self.Teleportation:
            self.x = random.randint(0, xaxis)
            self.y = random.randint(0, yaxis)

    def Draw(self):
        screen.blit(self.Name, (self.x, self.y))


    def MoveRight(self):
        self.x += self.Speed
        if self.x > xaxis:
            self.x = xaxis

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
        if self.y > yaxis:
            self.y = yaxis

    def Bullets(self):
        global score
        global BulletFire
        screen.blit(self.BulletName, (self.BulletX, self.BulletY))
        for obj in EnemyList:
            if obj.x - 26 < self.BulletX < obj.x + 26 and obj.y - 26 <= self.BulletY <= obj.y + 26:
                obj.Damage -= 1
                BulletFire = False
                screen.blit(self.FireName, (self.BulletX, self.BulletY))
                if obj.Damage == 0:
                    score += 1
                    screen.blit(self.FireName, (self.BulletX, self.BulletY))
                    EnemyList.remove(obj)


    def Rotation(self):
        OriginalPos = self.Pos
        # pos = ((int(height - 100)), int(width - 200))
        #image1 = pygame.image.load("SpaceShip6.png")
        image1 = self.Name
        #image = self.ImageName
        screen_rect = image1.get_rect()
        screen_rect.center = OriginalPos
        image = image1.copy()
        image_rect = image1.get_rect(center=screen_rect.center)
        image1 = pygame.transform.rotate(image1, self.Angle)
        image_rect = image1.get_rect(center=image_rect.center)
        screen.blit(image1, image_rect)



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
        m = int(tan(self.Angle))
        x = self.a
        y = int(m*x)
        screen.blit(self.BulletName, (x, y))
        self.a = self.a+10
#        SpaceShip.Bullets(Level1Bullet)
        #print(random.randrange(20, 50, 3))


    def Movement(self):
        if self.MoveLeftRight:
            if self.x < xaxis and self.EnemyMoveRight is True:
                self.x += 1
            elif self.x == xaxis:
                self.y += 10
                self.x = xaxis
                self.EnemyMoveRight = False
            elif self.x > 0 and self.EnemyMoveRight is False:
                self.x -= 1
            elif self.x <= 0:
                self.y += 10
                self.EnemyMoveRight = True




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
            EnemyList.append(SpaceShip(Name=Level1Enemy, ShowBullet=True,Damage=1 * Multiplier, Speed=5, x=random.randrange(0, xaxis, 30),
                                       y=random.randrange(0, yaxis, 30)))
    if level == 1:
        for i in range(number):
            EnemyList.append(SpaceShip(Name=Level2Enemy, MoveLeftRight=True, Damage=2 * Multiplier, Speed=10,
                                       x=random.randrange(0, xaxis, 30),
                                       y=random.randrange(0, yaxis, 30)))
    if level == 2:
        for i in range(number):
            EnemyList.append(
                SpaceShip(Name=Level3Enemy, Damage=3 * Multiplier, MoveUpDown=True, Speed=15, x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))

    if level == 3:
        for i in range(number):
            EnemyList.append(
                SpaceShip(Name=Level4Enemy, MoveLeftRight=True, MoveUpDown=True, Damage=4 * Multiplier, Speed=20,
                          x=random.randrange(0, xaxis, 30),
                          y=random.randrange(0, yaxis, 30)))


SpaceShipList = [(SpaceShip(Name=Level1SpaceShip, Damage=5, x=yaxis, y=random.randrange(0, xaxis, 30))),
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
    BulletTextRect.center = (xaxis-60, 60)
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
        RotatedImage.Rotation(Angle)
        RotatedImage.Movement()

        # generateEnemy()
        if len(EnemyList) == 0:
            Level += 1
            if Level == 0:
                GenerateEnemyBulk(0, 5)
            elif Level == 1:
                GenerateEnemyBulk(1, 4)
            elif Level == 2:
                GenerateEnemyBulk(2, 3)
            elif Level == 3:
                GenerateEnemyBulk(3, 2)
            else:
                isRunning = False

        for obj in EnemyList:
            # obj.telePortation()
            obj.Draw()
            obj.BulletX = obj.x
            obj.BulletY = obj.y
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
            if obj.ShowBullet:
                if obj.BulletY > 0:
                    m = int(tan(obj.Angle))
                    obj.BulletY = obj.BulletX * m
                    obj.BulletX -= 100
                    screen.blit(obj.BulletName, (obj.BulletX, obj.BulletY))
                    #obj.Bullets()

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
                SpaceShipList[spceshipindex].BulletX = SpaceShipList[spceshipindex].x
                SpaceShipList[spceshipindex].BulletY = SpaceShipList[spceshipindex].y
                KeyPressType = "Bullet"
                BulletFire = True
                SpaceShipList[spceshipindex].Bullets()

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
    if BulletFire and SpaceShipList[spceshipindex].BulletY > 0:
        m = int(tan(SpaceShipList[spceshipindex].Angle))
        #SpaceShipList[spceshipindex].BulletX = SpaceShipList[spceshipindex].BulletX * m
        SpaceShipList[spceshipindex].BulletY -= 10
        SpaceShipList[spceshipindex].Bullets()
    else:
        BulletFire = False

    # Check Results
    i += 1
    pygame.display.update()
