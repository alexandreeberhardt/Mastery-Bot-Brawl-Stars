import cv2
import numpy as np

def load_images(path_to_gameplay):
    gamescreen = cv2.imread(path_to_gameplay, cv2.IMREAD_UNCHANGED) #'../screens/gameplay_2.png'
    perso = cv2.imread('/home/alexandre/Mastery-Bot-Brawl-Stars/screens/perso_rond.png', cv2.IMREAD_UNCHANGED)
    return gamescreen, perso

def find_person(gamescreen, perso):
    return cv2.matchTemplate(gamescreen, perso, cv2.TM_CCOEFF_NORMED)

def draw_rectangles(gamescreen, result, perso, threshold=0.40):
    w = perso.shape[1]
    h = perso.shape[0]
    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 2)
    
    for (x, y, w, h) in rectangles:
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    return gamescreen, rectangles

def get_perso_info(path_to_gameplay):
    gamescreen, perso = load_images(path_to_gameplay)
    result = find_person(gamescreen, perso)
    _, rectangles = draw_rectangles(gamescreen, result, perso)
    list_perso = [(x, y) for (x, y, w, h) in rectangles]
    return {"nb_perso": len(list_perso), "list_perso": list_perso}

def display_image(image, window_name='image'):
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def main():
    path_to_gameplay='../screens/gameplay_2.png'
    gamescreen, perso = load_images(path_to_gameplay)
    result = find_person(gamescreen, perso)
    marked_screen, _ = draw_rectangles(gamescreen, result, perso)
    print(get_perso_info(path_to_gameplay))
    display_image(marked_screen)

if __name__ == "__main__":
    main()
