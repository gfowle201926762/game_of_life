# game of life
import math
import random
import numpy
import time
import pygame
pygame.init()

# RULES
# a cell with 2 or 3 live neighbours lives.
# a dead cell with 3 live neighbours comes alive.
# all other cells die.

# let's make a finite grid first.

w = 60

grid = numpy.full((w, w), 0)

#y, x!!!


def evolve(grid, w):
    a = numpy.where(grid==1)
    #print(a)
    y_coords = a[0]
    x_coords = a[1]
    length = int(len(x_coords))
    living_list = []

    for num in range(0, length):

        x = x_coords[num]
        y = y_coords[num]

        alive = 0
        for sx in range(-1, 2):
            for sy in range(-1, 2):
                if not (sx == 0 and sy == 0):
                    search_x = x + sx
                    search_y = y + sy
                    if search_x >= 0 and search_x < w:
                        if search_y >= 0 and search_y < w:

                            if grid[search_y, search_x] == 1:
                                alive += 1
                                #print("ALIVE")
                            else: # found a dead cell next to a live one. Let's check if this dead cell has exactly three neighbouring live cells:
                                reanimate = 0
                                for dsx in range(-1, 2):
                                    for dsy in range(-1, 2):
                                        dead_search_x = search_x + dsx
                                        dead_search_y = search_y + dsy
                                        if dead_search_x >= 0 and dead_search_x < w:
                                            if dead_search_y >= 0 and dead_search_y < w:
                                                if grid[dead_search_y, dead_search_x] == 1:
                                                    reanimate += 1

                                if reanimate == 3:
                                    living_list.append(search_x)
                                    living_list.append(search_y)

        if alive == 2 or alive == 3:
            living_list.append(x)
            living_list.append(y)


    # CHANGE GRID VALUES

    # kill all cells
    for x in range(0, w):
        for y in range(0, w):
            grid[x, y] = 0
    
    # revive cells which should have stayed alive or been reanimated.
    length = int(len(living_list)) / 2
    for num in range(0, int(length)):
        x = living_list[num * 2]
        y = living_list[(num * 2) + 1]
        grid[y, x] = 1








# PYGAME

dis_width_input = 900

green = (0, 225, 0)
yellow = (225, 225, 10)
brown = (31, 13, 4)
black = (0, 0, 0)
white = (255, 253, 209)
blue = (30, 144, 255)
red = (199, 21, 133)
pink = (255, 192, 203)
grey = (100, 100, 100)


dis_width = round(dis_width_input / w) * w
location_width = dis_width / w
gap = 1
block_width = location_width - gap

dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption("Game of Life")

alive_list = []
delayed_alive_list = []
mega_delayed_list = []


def stillcells():
    dis.fill(grey)
    for a in range(0, w):
        for b in range(0, w):
            if grid[a, b] == 1:
                pygame.draw.rect(dis, red, [a * location_width, b * location_width, block_width, block_width])
            else:
                pygame.draw.rect(dis, black, [a * location_width, b * location_width, block_width, block_width])


def cells():
    dis.fill(grey)

    # green is a cell alive last frame
    # yellow is a cell alive two frames ago
    # red is a new cell

    # we need a delayed list for the yellow colour to work.

    for a in range(0, w):
        for b in range(0, w):
            filled = False
            coord = [a, b]
            

            if grid[a, b] == 1:

                if coord in alive_list: # if the cell was alive the previous frame:
                    pygame.draw.rect(dis, green, [a * location_width, b * location_width, block_width, block_width])
                    filled = True

                if int(len(mega_delayed_list)) == 2 and filled == False:
                    if coord in mega_delayed_list[0]: # if cell alive two frames ago (still a new growth):
                        pygame.draw.rect(dis, yellow, [a * location_width, b * location_width, block_width, block_width])
                        alive_list.append(coord)
                        filled = True

                if filled == False: # if the cell is a new growth:
                    pygame.draw.rect(dis, red, [a * location_width, b * location_width, block_width, block_width])                
                    alive_list.append(coord)
            else:
                pygame.draw.rect(dis, black, [a * location_width, b * location_width, block_width, block_width])
                if coord in alive_list:
                    alive_list.remove(coord)

    delayed_alive_list = alive_list.copy()
    mega_delayed_list.append(delayed_alive_list)
    if int(len(mega_delayed_list)) > 2:
        mega_delayed_list.pop(0)






cells()
play = True
run = False
sleep = 0
count = 0
mega_delayed_list.pop()
while play == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                run = True
            if event.key == pygame.K_SPACE:
                run = False

            if event.key == pygame.K_UP: #faster
                if sleep >= 0.01:
                    sleep -= 0.01

            if event.key == pygame.K_DOWN: #slower
                sleep += 0.01


            if run == False and event.key == pygame.K_c:
                for a in range(0, w):
                    for b in range(0, w):
                        grid[a, b] = 0
                stillcells()

            if run == False and event.key == pygame.K_f:
                for a in range(0, w):
                    for b in range(0, w):
                        grid[a, b] = 1
                stillcells()

            if run == False and event.key == pygame.K_r:
                for a in range(0, w):
                    for b in range(0, w):
                        x = random.randint(0, 1)
                        grid[a, b] = x 
                stillcells()

            if run == False and event.key == pygame.K_h:
                for a in range(0, w):
                    for b in range(0, w):
                        x = random.randint(0, 2)
                        if x == 2:
                            x = 1
                        grid[a, b] = x 
                stillcells()

            if run == False and event.key == pygame.K_l:
                for a in range(0, w):
                    for b in range(0, w):
                        x = random.randint(0, 2)
                        if x == 2:
                            x = 0
                        grid[a, b] = x 
                stillcells()

            if run == False and event.key == pygame.K_m:
                for a in range(0 + int(round(w / 5)), w - int(round(w / 5))):
                    for b in range(0 + int(round(w / 5)), w - int(round(w / 5))):
                        x = random.randint(0, 1)
                        grid[a, b] = x 
                stillcells()

            if run == False and event.key == pygame.K_x:
                for a in range(0 + int(round(w / 4)), w - int(round(w / 4))):
                    for b in range(0 + int(round(w / 4)), w - int(round(w / 4))):
                        if a % 2 == 0:
                            if b % 2 == 0:
                                grid[a, b] = 1
                            else:
                                grid[a, b] = 0
                        else:
                            if b % 2 == 0:
                                grid[a, b] = 0
                            else:
                                grid[a, b] = 1
                stillcells()


            if run == False and event.key == pygame.K_t:
                for a in range(0, w):
                    for b in range(0, w):
                        if a % 2 == 0:
                            if b % 2 == 0:
                                grid[a, b] = 1
                            else:
                                grid[a, b] = 0
                        else:
                            if b % 2 == 0:
                                grid[a, b] = 0
                            else:
                                grid[a, b] = 1
                stillcells()

                

        if run == False and event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()
            x = math.floor(a[0] / location_width) # round down these values.
            y = math.floor(a[1] / location_width)
            delay = False
            if grid[x, y] == 0:
                grid[x, y] = 1
                delay = True
            if grid[x, y] == 1 and delay == False:
                grid[x, y] = 0
            stillcells()


    if run == True:
        count += 1
        print("\n")
        print(f"COUNT: {count}")
        print("\n")
        evolve(grid, w)
        time.sleep(sleep)
        cells()





    pygame.display.update()




