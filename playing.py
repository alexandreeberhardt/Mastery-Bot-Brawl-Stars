import pyautogui
import time
import math
import cv2
import numpy as np
from pynput import keyboard
from pynput import mouse
from datetime import datetime
import os

from computer_vision import IA_box
from computer_vision import IA_perso
from computer_vision import IA_bush
from computer_vision import IA_smoke
from computer_vision import IA_smoke_mean
from controller import mouse_controll

running = True
number = 0
click_positions = []
attempt=4
screen=1


def take_screenshot():

    global screen

    x1, y1 = 191, 141
    x2, y2 = 1728, 1004

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    filename = f'screenshot_a{attempt}_s{screen}.png'
    screenshot.save(os.path.join('play_screen',filename))


    print(f'Capture d\'écran sauvegardée sous le nom : {os.path.join('play_screen',filename)}')
    screen+=1
    click_positions.clear()
    return os.path.join('play_screen',filename)

def on_press(key):
    global running
    try:
        if key == keyboard.Key.esc:
            running = False
    except AttributeError:
        pass

def from_a_to_b(a,b):
    ax,ay=a[0],a[1]
    bx,by=b[0],b[1]
    vx=bx-ax
    vy=by-ay
    vy=-vy
    dist = math.sqrt(vx**2 + vy**2)
    angle_radian = math.atan2(vy, vx)
    angle_degrees = math.degrees(angle_radian)
    print(dist,angle_degrees)
    return dist,angle_degrees



def jouer(perso,box,bush,smoke,smoke_mean):
    nb_perso = perso["nb_perso"]
    is_smoke = smoke["nb_smoke"]>3
    is_box = box["nb_box"]>0
    is_bush = bush["nb_bush"]>0
    joué=False
    if is_bush and nb_perso==1 :
        bush_coords = np.array(bush['list_bush'])
        perso_coords = np.array(perso['list_perso'][0])
        distances = np.linalg.norm(bush_coords - perso_coords, axis=1)
        bush_dist = list(zip(bush['list_bush'], distances))
        bush_dist_sort = sorted(bush_dist, key=lambda x: x[1])
        closest_bush = bush_dist_sort[0]
        print("closest_bush",closest_bush)
    if is_box and nb_perso==1  :
        box_coords = np.array(box['list_box'])
        perso_coords = np.array(perso['list_perso'][0])
        distances = np.linalg.norm(box_coords - perso_coords, axis=1)
        box_dist = list(zip(bush['list_bush'], distances))
        box_dist_sort = sorted(box_dist, key=lambda x: x[1])
        closest_box = box_dist_sort[0]
        print("closest_box",closest_box)
    
    if is_smoke and nb_perso==1 and joué==False:
        smoke_coord_mean = smoke_mean["mean_pos"]
        smoke_dist,smoke_angle_degrees = from_a_to_b(smoke_coord_mean,perso_coords)
        if smoke_dist<250:
            print(f"il y a de la smoke en {smoke_coord_mean}, je suis en {perso_coords}, je me déplace pendant {2-smoke_dist/5} avec un angle de {smoke_angle_degrees}")
            mouse_controll.avance_angle_temps(2-smoke_dist/50,smoke_angle_degrees)
            time.sleep(abs(2-smoke_dist/5))
            joué=True

    if is_bush and nb_perso==1 and joué==False:
        dist,angle_degrees=from_a_to_b(perso_coords,closest_bush[0])
        print(f"il y a un bush en {closest_bush[0]}, je suis en {perso_coords}, je me déplace pendant {dist/150} avec un angle de {angle_degrees}")
        mouse_controll.avance_angle_temps(dist/150,angle_degrees)
        time.sleep(5+dist/150)
        joué=True


    

def boucle():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


    while running: # boucle principale
        path_to_screen = take_screenshot()
        box = IA_box.get_box_info(path_to_screen)
        perso = IA_perso.get_perso_info(path_to_screen)
        bush = IA_bush.get_bush_info(path_to_screen)
        smoke = IA_smoke.get_smoke_info(path_to_screen)
        smoke_mean = IA_smoke_mean.get_smoke_info(path_to_screen)
        print(perso,box,bush,smoke,smoke_mean)
        jouer(perso,box,bush,smoke,smoke_mean)
        time.sleep(1)

    listener.stop()

def debug():
    time.sleep(1)
    path_to_screen = take_screenshot()
    box = IA_box.get_box_info(path_to_screen)
    perso = IA_perso.get_perso_info(path_to_screen)
    bush = IA_bush.get_bush_info(path_to_screen)
    smoke = IA_smoke.get_smoke_info(path_to_screen)
    smoke_mean = IA_smoke_mean.get_smoke_info(path_to_screen)
    print(perso,box,bush,smoke,smoke_mean)
    jouer(perso,box,bush,smoke,smoke_mean)
def main():
    for i in range (100):
        debug()

if __name__==__name__:
    main()