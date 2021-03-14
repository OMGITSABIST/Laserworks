import pygame as pg
import random
import json
pg.init()
width, height = 640, 480                      
screen = pg.display.set_mode((width, height)) 
pg.display.set_caption("Laserworks")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)
sheet = pg.image.load('spritesheet.png')

image = [sheet.subsurface((225, 10+40*i, 35, 35)) for i in range(4)]
image += [sheet.subsurface((265, 10+40*i, 35, 35)) for i in range(4)]
image += [sheet.subsurface((305, 10+40*i, 35, 35)) for i in range(3)]

grid = [[0]*12 for i in range(16)]
for i in range(0,16):
    for j in range(0,12):
        grid[i][j]=0

comp=1

while 1:
    screen.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            keys = pg.key.get_pressed()
            pos = pg.mouse.get_pos()
            x = pos[0]//40
            y = pos[1]//40
            if (x<16 and x>=0 and y<12 and y>=0):
                if event.button == 1:
                    if comp<9:
                        if keys[pg.K_w]:
                            grid[x][y] = comp+1
                        elif keys[pg.K_a]:
                            grid[x][y] = comp+2
                        elif keys[pg.K_s]:
                            grid[x][y] = comp+3
                        else:
                            grid[x][y] = comp
                    else:
                        grid[x][y] = comp
                elif event.button == 3:
                    grid[x][y]=0
                elif event.button == 4:
                    if (grid[x][y]>0 and grid[x][y]<4) or (grid[x][y]>4 and grid[x][y]<8):
                        grid[x][y] += 1
                    elif grid[x][y]==4 or grid[x][y]==8:
                        grid[x][y] -= 3
                elif event.button == 5:
                    if (grid[x][y]>1 and grid[x][y]<5) or (grid[x][y]>5 and grid[x][y]<9):
                        grid[x][y] -= 1
                    elif grid[x][y]==1 or grid[x][y]==5:
                        grid[x][y] += 3
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            pos = pg.mouse.get_pos()
            x = pos[0]//40
            y = pos[1]//40
            if keys[pg.K_z]:
                comp=1
            elif keys[pg.K_x]:
                comp=5
            elif keys[pg.K_c]:
                comp=10
            elif keys[pg.K_v]:
                comp=9
            elif keys[pg.K_b]:
                comp=11
            elif keys[pg.K_LEFT]:
                grid=grid[1:]+[[0]*12]
            elif keys[pg.K_RIGHT]:
                grid=[[0]*12]+grid[:-1]
            elif keys[pg.K_UP]:
                grid=[grid[i][1:]+[0] for i in range(16)]
            elif keys[pg.K_DOWN]:
                grid=[[0]+grid[i][:-1] for i in range(16)]
            elif keys[pg.K_SPACE]:
                print(grid)
            elif keys[pg.K_LCTRL] and keys[pg.K_LSHIFT]:
                if keys[pg.K_1]:
                    with open('save1.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_2]:
                    with open('save2.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_3]:
                    with open('save3.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_4]:
                    with open('save4.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_5]:
                    with open('save5.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_6]:
                    with open('save6.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_7]:
                    with open('save7.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_8]:
                    with open('save8.txt', 'r') as f:
                        grid = json.loads(f.read())
                elif keys[pg.K_9]:
                    with open('save9.txt', 'r') as f:
                        grid = json.loads(f.read())
            elif keys[pg.K_LCTRL]:
                if keys[pg.K_1]:
                    with open('save1.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_2]:
                    with open('save2.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_3]:
                    with open('save3.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_4]:
                    with open('save4.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_5]:
                    with open('save5.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_6]:
                    with open('save6.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_7]:
                    with open('save7.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_8]:
                    with open('save8.txt', 'w') as f:
                        f.write(json.dumps(grid))
                elif keys[pg.K_9]:
                    with open('save9.txt', 'w') as f:
                        f.write(json.dumps(grid))

    for i in range(0,16):
        for j in range(0,12):
            if grid[i][j]:
                screen.blit(image[grid[i][j]-1], (40*i,40*j))
    pg.display.update()
