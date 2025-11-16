import cv2

img = cv2.imread("/home/prakhar/Downloads/Black_hole_-_Messier_87_crop_max_res.jpg")

print("Dimmension of Original image" , img.shape)

scale = 50

width = int(img.shape[1]*scale/100)
height = int(img.shape[0]*scale / 100)

dim = (width,height)

# resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
resized = cv2.resize(img,dim,interpolation=cv2.INTER_LINEAR)


print('Dimmensions of Resize Image', resized.shape)

# cv2.imshow('Resized',resized)
# cv2.imshow('Original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


