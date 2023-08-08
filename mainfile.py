print("WELCOME TO VEHICLE NUMBER PLATE RECOGNITION AND AUTOMATIC OPENING OF PARKING GATES")

import mysql.connector 

cn = mysql.connector.connect(host = "localhost", user = "root",passwd = "2003",database="licenseplate")  
print("connected to:", cn)  

c = cn.cursor()

def create_table():
    c.execute('CREATE TABLE VehicleDetails (Serial REAL, Brand TEXT,  Vehicle_Number TEXT)')

def data_entry():
        c.execute("INSERT INTO VehicleDetails  VALUES(1 , 'MAHINDRA', 'MH 04 JM 8765')")
        c.execute("INSERT INTO VehicleDetails  VALUES(2 , 'FORD', 'MH12DE1433')")
        c.execute("INSERT INTO VehicleDetails  VALUES(3 , 'TATA', 'KL 65 H 4383')")
        cn.commit()

print("THE PARKING DATABASE")

def read_table():
    query="select * from VehicleDetails"
    c.execute(query)
    result = c.fetchall()
    for row in result:
        print(row, '\n')



# create_table()
# data_entry()
read_table()

import cv2
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

a=input("Enter name of the image file:")
b=input("Enter the file type(png/jpg/jpeg/JPG) of the image file:")

original_image = cv2.imread(a +"."+ b)
original_image = imutils.resize(original_image, width=500 )
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) 
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
edged_image = cv2.Canny(gray_image, 30, 200)
contours, new = cv2.findContours(edged_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = original_image.copy()
cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
cv2.imshow("img1", img1)

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]

# stores the license plate contour
screenCnt = None
img2 = original_image.copy()


# draws top 30 contours
cv2.drawContours(img2, contours, -1, (0, 255, 0), 3)
cv2.imshow("img2", img2)

count = 0
idx = 7

for c in contours:
    # approximate the license plate contour
    contour_perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * contour_perimeter, True)

    # Look for contours with 4 corners
    if len(approx) == 4:
        screenCnt = approx

        # find the coordinates of the license plate contour
        x, y, w, h = cv2.boundingRect(c)
        new_img = original_image [ y: y + h, x: x + w]

        # stores the new image
        cv2.imwrite('./'+str(idx)+'.png',new_img)
        idx += 1
        break

# draws the license plate contour on original image
cv2.drawContours(original_image , [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("detected license plate", original_image )

# filename of the cropped license plate image
cropped_License_Plate = './7.png' 
cv2.imshow("cropped license plate", cv2.imread(cropped_License_Plate))

data = pytesseract.image_to_string(cropped_License_Plate, lang='eng', config='--psm 6')
print("\nDETECTED VEHICLE NUMBER IS:", data)


#PARKING GATE
print("vehicle number plate in database are the following:\n1. MH 04 JM 8765\n2. MH12DE1433\n3. KL 65 H 4383")
user_entry=input("DETECTED VEHICLE NUMBER IS:")
if user_entry == 1 or 2 or 3:
    print("WELCOME TO THE PARKING LOT!! \n THE GATE IS OPENING FOR YOUR VEHICLE")
else:
    print("YOUR VEHCILE IS NOT ALLOWED \n AS IT IS NOT IN THE DATABASE, CONTACT ADMIN TO ENTER THE PARKING LOT!")

     
cv2.waitKey(0)
cv2.destroyAllWindows()