import cv2
import numpy as np

def load_images():
    gamescreen = cv2.imread('../screens/gameplay_2.png', cv2.IMREAD_UNCHANGED)
    box = cv2.imread('../screens/box_clean.png', cv2.IMREAD_UNCHANGED)
    return gamescreen,box

def find_boxes(gamescreen, box):
    return cv2.matchTemplate(gamescreen, box, cv2.TM_CCOEFF_NORMED)

def display_image(image, window_name='image'):
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def draw_rectangles(gamescreen, result, box, threshold=0.60):
    w = box.shape[1]
    h = box.shape[0]
    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0,255,0), 2)
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 2)
    return rectangles


def mark_boxes(gamescreen, rectangles):
    liste_box=[]
    for (x, y,w ,h) in rectangles:
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255,0,0), 2)
        liste_box.append((x,y))

    return gamescreen,liste_box

def get_box_info():
    gamescreen, bush = load_images()
    result = find_boxes(gamescreen, bush)
    rectangles = draw_rectangles(gamescreen, result, bush)
    _, list_box= mark_boxes(gamescreen, rectangles)
    return {"nb_box":len(list_box),"list_box":list_box}

def main():
    gamescreen, box = load_images()
    result = find_boxes(gamescreen, box)
    rectangles = draw_rectangles(gamescreen, result, box)
    marked_screen, _= mark_boxes(gamescreen, rectangles)
    print(get_box_info())
    display_image(marked_screen)

if __name__ == "__main__":
    main()


