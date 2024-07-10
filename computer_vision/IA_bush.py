import cv2
import numpy as np

def load_images():
    gamescreen = cv2.imread('../screens/gameplay_6.png', cv2.IMREAD_UNCHANGED)
    bush = cv2.imread('../screens/bush_top_clean.png', cv2.IMREAD_UNCHANGED)
    return gamescreen,bush

def find_bushes(gamescreen, bush):
    return cv2.matchTemplate(gamescreen, bush, cv2.TM_CCOEFF_NORMED)

def draw_rectangles(gamescreen, result, bush, threshold=0.40):
    w = bush.shape[1]
    h = bush.shape[0]
    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0,255,0), 2)
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 2)
    return rectangles

def mark_bushes(gamescreen, rectangles):
    liste_bush=[]
    for (x, y,w ,h) in rectangles:
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255,0,0), 2)
        liste_bush.append((x,y))

    return gamescreen,liste_bush


def display_image(image, window_name='image'):
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def get_bush_info():
    gamescreen, bush = load_images()
    result = find_bushes(gamescreen, bush)
    rectangles = draw_rectangles(gamescreen, result, bush)
    _, list_bush= mark_bushes(gamescreen, rectangles)
    return {"nb_bush":len(list_bush),"list_bush":list_bush}

def main():
    gamescreen, bush = load_images()
    result = find_bushes(gamescreen, bush)
    rectangles = draw_rectangles(gamescreen, result, bush)
    marked_screen, _= mark_bushes(gamescreen, rectangles)

    print(get_bush_info())
    
    display_image(marked_screen)

if __name__ == "__main__":
    main()
