import  cv2
image=cv2.imread("mypic.jpg")
scalepercent=int(input("Enter the size of the image you want to small by : "))
width_dimension=int(image.shape[1]*scalepercent / 100)
height_dimension=int(image.shape[0]*scalepercent / 100)

dsize=(width_dimension,height_dimension)

resized_img = cv2.resize(image, dsize)

cv2.imshow("Output",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()