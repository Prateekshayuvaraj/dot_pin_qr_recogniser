import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode

#class to process contour in an image 
class dotdetector:
    def __init__(self, image_path): #class constructor
        self.image_path = image_path
        self.image = None
        self.gray = None
        self.edges = None
        self.width = None
        self.height = None
        self.channel = None
        self.contours = None
        self.filtered_contours = None
        self.result = None
 #load the image
    def load_image(self):
        self.image = cv2.imread(self.image_path)
       
#converting into grayscale,blur,gussianblur,and edge using canny
    def preprocess_image(self):
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.gray = cv2.GaussianBlur(self.gray, (9, 9), 2)
        kernel = np.ones ((2,2), np.uint8)
        self.edges = cv2.dilate(cv2.canny(self.gray, 100, 255),kernel,iterations=1)
        
    def find_contours(self):
        contours_hierarchy = cv2.findContours(
            self.edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        self.contours = contours_hierarchy[-2]
#filter counters
    def filter_contours(self):
        self.filtered_contours = []
        for contour in self.contours:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)

            if perimeter > 0:
                circularity = 4 * np.pi * (area / (perimeter * perimeter))

                if circularity > 0.0:  # adjust circularity
                    self.filtered_contours.append(contour)
#draw contour
    def draw_contours(self):
        self.result = np.zeros_like(self.image)
        cv2.drawContours(self.image, self.filtered_contours, -2, (0, 0, 0), 2)
        cv2.drawContours(
            self.result,
            self.filtered_contours,
            -3,
            (255, 255, 255),
            thickness=cv2.FILLED,
        )
    #image size
    def find_size(self):
        if self.image is not None:
            self.height, self.width, self.channels = self.image.shape
            print(f"Width: {self.width}, Height: {self.height}")
            
# Create a black image with the same resolution as the input image
    def create_black_and_white_background(self):
        black_background = np.zeros_like(self.image)

        # Draw filtered contours on the black background
        cv2.drawContours(black_background, self.filtered_contours, -1, (255, 255, 255), thickness=cv2.FILLED)
        black_background = cv2.bitwise_not(black_background) #inverse
        self.result = black_background
        return black_background
    
    def draw_contours(self):
    # Create a copy of the original image to draw contours on
     self.result = self.image.copy()

    # Draw filtered contours on the result image
     cv2.drawContours(self.result, self.filtered_contours, -3, (0, 0, 255), thickness=cv2.FILLED)

  #display result  
    def display_results(self):
        print(len(self.filtered_contours))
        cv2.imshow("Filtered Contours", self.image)
        cv2.imshow("Result", self.result)
        cv2.imshow("Black and White Background", self.create_black_and_white_background())
        cv2.waitKey(0)
        cv2.destroyAllWindows()
   #extract the data
    def extract_data(self):
        codes = decode(self.result)
        if codes:
            for code in codes:
                print("Detected DataMatrix code:", code.data)
                x, y, w, h = code.rect
                cv2.rectangle(self.result, (x, y), (x + w, y + h), (0, 255, 0), 2)