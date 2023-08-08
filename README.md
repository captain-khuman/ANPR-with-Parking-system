# ANPR-with-Parking-system

Design:

The ANPR with Parking System is a computer vision project that incorporates Automatic Number Plate Recognition (ANPR) to detect and recognize vehicle license plates from images or video streams. The project involves several stages, including license plate image capture, image preprocessing, character extraction, and Optical Character Recognition (OCR) for character recognition. 
OpenCV, an open-source computer vision library, is utilized for image processing tasks such as license plate image capture, resizing, and applying various image processing techniques. 
PyTesseract, a wrapper for the Tesseract OCR engine developed by Google, is employed for character recognition from license plate images.

Working on the Project:

To work on the ANPR with Parking System project, follow these steps:
1. Install OpenCV and PyTesseract dependencies.
2. Capture an image or video stream containing license plate images.
3. Use OpenCV to detect the contours of the license plate, isolating it from the rest of the vehicle.
4. Preprocess the license plate image, applying techniques like cropping, contrast stretching, and noise reduction.
5. Utilize PyTesseract to recognize the characters on the license plate.
6. Compare the recognized characters with entries in an SQL database.
7. If a match is found, assume the person is a registered user and open the parking gates.

Make sure to refer to the documentation and code files for more detailed instructions on setting up the project, configuring the database, and integrating the ANPR system with the parking gates.
