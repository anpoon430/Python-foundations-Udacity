from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import turtle

def draw_triangle(aturtle):
    aturtle.right(60)
    aturtle.forward(10)
    aturtle.right(120)
    aturtle.forward(10)
    aturtle.right(120)
    aturtle.forward(10)
    
def draw_filledtriangles(atriangle):        
    atriangle.begin_fill()
    draw_triangle(atriangle)
    atriangle.forward(10)
    atriangle.right(60)
    draw_triangle(atriangle)
    atriangle.right(120)
    atriangle.forward(10)
    atriangle.left(60)
    draw_triangle(atriangle)
    atriangle.end_fill()
    
def draw_manyfilledtri(atri):
    draw_filledtriangles(atri)
    atri.left(60)
    atri.forward(10)
    atri.right(60)
    atri.forward(10)
    atri.right(60)
    draw_filledtriangles(atri)
    atri.right(120)
    atri.forward(10)
    atri.right(60)
    atri.forward(10)
    atri.left(120)
    draw_filledtriangles(atri)
        
def draw_art():
    window=turtle.Screen()
    window.bgcolor("white")
    
    bob=turtle.Turtle()#create turtle bob draws a triangle
    bob.shape("turtle")
    bob.speed(10)
    bob.pencolor("blue")
    bob.fillcolor("green")
    
    draw_manyfilledtri(bob)
    bob.right(120)
    bob.forward(10)
    bob.right(120)
    bob.forward(80)
    bob.right(120)
    bob.forward(10)
    bob.right(60)
    draw_manyfilledtri(bob)
    bob.left(60)
    bob.forward(30)
    bob.right(60)
    bob.forward(10)
    bob.right(60)
    draw_manyfilledtri(bob)

    bob.hideturtle()
    window.exitonclick()
     
    
draw_art()

