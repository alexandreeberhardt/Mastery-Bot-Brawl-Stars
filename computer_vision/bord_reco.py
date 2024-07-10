import cv2
import numpy as np

"NOT EFFICIENT"

gamescreen = cv2.imread('../screens/gameplay_5.png', cv2.IMREAD_UNCHANGED)
bord = cv2.imread('../screens/bord_rond.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(gamescreen, bord, cv2.TM_CCOEFF_NORMED)
cv2.imshow('gamescreen', result)
cv2.waitKey()
cv2.destroyAllWindows()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = bord.shape[1]
h = bord.shape[0]

threshold = .30
yloc, xloc = np.where(result >= threshold)

rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

rectangles, weights = cv2.groupRectangles(rectangles, 1, 2)

for (x, y,w ,h) in rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255,0,0), 2)
    print(f"il y a un bord en x={x} y={y}")

cv2.imshow('gamescreen', gamescreen)
cv2.waitKey()
cv2.destroyAllWindows()



