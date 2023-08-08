# ANPR-with-Parking-system

Design:

An Automatic Number Plate Recognition (ANPR) is a computer vision project that detects and recognizes vehicle license plates from images or video streams.
The ANPR project typically involves capturing the license plate image using cameras, pre-processing the image (such as cropping, contrast stretching, and noise reduction), extracting the characters from the image, and finally recognizing the characters using Optical Character Recognition (OCR).
OpenCV is an open-source computer vision library that is used for image processing and computer vision tasks. It can be used to capture license plate images, resize them, and apply various image processing techniques.
PyTesseract is a wrapper for the Tesseract OCR engine, an open-source OCR engine developed by Google. It can be used to recognize the characters from the license plate images.

Working on the Project:

OpenCV is used to detect the contours of the number plate in the image and isolate it from the rest of the vehicle. After this, Pytesseract is used to recognize the characters on the number plate. These characters are then compared with the entries in the SQL database. If a match is found, the person is assumed to be a registered user and the parking gates are opened.
