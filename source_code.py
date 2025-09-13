Import numpy as np
Import cv2
Import imutils
Import pytesseract
Pytesseract.pytesseract.tesseract_cmd = “C:\Program Files (x86)\Tesseract-OCR\tesseract.exe
# Read the image file
Image = cv2.imread(‘car2.jpg)
# Resize the image file
Image = imutils.resize(image, width=500)
# Display the original image
cv2.imshow(“Original Image”, image)
cv2.waitKey(0)
# RGB to Gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(“1 – Grayscale Conversion”, gray)
cv2.waitKey(0)
# Noise removal with iterative bilateral filter removes noise while preserving edges
Gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow(“2 – Bilateral Filter”, gray)
cv2.waitKey(0)
# Find Edges of the grayscale image
Edged = cv2.Canny(gray, 170, 200)
cv2.imshow(“3 – Canny Edges”, edged)
cv2.waitKey(0)
# Find Contours based on edges
Cnts, new = cv2.findcontours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# create copy of original image to draw all countours
Img1 = image.copy()
cv2.drawCountours(img1, cnts, -1, (0,255,0), 3)
cv2.imshow(“4- All Contours”, img1)
cv2.waitKey(0)
# sort contours based their area keeping minimum area as ‘30’(anything smaller than not be considered)
cnts=sorted(cnts, key = cv2.contoursArea, reverse = True)[:30]
NumberPlateCnt = none
# Top 30 Contours
Img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0,255,0), 3)
cv2.imshow(“5- Top 30 Contours”, img2)
cv2.waitKey(0)
# Loop over out contours to find the best possible approximate contour of number plate
count = 0
idx =7
for c in cnts:
peri = cv2.arcLength(c, True)
approx. = cv2.approxPolyDP(c, 0.02 * peri, True)
# print (“approx = “,approx)
If len(approx) == 4:
NumberPlateCnt = approx
# crop those contours and store it in cropped images folder
x, y, w, h = cv2.boundingRect(c)
new_img = image[y:y + h, x:x+w]
cv2.imwrite(‘car2.jpg/’ + str(idx) + ‘.jpg’, new_img)
idx+=1
break
#Drawing the selected contour on the original image
#Print (NumberPlateCnt)
cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.imshow(“Final Image With Number Plate Detected”, image)
cv2.waitKey(0)
