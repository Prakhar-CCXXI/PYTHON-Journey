import cv2

img = cv2.imread("/home/prakhar/Downloads/SCB.jpeg")
width = 600
height = 850
dim =(width,height)

resized = cv2.resize(img,dim)
print("Size in bytes:",img.size)

cv2.imshow('Original', resized)

flip_horizontal = cv2.flip(resized,1)
cv2.imshow('Horizontal',flip_horizontal)

flip_vertical = cv2.flip(resized,0)
cv2.imshow('Vertical',flip_vertical)

flip_vertical_horizontal = cv2.flip(resized,-1)
cv2.imshow('Vertical_horizontal',flip_vertical_horizontal)



cv2.waitKey(0)
cv2.destroyAllWindows()