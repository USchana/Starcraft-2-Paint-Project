'''
Paint project
'''
from pygame import *
from math import *
from time import *
from random import *
from tkinter import *
from tkinter import filedialog

init()

width,height = 1900,1080
screen = display.set_mode((width,height))

root = Tk()
root.withdraw()

display_font = font.SysFont("kaiti", 20)

"_________COLOURS_________"

RED = (181,36,36)
GREY = (127,127,127)
BLACK = (0,0,0)
BLUE = (44,69,191)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PURPLE = (122,73,191)
WHITE = (255,255,255)
cCanvas = (177, 189, 201)


"_________IMAGES_________"

#pylon
morePylons = image.load("images/pylon.jpg")
smallPylon = transform.scale(morePylons,(125,125))

#protoss
smallProtoss = transform.scale(image.load("images/protoss.jpg"),(200,200))
smallerProtoss = transform.scale(smallProtoss,(125,125))

#ghost academy
ghostMan = transform.scale(image.load("images/ghost academy.jpg"),(350,350))
smallerGhost = transform.scale(ghostMan,(200,200))

#terran
smallTerran = transform.scale(image.load("images/terran.jpg"),(150,150))
smallerTerran = transform.scale(smallTerran,(90,90))

#spawning pool
smallPool = transform.scale(image.load("images/spawning pool.jpg"),(150,150))
smallerPool = transform.scale(smallPool,(110,110))

#zerg
smallZerg = transform.scale(image.load("images/zerg.jpg"),(135,135))
smallerZerg = transform.scale(smallZerg,(100,100))

#background
logo = image.load("images/starcraft logo.png")
back1 = image.load("images/background 1.jpg")

#pencil
smallPencil = transform.scale(image.load("images/pencil.jpg"),(125,125))

#eraser
smallEraser = transform.scale(image.load("images/eraser.jpg"),(100,100))

#pallette
smallPalette = transform.scale(image.load("images/colour palette.png"),(150,150))
smallBW = transform.scale(image.load("images/shades.jpg"),(31,150))

#brush
smallBrush = transform.scale(image.load("images/brush.jpg"),(125,125))

#spray can
smallSpray = transform.scale(image.load("images/spray.jpg"),(125,125))

#eyedropper
smallEye = transform.scale(image.load("images/eyedropper.jpg"),(125,125))

#clear
smallClear = transform.scale(image.load("images/clear.jpg"),(110,110))

#open save
smallSave = transform.scale(image.load("images/save.jpg"),(100,100))
smallLoad = transform.scale(image.load("images/load.jpg"),(100,100))

#undo redo
smallUndo = transform.scale(image.load("images/undo.jpg"),(90,90))
smallRedo = transform.flip(smallUndo,True,False)

#music player
play = transform.scale(image.load("images/play.jpg"),(90,90))
pause = transform.scale(image.load("images/pause.jpg"),(90,90))


"__________MUSIC__________"

Theme = mixer.music.load("Heaven's devils.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)


" _________RECTANGLES_________"

#defining tool rectangles
rectI = Rect(20,200,125,125)
rectSquared = Rect(170,200,125,125)
rectCubed = Rect(20,350,125,125)
rectToTheIV = Rect(170,350,125,125)
rectToTheV = Rect(20,500,125,125)
rectToTheVI = Rect(170,500,125,125)
rectToTheVII = Rect(20,650,125,125)
rectToTheVIII = Rect(170,650,125,125)

#page changing rectangles 
pgLeftRect = Rect(20,140,50,50)
pgRightRect = Rect(90,140,50,50)

#misc rectangles
canvasRect = Rect(325,200,1400,750)
cBorder = Rect(323,198,1402,752)
paletteRect = Rect(20,800,221,150)

#open and save rectangles
saveRect = Rect(1600,20,100,100)
openRect = Rect(1710,20,100,100)

#undo and redo rectangles
redoRect = Rect(1490,20,100,100)
undoRect = Rect(1380,20,100,100)

#music player rectangles
play_pauseRect = Rect(1270,20,100,100)


"_________VARIABLES and LISTS_________ "

pg = 1
sz = 5
tool = "no tool"
col = BLACK
sx,sy = (0,0)
count = 0

#defining lists 

undoList = []
redoList = []
polyList = []
rects = [rectI,rectSquared,rectCubed,rectToTheIV,rectToTheV,rectToTheVI,rectToTheVII,rectToTheVIII]
toolsPG1 = ["pencil","eraser","get rekt","brush","polygon","line","ellipse","spray can"]
toolsPG2 = ["clear","eyedropper","protoss","pylon","terran","ghost","zerg","spawning pool"]

#bliting background images

screen.blit(back1,(0,0))
screen.blit(logo,(20,0))

typing = False
running = True
click = False
music = True
draw.rect(screen,(cCanvas),play_pauseRect,0)
screen.blit(pause,(1275,25))

draw.rect(screen,cCanvas,canvasRect,0)

screenCap = screen.subsurface(canvasRect).copy()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        if evt.type == MOUSEBUTTONUP:
            screenCap = screen.subsurface(canvasRect).copy()
            undoList.append(screenCap)          #taking a screenshot when user is no longer clicking and adding it to undoList
        if evt.type == MOUSEBUTTONDOWN:
            #if canvasRect.collidepoint((mx,my)):
                #screen.blit(screenCap,(325,200))#bliting screenCap when user clicks
            sx,sy = evt.pos
            click = True
            if music and play_pauseRect.collidepoint((mx,my)):  # turn music off
                music = False
                mixer.music.pause()
                draw.rect(screen,(255, 0, 0),play_pauseRect)
                draw.rect(screen,(cCanvas),play_pauseRect,0)
                screen.blit(play,(1275,25))
            elif music == False and play_pauseRect.collidepoint((mx,my)):  # turn music on
                music = True
                mixer.music.play(-1,0.0)
                draw.rect(screen,(214,182,54),play_pauseRect)
                draw.rect(screen,(cCanvas),play_pauseRect,0)
                screen.blit(pause,(1275,25))
            if tool == "get rekt":
                if evt.type == MOUSEBUTTONUP:
                    screen.blit(screenCap,(canvasRect))
                    screenCap = screen.subsurface(canvasRect).copy()
            if tool == "polygon":
                screen.set_clip(canvasRect)
                if evt.button != 3:             
                    if evt.button == 1 and canvasRect.collidepoint(mx,my):
                        count += 1              #counting number of points selected
                        if count > 0 and len(polyList) > 0:
                            draw.line(screen,(col),(mx,my),(polyList[-1]),2)    #drawing lines to form a polygon
                        polyList.append((mx,my))    #appending points selected to a list
                if evt.button == 3:
                    try:
                        draw.polygon(screen,(col),polyList,sz)  #closing the polygon when user right clicks
                        polyList = []   #emptying the list
                    except:
                        print("more points required") 
                screen.set_clip(None)
## SIZE ##
            if evt.button == 4:     #scroll to change size
                sz += 1
                print(sz)
            if evt.button==5:
                sz -= 1
                print(sz)
            if sz < 1:      #keeping sz positive
                sz = 0
                print(sz)
## STAMPS ##
            if evt.button == 1:
                screen.set_clip(canvasRect)
                if tool == "protoss":
                    screen.blit(smallProtoss,(mx - smallProtoss.get_width()/2,my - smallProtoss.get_height()/2))
                if tool == "terran":
                    screen.blit(smallTerran,(mx - smallTerran.get_width()/2,my - smallTerran.get_height()/2))
                if tool == "pylon":
                    screen.blit(morePylons,(mx - morePylons.get_width()/2,my - morePylons.get_height()/2))
                if tool == "ghost":
                    screen.blit(ghostMan,(mx - ghostMan.get_width()/2,my - ghostMan.get_height()/2))
                if tool == "zerg":
                    screen.blit(smallZerg,(mx - smallZerg.get_width()/2,my - smallZerg.get_height()/2))
                if tool == "spawning pool":
                    screen.blit(smallPool,(mx - smallPool.get_width()/2,my - smallPool.get_height()/2))
                screen.set_clip(None)
## UNDO and REDO ## 
            


    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()


##### DRAWING RECTANGLES #####

    ind = 0
    for i in range(len(rects)): #drawing tool rectangles
        draw.rect(screen,(54,59,64),rects[ind],0)
        ind += 1
       
    draw.polygon(screen,(GREY),((70,140),(70,190),(20,165)),0)
    draw.polygon(screen,(GREY),((90,140),(90,190),(140,165)),0) #page change buttons

    draw.rect(screen,(cCanvas),saveRect,0)
    draw.rect(screen,(cCanvas),openRect,0)
    draw.rect(screen,(cCanvas),undoRect,0)
    draw.rect(screen,(cCanvas),redoRect,0)


##### ICONS #####

    screen.blit(smallPalette,(paletteRect))
    screen.blit(smallBW,(190,800))
    screen.blit(smallSave,(saveRect))
    screen.blit(smallLoad,(openRect))
    screen.blit(smallUndo,(1385,25,100,100))
    screen.blit(smallRedo,(1495,25,100,100))

    if pg == 1:
        screen.blit(smallPencil,(20,200))
        screen.blit(smallEraser,(180,210))
        screen.blit(smallBrush,(rectToTheIV))
        draw.rect(screen,(BLACK),(42,372,80,80),4)
        draw.polygon(screen,(BLACK),((55,520),(100,550),(130,600),(50,610),(40,550)),4)
        draw.line(screen,(BLACK),(190,520),(270,600),4)
        draw.ellipse(screen,(BLACK),(30,680,105,80),4)
        screen.blit(smallSpray,(rectToTheVIII))

    if pg == 2:
        screen.blit(smallClear,(27,207)) 
        screen.blit(smallEye,(rectSquared))
        screen.blit(smallerProtoss,(rectCubed))
        screen.blit(smallerTerran,(37,515))
        screen.blit(smallPylon,(170,345))
        screen.blit(smallerGhost,(137,450))
        screen.blit(smallerZerg,(30,660))
        screen.blit(smallerPool,(180,660))


##### TOOL SELECTION #####

    draw.rect(screen,BLUE,rectI,2)
    if rectI.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectI,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "pencil"
            if pg == 2:
                tool = "clear"
           
    draw.rect(screen,BLUE,rectSquared,2)
    if rectSquared.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectSquared,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "eraser"
            if pg == 2:
                tool = "eyedropper"
       
    draw.rect(screen,BLUE,rectCubed,2)
    if rectCubed.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectCubed,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "get rekt"
            if pg == 2:
                tool = "protoss"
           
    draw.rect(screen,BLUE,rectToTheIV,2)
    if rectToTheIV.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectToTheIV,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "brush"
            if pg == 2:
                tool = "pylon"

    draw.rect(screen,BLUE,rectToTheV,2)
    if rectToTheV.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectToTheV,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "polygon"
            if pg == 2:
                tool = "terran"

    draw.rect(screen,BLUE,rectToTheVI,2)
    if rectToTheVI.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectToTheVI,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "line"
            if pg == 2:
                tool = "ghost"
            draw.rect(screen,RED,rectToTheVI,2)

    draw.rect(screen,BLUE,rectToTheVII,2)
    if rectToTheVII.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectToTheVII,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "ellipse"
            if pg == 2:
                tool = "zerg"

    draw.rect(screen,BLUE,rectToTheVIII,2)
    if rectToTheVIII.collidepoint(mx,my):
        draw.rect(screen,PURPLE,rectToTheVIII,2)
        if mb[0] == 1:
            if pg == 1:
                tool = "spray can"
            if pg == 2:
                tool = "spawning pool"

## SAVE and OPEN ##

    draw.rect(screen,BLUE,saveRect,2)
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,PURPLE,saveRect,2)
        if mb[0] == 1:
            try:
                fname = filedialog.asksaveasfilename(defaultextension = ".jpg")
                print(fname)
                image.save(screen.copy(canvasRect),fname)
            except:
                print("saving error")
            draw.rect(screen,RED,saveRect,2)

    draw.rect(screen,BLUE,openRect,2)
    if openRect.collidepoint(mx,my):
        draw.rect(screen,PURPLE,openRect,2)
        if mb[0] == 1:
            try:
                fname = filedialog.askopenfilename()    
                print(fname)
                mypic = image.load(fname)  
                screen.blit(mypic,(canvasRect))
            except:
                print("loading error")
            draw.rect(screen,(RED),openRect,2)

## UNDO and REDO ##

    draw.rect(screen,BLUE,undoRect,2)
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,PURPLE,undoRect,2)
        if mb[0] == 1:
            try:
                screen.blit(undoList[-2],(canvasRect))  #blitting the second last thing drawn by user
                redoList.append(undoList[-1])   #adding the last thing drawn to redoList
                del undoList[-1]    #removing the last thing drawn from undoList
            except:
                print("undo error") 
            draw.rect(screen,RED,undoRect,2)

    draw.rect(screen,BLUE,redoRect,2)
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,PURPLE,redoRect,2)
        if mb[0] == 1:
            try:
                screen.blit(redoList[-1],(canvasRect))  #blitting the last thing drawn by user
                undoList.append(redoList[-1])   #adding the image blitted to undoList
                del redoList[-1]    #removing the blitted image from redoList
            except:
                print("redo error")
            draw.rect(screen,RED,redoRect,2)

## MUSIC PLAY / PAUSE ##

    draw.rect(screen,BLUE,play_pauseRect,2)
    if play_pauseRect.collidepoint(mx,my):
        draw.rect(screen,PURPLE,play_pauseRect,2)
        if mb[0] == 1:
            draw.rect(screen,RED,play_pauseRect,2)

## CANVAS BORDER ##

    draw.rect(screen,BLUE,cBorder,2)
    if cBorder.collidepoint(mx,my):
        draw.rect(screen,PURPLE,cBorder,2)
        if mb[0] == 1:
            draw.rect(screen,RED,cBorder,2)

## HIGHLIGHTING SELECTED TOOL ##

    if tool in toolsPG1 and pg == 1:
        rectInd = toolsPG1.index(tool)
        draw.rect(screen,(RED),(rects[rectInd]),2)
    if tool in toolsPG2 and pg == 2:
        rectInd = toolsPG2.index(tool)
        draw.rect(screen,(RED),(rects[rectInd]),2)


##### PAGE CHANGE #####

    if mb[0] == 1 and pgRightRect.collidepoint(mx,my):
        pg += 1
        if pg > 2:
            pg = 2

    if mb[0] == 1 and pgLeftRect.collidepoint(mx,my):
        pg -= 1
        if pg < 1:
            pg = 1


##### TOOLS #####
    
    if tool == "clear":
            draw.rect(screen,(col),(canvasRect),0)

    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool == "pencil":
            draw.line(screen,(col),(omx,omy),(mx,my),5)
           
        if tool == "eraser":
            screenCap = screen.subsurface(canvasRect).copy()
            dx = mx - omx  
            dy = my - omy  
            hyp = sqrt(dx**2 + dy**2)
            for i in range(1,int(hyp)):
                dotx = int(omx + i*dx/hyp)
                doty = int(omy + i*dy/hyp)

                draw.circle(screen,(cCanvas),(dotx,doty),sz)

        if tool == "brush":
            dx = mx - omx  
            dy = my - omy  
            hyp = sqrt(dx**2 + dy**2)
            for i in range(1,int(hyp)):
                dotx = int(omx + i*dx/hyp)
                doty = int(omy + i*dy/hyp)
                draw.circle(screen,col,(dotx,doty),sz)

        if tool == "get rekt":
            gaps = [(mx - sz/2),(my - sz/2),((sx - sz/2) + 1),((sy - sz/2) + 1),(mx - sz/2),((sy - sz/2) + 1),((sx - sz/2) + 1),(my - sz/2)]
            ind = 0
            screen.blit(screenCap,(canvasRect))
            draw.rect(screen,(col),(sx,sy,mx - sx,my - sy),sz)
            for i in range(int(len(gaps)/2)):
                draw.rect(screen,(col),(gaps[ind],gaps[ind + 1],sz,sz),0)   #filling gaps on corners of rectangle
                ind += 2

        if tool == "line":
            screen.blit(screenCap,(canvasRect))
            draw.line(screen,(col),(sx,sy),(mx,my),sz)

        if tool == "ellipse":
            screen.blit(screenCap,(canvasRect))
            ellipseRect = Rect(sx,sy,mx - sx,my - sy)
            ellipseRect.normalize()
            if sz < abs((mx - sx)/2) and sz < abs((my - sy)/2): #checking if sz is greater or less than ellipse radius
                draw.ellipse(screen,(col),(ellipseRect),sz)
            if sz > abs((mx - sx)/2) or sz > abs((my - sy)/2):
                draw.ellipse(screen,(col),(ellipseRect),0)
           
        if tool == "spray can":
            for i in range(int(sz / 2)):    #drawing more circles as sz increases
                rx = randint(((-1)*sz),sz)
                ry = randint(((-1)*sz),sz)
                dist = sqrt((mx-(mx + rx))**2 + (my-(my + ry))**2)
                if dist < sz and mb[0] == 1:    #keeping all circles drawn within a radius of sz
                    draw.circle(screen,(col),(mx + rx,my + ry),2,0)

        if tool == "eyedropper":
            col = screen.get_at((mx,my))

        screen.set_clip(None)

    if mb[0] == 1:
        if paletteRect.collidepoint(mx,my):
            col = screen.get_at((mx,my))
   
    display.flip()
    click = False
    omx,omy = mx,my
   
quit()
