import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
#import pygame
#from pygame.locals import *



from functools import reduce

#draw_triangle = lambda n: n/2

#print(draw_triangle)

print("Enter counter of fractal iterations")
n = int(input())
w, h = 500, 500

'''
def square():
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()
'''

x1 = w / 2
y1 = h

x2 = 1
y2 = 1

x3 = w
y3 = 1

x12 = x1
y12 = y1

x23 = x2
y23 = y2

x31 = x3
y31 = y3

def SerpinskyTriangle():
    def update_middles(x1, y1, x2, y2, x3, y3):
        global x12, y12, x23, y23, x31, y31
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2

        x23 = (x2 + x3) / 2
        y23 = (y2 + y3) / 2

        x31 = (x3 + x1) / 2
        y31 = (y3 + y1) / 2
        print(x12)
        return

    #FUNCTIONAL PARADIGM AND VERTICES CALCULATION STARTS HERE 
    
    elapesed_ms = glutGet(GLUT_ELAPSED_TIME)
    draw_triangle = lambda x1, y1, x2, y2, x3, y3, i: (i < n  ) and (
                                                    glBegin(GL_LINE_STRIP),
                                                        elapesed_ms > i*1000 and glVertex2f(x1, y1),
                                                        elapesed_ms > i*1000+1000 and glVertex2f(x2, y2),
                                                        elapesed_ms > i*1000+2000 and glVertex2f(x3, y3),
                                                    elapesed_ms > i * 1000 + 2000 and glVertex2f(x1, y1),
                                                    glEnd(),
                                                    update_middles(x1, y1, x2, y2, x3, y3),
                                                    draw_triangle(x1, y1, x12, y12, x31, y31, i + 1),
                                                    update_middles(x1, y1, x2, y2, x3, y3),
                                                    draw_triangle(x31, y31, x23, y23, x3, y3, i+1),
                                                    update_middles(x1, y1, x2, y2, x3, y3),
                                                    draw_triangle(x12, y12, x2, y2, x23, y23, i + 1),
                                                    update_middles(x1, y1, x2, y2, x3, y3))

    draw_triangle(x1, y1, x2, y2, x3, y3, 0)
    
    #FUNCTIONAL PARADIGM AND VERTICES CALCULATION ENDS HERE 

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    SerpinskyTriangle()
  #  square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

