from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Coordonnées du clic: (X: {x}, Y: {y})")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
