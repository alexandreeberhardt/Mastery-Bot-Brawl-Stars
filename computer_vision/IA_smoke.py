import cv2
import numpy as np

def load_images():
    gamescreen = cv2.imread('../screens/gameplay_6.png', cv2.IMREAD_UNCHANGED)
    smoke = cv2.imread('../screens/smoke_small_cropped.png', cv2.IMREAD_UNCHANGED)
    return gamescreen,smoke

def find_smokees(gamescreen, smoke):
    result = cv2.matchTemplate(gamescreen, smoke, cv2.TM_CCOEFF_NORMED)
    return result

def position_moyenne(points):
        if not points:
            return None
        
        somme_x = sum(point[0] for point in points)
        somme_y = sum(point[1] for point in points)
        nombre_de_points = len(points)
        
        moyenne_x = int(somme_x / nombre_de_points)
        moyenne_y = int(somme_y / nombre_de_points)
        
        return moyenne_x, moyenne_y

def draw_rectangles(gamescreen, result, smoke, threshold=0.95):
    w = smoke.shape[1]
    h = smoke.shape[0]
    yloc, xloc = np.where(result >= threshold)
    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0,255,0), 2)
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 2)
    return rectangles

def mark_smokees(gamescreen, rectangles):
    liste_smoke=[]
    for (x, y,w ,h) in rectangles:
        cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255,0,0), 2)
        #print(f"Il y a de la smoke en x={x} y={y}")
        liste_smoke.append((x,y))
    if len(liste_smoke)!=0:
        cv2.circle(gamescreen, position_moyenne(liste_smoke), radius=10, color=(0, 255, 0), thickness=2)
        cv2.circle(gamescreen, (gamescreen.shape[1] // 2, gamescreen.shape[0] // 2), 20, (255, 0, 0), 2)
        # It draws circles to the mean position of smoke (to avoid) and to the center of the screen (to see how close we are)
    return gamescreen,liste_smoke

def display_image(image, window_name='image'):
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def calculate_average_position(points):
    if not points:
        return None
    
    somme_x = sum(point[0] for point in points)
    somme_y = sum(point[1] for point in points)
    nombre_de_points = len(points)
    
    moyenne_x = int(somme_x / nombre_de_points)
    moyenne_y = int(somme_y / nombre_de_points)
    
    return moyenne_x, moyenne_y
def calculate_distance(point1, point2):
    return int(np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def get_smoke_info():
    gamescreen, smoke = load_images()
    result = find_smokees(gamescreen, smoke)
    rectangles = draw_rectangles(gamescreen, result, smoke)
    _, liste_smoke= mark_smokees(gamescreen, rectangles)
    centre_ecran = (gamescreen.shape[1] // 2, gamescreen.shape[0] // 2)
    if len(liste_smoke)!=0:
        mean_pos = calculate_average_position(liste_smoke)
        distance = calculate_distance(mean_pos, centre_ecran)
        return {"mean_pos":mean_pos, "nb_smoke":len(liste_smoke),"centre_ecran":centre_ecran, "distance":distance}
    else :
        return {"nb_smoke":len(liste_smoke),"centre_ecran":centre_ecran}



def main():
    gamescreen, smoke = load_images()
    result = find_smokees(gamescreen, smoke)
    rectangles = draw_rectangles(gamescreen, result, smoke)
    marked_screen, _= mark_smokees(gamescreen, rectangles)
    print(get_smoke_info())
    display_image(marked_screen)

if __name__ == "__main__":
    main()










