import random
import pygame
pygame.init()
H= 600
W=800
gameScreen= pygame.display.set_mode((W,H))
color= (255,255,255)
red = (255 , 0 , 0 )
blue = (0,0,255)
x=0
y=0
w=30
h=30
movex = 0
movey = 0

frog=pygame.image.load(r'C:\Users\jatin mor\Desktop\frogg.png')#raw string-path....pygame\frog.png
frog = pygame.transform.scale(frog,(50,50))
# (0,W-50) is range for random function.... this is also act as boundry 
frogX = random.randint(0,W-50)
frogY = random.randint(0,H-50)
counter = 0
audio = pygame.mixer.Sound("C.Y.E-Resurrection.mp3")

def Score(counter):
    font=pygame.font.SysFont(None,30)
    text=font.render(f"Score:{counter}",True,blue)
    gameScreen.blit(text,(10,10))

while True:
    gameScreen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movex=-1
                movey=0
            elif event.key == pygame.K_RIGHT:
                movex=1
                movey=0
            elif event.key==pygame.K_UP:
                movey=-1
                movex=0
            elif event.key==pygame.K_DOWN:
                movey=1
                movex=0
    # gameScreen.blit(image,(imageX,imageY))
    frogRect = pygame.Rect([frogX,frogY,50,50])
    gameScreen.blit(frog,(frogX,frogY))
    x += movex
    y += movey
    
    if x>W-w:
        movex=-1
    elif x<0:
        movex=1
    if y>H-h:
        movey=-1
    elif y<0:
        movey=1
    
    Score(counter)
    snake = pygame.draw.rect(gameScreen,red,[x,y,w,h])
    if snake.colliderect(frogRect):
        frogX = random.randint(0,W-50)
        frogY = random.randint(0,H-50)
        counter+=1
        # if you use -1 it will be play infinite tyms
        audio.play(1)
        
    pygame.display.update()
