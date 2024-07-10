import pyautogui
from pynput import mouse
from datetime import datetime
import os

click_positions = []

def on_click(x, y, button, pressed):
    if pressed:
        click_positions.append((x, y))
        print(f'Coordonnée du clic : (X: {x}, Y: {y})')
        if len(click_positions) == 2:
            take_screenshot()

def take_screenshot():
    x1, y1 = click_positions[0]
    x2, y2 = click_positions[1]

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'zscreenshot_{timestamp}.png'
    screenshot.save(os.path.join('../screens',filename))


    print(f'Capture d\'écran sauvegardée sous le nom : {os.path.join('screens',filename)}')

    click_positions.clear()

with mouse.Listener(on_click=on_click) as listener:
    print("Cliquez en haut à gauche puis en bas à droite de la zone à screen.")
    listener.join()
