import cv2


def cv_show(image):
    cv2.imshow("camera", image)
    cv2.waitKey(1) 
