import cv2
import numpy as np

def load_image(image_path):
    return cv2.imread(image_path)

def convert_to_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def contours_image(hsv_image, lower_red, upper_red):
    mask= cv2.inRange(hsv_image, lower_red, upper_red)
    return cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

def draw_contours(image, contours, color, thickness):
    cv2.drawContours(image, contours, -1, color, thickness)
    return image

def show_nb():
    image_path = '../screens/gameplay_6.png'
    
    image = load_image(image_path)
    hsv_image = convert_to_hsv(image)
    
    lower_red = np.array([0, 150, 210])
    upper_red = np.array([10, 200, 255])
    
    contours = contours_image(hsv_image, lower_red, upper_red)
    
    detected_image = np.zeros_like(image)
    detected_image = draw_contours(detected_image, contours, (255, 255, 255), 2)
        
    cv2.imshow('Detected Red Areas', detected_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_superpose():
    image_path = '../screens/gameplay_6.png'
    
    image = load_image(image_path)
    hsv_image = convert_to_hsv(image)
    
    lower_red = np.array([0, 150, 210])
    upper_red = np.array([10, 200, 255])
    
    contours = contours_image(hsv_image, lower_red, upper_red)
    
    detected_image = np.zeros_like(image)
    detected_image = draw_contours(detected_image, contours, (255, 255, 255), 2)
    
    image_with_green_contours = draw_contours(image.copy(), contours, (0, 255, 0), 2)
    
    cv2.imshow('Image with Green Contours', image_with_green_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    show_superpose()

if __name__ == "__main__":
    main()
