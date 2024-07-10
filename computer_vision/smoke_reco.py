import cv2
import numpy as np
gamescreen = cv2.imread('../screens/gameplay_6.png', cv2.IMREAD_UNCHANGED)
bush = cv2.imread('../screens/smoke_small_cropped.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(gamescreen, bush, cv2.TM_CCOEFF_NORMED)
cv2.imshow('gamescreen', result)
cv2.waitKey()
cv2.destroyAllWindows()
liste_bush=[]
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = bush.shape[1]
h = bush.shape[0]

threshold = .95
yloc, xloc = np.where(result >= threshold)

rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0,255,0), 2)


rectangles, weights = cv2.groupRectangles(rectangles, 1, 2)

def position_moyenne(points):
        if not points:
            return None
        
        somme_x = sum(point[0] for point in points)
        somme_y = sum(point[1] for point in points)
        nombre_de_points = len(points)
        
        moyenne_x = int(somme_x / nombre_de_points)
        moyenne_y = int(somme_y / nombre_de_points)
        
        return moyenne_x, moyenne_y

for (x, y,w ,h) in rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255,0,0), 2)
    print(f"Il y a de la smoke en x={x} y={y}")
    liste_bush.append((x,y))
if len(liste_bush)!=0:
    '''bush_sorted_by_x_min = sorted(liste_bush, key=lambda point: point[0])[:10]
    bush_sorted_by_y_min = sorted(liste_bush, key=lambda point: point[1])[:10]
    bush_sorted_by_x_max = sorted(liste_bush, key=lambda point: point[0], reverse=True)[:10]
    bush_sorted_by_y_max = sorted(liste_bush, key=lambda point: point[1], reverse=True)[:10]
    border_droite=min(x[0] for x in bush_sorted_by_y_min)
    border_bas=min(x[1] for x in bush_sorted_by_x_min)
    border_gauche=max(x[0] for x in bush_sorted_by_y_min)
    border_haut=max(x[1] for x in bush_sorted_by_x_min)
    cv2.line(gamescreen, (border_droite,0), (border_droite,gamescreen.shape[0]), (0, 0, 255), 2)
    cv2.line(gamescreen, (0,border_bas), (gamescreen.shape[1],border_bas), (0, 0, 255), 2)
    cv2.line(gamescreen, (border_gauche,0), (border_gauche,gamescreen.shape[0]), (0, 0, 255), 2)
    cv2.line(gamescreen, (0,border_haut), (gamescreen.shape[1],border_haut), (0, 0, 255), 2)'''
    #it draws lines to créate a virtual border, but it's not eficient.
    cv2.circle(gamescreen, position_moyenne(liste_bush), radius=10, color=(0, 255, 0), thickness=2)
    cv2.circle(gamescreen, (gamescreen.shape[1] // 2, gamescreen.shape[0] // 2), 20, (255, 0, 0), 2)
    # It draws circles to the mean position of smoke (to avoid) and to the center of the screen (to see how close we are)


cv2.imshow('gamescreen', gamescreen)
cv2.waitKey()
cv2.destroyAllWindows()



