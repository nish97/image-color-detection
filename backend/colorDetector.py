import numpy as np
import pandas as pd
import cv2

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0


def recognize_color(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


def mouse_click(x, y, flags, param, img):
    global b, g, r, xpos, ypos, clicked
    clicked = True
    xpos = x
    ypos = y
    b, g, r = img[y, x]
    b = int(b)
    g = int(g)
    r = int(r)
    return int(r), int(g), int(b)

