from turtle import *
from math import pi

def change_color(angle):
    if round(angle % (pi / 4), 2) == round(angle % (pi / 6), 2):
        color("green")
    elif round(angle % (pi / 4), 2) == 0:
        color("blue")
    elif round(angle % (pi / 6), 2) == 0.0:
        color("red")
    else:
        color("black")

def draw_angle(angle):
    circle(200, angle)
    change_color(heading())
    left(pi / 2)
    forward(200)
    left(pi)
    forward(200)
    left(pi / 2)

def dessiner_cercle_trigonometrique():
    radians()
    width(1)
    forward(200)
    left(pi / 2)

    for x in range(4):
        for angle in (pi / 6, (pi / 4) - (pi / 6), (pi / 3) - (pi / 4), pi / 6):
            color("black")
            draw_angle(angle)

def dessiner_angle_final():
    angle_input = textinput("Angle", "Quel angle voulez vous que je dessine ? (Vous pouvez utiliser la variable \"pi\") ")
    try:
        angle_parsed = eval(angle_input)
    except:
        angle_parsed = 0

    if angle_parsed != 0:
        width(2)
        change_color(angle_parsed)
        draw_angle(angle_parsed)

if __name__ == "__main__":
    speed(0)
    dessiner_cercle_trigonometrique()
    dessiner_angle_final()
    exitonclick()
