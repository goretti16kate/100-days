import numpy as np
import cv2 

#load the image
image = cv2.imread("mexico.jpg")

#we loop over various value of alpha transparency(0,1)
for alpha in np.arange(0, 1.1, 0.1)[::-1]:
    #create two copies of the image 
    overlay = image.copy()
    output = image.copy()

    #draw a rectangle at the specified position
    cv2.rectangle(overlay,(420,205),(595, 385),(0,0,255), -1)
    # text at the top of image
    cv2.putText(overlay, "pylance: alpha={}".format(alpha),(10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

    # apply the transparent overlay
    #first arguement = the image we want to overay on top of the original image
    #second arguement = actual alpha transparency of the overlay
    #third arguement = the source image, original image loaded from the disk
    #forth arguement = beta whiich is defined as 1 - alpha(alpha + beta = 1.0)
    #fifth parameter = the gamma value (a constant added to the output image after applying the weighted addition)
    #last is the the output destination  after applying the weighted sum operation
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    #displays the final output 
    print ("alpha{}, beta {}".format(alpha, 1 - alpha))
    cv2.imshow("output", output)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()