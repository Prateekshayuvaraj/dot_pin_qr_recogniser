# Dot Detector and DataMatrix Reader 🛍️
This Python script detects dots in an image using contour detection techniques and reads DataMatrix codes present within those dots.

## Features
- **Dot Detection**: Utilizes OpenCV for contour detection to identify dots within the image.
- **DataMatrix Reading**: Utilizes the `pylibdmtx` library to read DataMatrix codes present within the detected dots.
- **Preprocessing**: Converts the input image to grayscale, applies Gaussian blur, and detects edges using the Canny edge detector.
- **Contour Filtering**: Filters contours based on their circularity to select relevant dot-like shapes.
- **Visualization**: Draws contours on the original image and generates a black and white background with detected dots highlighted.
- **Data Extraction**: Extracts DataMatrix codes from the detected dots and overlays bounding boxes on them for visualization.

## How to Use
1. **Setup**: Ensure you have Python installed along with the required dependencies specified in `requirements.txt`.
2. **Input Image**: Provide the path to the input image containing dots and DataMatrix codes.
3. **Run Script**: Execute the script `main.py` and specify the path to the input image.
4. **Output**: The script will display the original image with contours drawn, the result image with detected dots highlighted, and the black and white background with dots.

## Dependencies
- Python 3.x
- OpenCV
- pylibdmtx

## Acknowledgements
- Inspired by the concepts of contour detection and DataMatrix decoding in image processing.
