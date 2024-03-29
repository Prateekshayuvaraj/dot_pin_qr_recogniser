from process import dotdetector
import cv2
#input as given
if __name__ == "__main__":
    image_path = "dot_peen qr\ final.jpg"
    dot_detector = dotdetector(image_path)

    dot_detector.load_image()
    dot_detector.preprocess_image()
    dot_detector.find_contours()
    dot_detector.filter_contours()
    dot_detector.draw_contours()
    
# Create a new image with detected contours as black and white background
    black_and_white_background = dot_detector.create_black_and_white_background()

    # Display results
    dot_detector.extract_data()
    dot_detector.display_results()

  

    # Optionally, you can save the black and white background to an image file
    cv2.imwrite("output_black_and_white_background.jpg", black_and_white_background)