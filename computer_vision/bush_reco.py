import cv2
import numpy as np
gamescreen = cv2.imread('../screens/gameplay_7.png', cv2.IMREAD_UNCHANGED)
bush = cv2.imread('../screens/bush_top_clean.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(gamescreen, bush, cv2.TM_CCOEFF_NORMED)
cv2.imshow('gamescreen', result)
cv2.waitKey()
cv2.destroyAllWindows()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = bush.shape[1]
h = bush.shape[0]

threshold = .40
yloc, xloc = np.where(result >= threshold)

rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0,255,0), 2)


rectangles, weights = cv2.groupRectangles(rectangles, 1, 2)
print(len(rectangles))
for (x, y,w ,h) in rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255,0,0), 2)
    print(f"Il y a des buissons en x={x} y={y}")

cv2.imshow('gamescreen', gamescreen)
cv2.waitKey()
cv2.destroyAllWindows()



