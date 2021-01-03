import cv2 as cv
import tkinter as tk


# Here we are extracting the major information of the selected object such as Center, Radius, Area, Perimeter
def cbf(contours):  # Content Based Features

    centers = []
    perimeters = []
    areas = []
    rads = []

    for i in contours:
        cnt = [0, 0]
        M = cv.moments(i)
        #  To avoid dividing to zero we added a small number.
        cnt[0] = int(M['m10'] / (M['m00'] + 1e-5))
        cnt[1] = int(M['m01'] / (M['m00'] + 1e-5))
        #  print("Cx= ", cnt[0], "   Cy=", cnt[1])
        centers.append(cnt)

        perimeter = cv.arcLength(i, True)
        perimeters.append(perimeter)

        area = cv.contourArea(i)
        areas.append(area)

        radius = (area / (perimeter + 1e-5)) * 2
        radius = round(radius, 2)
        rads.append(radius)

        #  print("Radius=", radius)

    # all data collected in the dictionary and returns to the main code
    cbf_data = {"centers": centers, "perimeters": perimeters, "areas": areas, "radius": rads}
    return cbf_data


img_org = cv.imread("G:\Google\Madarek\Resume\CDRs\Pistachio Sorter By Ali\Basler images/3.jpg")
print("input shape array is: ", img_org.shape)

#Fix the format of the input picture
img = cv.cvtColor(img_org, cv.COLOR_BGR2GRAY)
fromCenter = False
Boundaries = []

# Select ROI that the our object is present, choose only one object for this trial or system only process one object
ROI_bounding = cv.selectROI("Image", img, fromCenter)

# To Finish the selection process.
ROI = img[int(ROI_bounding[1]):int(ROI_bounding[1] + ROI_bounding[3]),
      int(ROI_bounding[0]):int(ROI_bounding[0] + ROI_bounding[2])]
cv.imshow("ROI" + str(ROI_bounding), ROI)
cv.imwrite("ROI" + str(ROI_bounding) + ".jpg", ROI)

#To give enough time to show the above images
cv.waitKey(10)

# At this point we have the object
# Apply a few filters to remove noises, we suggest to add closing and opening methods as well.
img = cv.medianBlur(ROI, 5)
blur1 = cv.GaussianBlur(img, (5, 5), 10)
blur1 = cv.GaussianBlur(blur1, (5, 5), 10)

# Showing the result and saving it.
cv.imshow("blur", blur1)
cv.imwrite("Blur" + str(ROI_bounding) + ".jpg", blur1)

# Change the domain to BW, now we are able to apply more morphological filters.
b, thresh_OTSU = cv.threshold(blur1, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# At this poit we should add some morphological methods such as opening and closing to get a better object.

# Apply Filter A
# Aplly Filter B

# Show and save the results.
cv.imshow("B&W", thresh_OTSU)
cv.imwrite("BW" + str(ROI_bounding) + ".jpg", thresh_OTSU)

# Time to show the results.
cv.waitKey(10)

# Extracting and Drawing the counters
_, contours, hierarchy = cv.findContours(thresh_OTSU, 1, 2)
img = cv.drawContours(ROI, contours, -1, (255, 255, 255), 4)
cv.imshow("contour", img)
cv.imwrite("Contours" + str(ROI_bounding) + ".jpg", img)
print("We have total {} contours".format(len(contours)))

anl = cbf(contours)
print("Content Base features are: ", anl)

# Here we will find the best Ellipse that fit our object.
for i in contours:
    if len(i) > 5:
        ellipse = cv.fitEllipse(i)
        (x, y), (MA, ma), angle = ellipse
        print("ellipse", ellipse)
        im = cv.ellipse(img, ellipse, (255, 255, 255), 4)
        cv.imshow("Ellipse", im)
        cv.imwrite("Ellipse" + str(ROI_bounding) + ".jpg", im)
        pis_type = ma / (MA + 1e-5)
        print("Oval rate: ", pis_type)

# To draw the biggest contour which is might be our main target.

# There is a possibility that there are a few contours inside our object, but we are sure that our object contour
# will be the biggest.

e = []
ROI = img_org[int(ROI_bounding[1]):int(ROI_bounding[1] + ROI_bounding[3]),
      int(ROI_bounding[0]):int(ROI_bounding[0] + ROI_bounding[2])]
for i in contours:
    e.append(len(i))
for i in contours:
    if len(i) == max(e):
        ellipse = cv.fitEllipse(i)
        im = cv.ellipse(ROI, ellipse, (255, 0, 0), 5)
        cv.imshow("Ellipse biggest", im)
        cv.imwrite("Ellipse_biggest" + str(ROI_bounding) + ".jpg", im)

# To have a backup exit system that will sure we will exit effectively. 
while True:
    if cv.waitKey(10) & 0xff == ord("q"):
        break
