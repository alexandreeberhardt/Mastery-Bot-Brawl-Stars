import pyautogui
import time
import math
from pynput import keyboard

time.sleep(2) # wait until we switch to the gamescreen

"here are my control settings, you can easily change it if you've other screen settings ! (in pixels)"

DEPLACEMENT_COORD = (285, 725)
DEPLACEMENT_DROITE = (405, 725)
DEPLACEMENT_HAUT = (285, 605)
DEPLACEMENT_GAUCHE = (165, 725)
DEPLACEMENT_BAS = (285, 845)
DEPLACEMENT_RAYON = 120

ATTAQUE_COORD = (1626, 683)
ATTAQUE_DROITE = (1748, 683)
ATTAQUE_HAUT = (1623, 571)
ATTAQUE_GAUCHE = (1505, 695)
ATTAQUE_BAS = (1629, 809)
ATTAQUE_RAYON = 120

ULTI_COORD = (1384, 785)
ULTI_DROITE = (1503, 781)
ULTI_HAUT = (1383, 656)
ULTI_GAUCHE = (1276, 788)
ULTI_BAS = (1397, 888)
ULTI_RAYON = 120

POUVOIR_STAR_COORD = (1265, 910)
GADGET_COORD = (1540, 910)

def avance_droite_temps(temps: int):
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_DROITE[0],DEPLACEMENT_DROITE[1],duration=0.01)
    time.sleep(temps)
    pyautogui.mouseUp()

def avance_gauche_temps(temps: int):
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_GAUCHE[0],DEPLACEMENT_GAUCHE[1],duration=0.01)
    time.sleep(temps)
    pyautogui.mouseUp()

def avance_bas_temps(temps: int):
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_BAS[0],DEPLACEMENT_BAS[1],duration=0.01)
    time.sleep(temps)
    pyautogui.mouseUp()

def avance_haut_temps(temps: int):
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_HAUT[0],DEPLACEMENT_HAUT[1],duration=0.01)
    time.sleep(temps)
    pyautogui.mouseUp()

def avance_angle_temps(temps: int, angle : int):

    angle_radian = math.radians(angle)
    sinus = math.sin(angle_radian)
    cosinus = math.cos(angle_radian)

    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()

    pyautogui.moveTo(DEPLACEMENT_COORD[0]+cosinus*DEPLACEMENT_RAYON,DEPLACEMENT_COORD[1]-sinus*DEPLACEMENT_RAYON,duration=0.01)
    time.sleep(temps)
    pyautogui.mouseUp()

def avance_angle_smooth(angle : int):

    angle_radian = math.radians(angle)
    sinus = math.sin(angle_radian)
    cosinus = math.cos(angle_radian)
    pyautogui.moveTo(DEPLACEMENT_COORD[0]+cosinus*DEPLACEMENT_RAYON,DEPLACEMENT_COORD[1]-sinus*DEPLACEMENT_RAYON,duration=0.01)


def avance_droite():
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_DROITE[0],DEPLACEMENT_DROITE[1],duration=0.01)


def avance_gauche():
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_GAUCHE[0],DEPLACEMENT_GAUCHE[1],duration=0.01)


def avance_bas():
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_BAS[0],DEPLACEMENT_BAS[1],duration=0.01)


def avance_haut():
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(DEPLACEMENT_HAUT[0],DEPLACEMENT_HAUT[1],duration=0.01)


def avance_angle(angle : int):

    angle_radian = math.radians(angle)
    sinus = math.sin(angle_radian)
    cosinus = math.cos(angle_radian)

    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()

    pyautogui.moveTo(DEPLACEMENT_COORD[0]+cosinus*DEPLACEMENT_RAYON,DEPLACEMENT_COORD[1]-sinus*DEPLACEMENT_RAYON,duration=0.01)


def tour():
    pyautogui.moveTo(DEPLACEMENT_COORD[0],DEPLACEMENT_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    for i in range (0, 360,2):
        avance_angle_smooth(i)
    pyautogui.mouseUp()

def attaque_auto():
    pyautogui.click(ATTAQUE_COORD[0], ATTAQUE_COORD[1])

def attaque_angle(angle : int):

    angle_radian = math.radians(angle)
    sinus = math.sin(angle_radian)
    cosinus = math.cos(angle_radian)

    pyautogui.moveTo(ATTAQUE_COORD[0],ATTAQUE_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(ATTAQUE_COORD[0]+cosinus*ATTAQUE_RAYON,ATTAQUE_COORD[1]-sinus*ATTAQUE_RAYON,duration=0.01)
    pyautogui.mouseUp()

def ulti_auto():
    pyautogui.click(ULTI_COORD[0], ULTI_COORD[1])

def ulti_angle(angle : int):

    angle_radian = math.radians(angle)
    sinus = math.sin(angle_radian)
    cosinus = math.cos(angle_radian)

    pyautogui.moveTo(ULTI_COORD[0],ULTI_COORD[1],duration=0.01)
    pyautogui.mouseDown()
    pyautogui.moveTo(ULTI_COORD[0]+cosinus*ULTI_RAYON,ULTI_COORD[1]-sinus*ULTI_RAYON,duration=0.01)
    pyautogui.mouseUp()

def pouvoir_star_auto():
    pyautogui.click(POUVOIR_STAR_COORD[0], POUVOIR_STAR_COORD[1])

def gadget_auto():
    pyautogui.click(GADGET_COORD[0], GADGET_COORD[1])

def keyboard_control():
    def on_press(key): 
        #bind keyx, zqsd to move straigth, aewx to move diagonally, space to auto-shoot and enter to auto-ulti (esc to leave)
        value=""
        try :
            if key.char=="d":
                if value !="d":
                    value="d"
                    pyautogui.mouseUp()
                    avance_droite()
            elif key.char=="q":
                if value !="q":
                    value="q"
                    pyautogui.mouseUp()
                    avance_gauche()
            elif key.char=="z":
                if value !="z":
                    value="z"
                    pyautogui.mouseUp()
                    avance_haut()
            elif key.char=="s":
                if value !="s":
                    value="s"
                    pyautogui.mouseUp()
                    avance_bas()
            elif key.char=="a":
                if value !="a":
                    value="a"
                    pyautogui.mouseUp()
                    avance_angle(135)
            elif key.char=="e":
                if value !="e":
                    value="e"
                    pyautogui.mouseUp()
                    avance_angle(45)
            elif key.char=="w":
                if value !="w":
                    value="w"
                    pyautogui.mouseUp()
                    avance_angle(225)
            elif key.char=="x":
                if value !="x":
                    value="x"
                    pyautogui.mouseUp()
                    avance_angle(315)
            elif key.char == "t":
                pyautogui.mouseUp()

        except:
            if key==keyboard.Key.space:
                attaque_auto()
            elif key==keyboard.Key.enter:
                ulti_auto()
        if key == keyboard.Key.esc:
            return False  
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    time.sleep(2)
    avance_droite_temps(3)

if __name__ == "__main__":
    main()