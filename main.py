from tkinter import *
import numpy as np
from math import *
import time

#prep work
m = Tk()
FRAMERATE = int(1000/60)
WIDTH, HEIGHT = 800, 600
scale = 150
m.geometry(str(WIDTH) + "x" + str(HEIGHT))


# all the cube vertices
points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))


cubeper_pos = [WIDTH/4, HEIGHT/4]
cubeort_pos = [WIDTH/4*3, HEIGHT/4*3]

canvas = Canvas(m,width=WIDTH,height=HEIGHT)

angle = 0

canvas.pack()
def drawline(i,j,points):
    canvas.create_line(
        points[i][0]
        ,points[i][1]
        ,points[j][0]
        ,points[j][1]
        ,width=2, fill='black', capstyle=ROUND)

def drawcube(angle):

    #rotation matrixes
    rotation_z = np.matrix([
        [cos(angle),-sin(angle),0],
        [sin(angle),cos(angle),0],
        [0,0,1]
    ])

    rotation_y = np.matrix([
        [cos(angle),0,sin(angle)],
        [0,1,0],
        [-sin(angle),0,cos(angle)]
    ])

    canvas.delete('all')
    projectedpointsper = []
    projectedpointsort = []

    for point in points:

        #generic rotation
        rotated = np.dot(rotation_z, point.T)
        rotated = np.dot(rotation_y, rotated)

        #perceptive perception matrix
        distance = 5
        z = 1/(distance - float(rotated[2][0]))

        projectionmatrixper = np.matrix([
            [z, 0, 0],
            [0, z, 0]
        ])
        projected2dper = np.dot(projectionmatrixper, rotated)

        #points per
        x = int(projected2dper[0]*scale)+cubeper_pos[0]
        y = int(projected2dper[1]*scale)+cubeper_pos[1]

        canvas.create_line(
            x
            ,y
            ,x
            ,y
            ,width=5, fill='red', capstyle=ROUND)
        projectedpointsper.append([x,y])


        #orthogonal perception matrix
        projectionmatrixort = np.matrix([
            [0.25, 0, 0],
            [0, 0.25, 0]
        ])

        projected2dort = np.dot(projectionmatrixort, rotated)

        #points ort
        x = int(projected2dort[0]*scale)+cubeort_pos[0]
        y = int(projected2dort[1]*scale)+cubeort_pos[1]

        canvas.create_line(
            x
            ,y
            ,x
            ,y
            ,width=5, fill='red', capstyle=ROUND)
        projectedpointsort.append([x, y])

    #draw all lines
    drawline(0, 1, projectedpointsper)
    drawline(1, 2, projectedpointsper)
    drawline(2, 3, projectedpointsper)
    drawline(3, 0, projectedpointsper)

    drawline(4, 5, projectedpointsper)
    drawline(5, 6, projectedpointsper)
    drawline(6, 7, projectedpointsper)
    drawline(7, 4, projectedpointsper)

    drawline(0, 4, projectedpointsper)
    drawline(1, 5, projectedpointsper)
    drawline(2, 6, projectedpointsper)
    drawline(3, 7, projectedpointsper)

    drawline(0, 1, projectedpointsort)
    drawline(1, 2, projectedpointsort)
    drawline(2, 3, projectedpointsort)
    drawline(3, 0, projectedpointsort)

    drawline(4, 5, projectedpointsort)
    drawline(5, 6, projectedpointsort)
    drawline(6, 7, projectedpointsort)
    drawline(7, 4, projectedpointsort)

    drawline(0, 4, projectedpointsort)
    drawline(1, 5, projectedpointsort)
    drawline(2, 6, projectedpointsort)
    drawline(3, 7, projectedpointsort)


while True:
    drawcube(angle)
    angle += 0.02
    canvas.update()
    time.sleep(0.001)

mainloop()