import cv2
import sys

image_path = "/home/prakhar/Downloads/Black_hole_-_Messier_87_crop_max_res.jpg"

img = cv2.imread(image_path , 0)

if img is None:
    sys.exit("Error: Could not read the image. Please check the file path.")

# Reading an image
# cv2.imshow("window", img)

# Writing an image
# cv2.imwrite('Blackhole.jpg' , img)

# Resizing an image
print("Dimmensions" , img.shape)
width = img.shape[1]
height = 400
dim = (width , height)
resized = cv2.resize(img,dim)

cv2.imshow("window", resized)




cv2.waitKey(0)

cv2.destroyAllWindows()




# /home/prakhar/Downloads/Black_hole_-_Messier_87_crop_max_res.jpg