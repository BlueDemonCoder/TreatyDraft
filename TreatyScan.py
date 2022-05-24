import cv2
import numpy as np
from imutils.video import VideoStream
from imutils import resize

def scanPet():
    'scans for pet using IFR camera, when heat source in position for {x} dispensetreat'
    flag = False
    im = vs.read()
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im = cv2.blur(im,(20,20))
    return im

    old_image = getImage()

    while True:
        new_image = getImage()
        diff = cv2.absdiff(old_image,new_image)
        diff_score = np.sum(diff)

        if diff_score > diff_threshold:
            flag= True
            print("Movement detected")
        old_image = new_image
        return flag
