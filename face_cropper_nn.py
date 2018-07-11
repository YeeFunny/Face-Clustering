# USAGE
# python detect_faces.py --image rooster.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
import numpy as np
import cv2
import os
import re

class FaceCropper(object):

    def __init__(self):
        # load our serialized model from disk
        self.net = cv2.dnn.readNetFromCaffe('model/deploy.prototxt.txt', 'model/res10_300x300_ssd_iter_140000.caffemodel')

    def generate(self, image_path, f, num):
        # load the input image and construct an input blob for the image
        # by resizing to a fixed 300x300 pixels and then normalizing it
        image = cv2.imread(images_path + f)
        if (image is None):
            print("Can't open image file %s" % f)
            return 0

        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))

        # pass the blob through the network and obtain the detections and
        # predictions
        self.net.setInput(blob)
        detections = self.net.forward()

        # loop over the detections
        face = 0
        for i in range(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with the
            # prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > 0.7:
                # compute the (x, y)-coordinates of the bounding box for the
                # object
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the bounding box of the face along with the associated
                # probability
                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                crop_img = image[startY: endY, startX: endX]

                face += 1
                cv2.imwrite(folder + num + "_%d.png" % face, crop_img)
                #cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                #cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

if __name__ == '__main__':

    images_path = "./downloads/Walid Phares/"
    folder = images_path + 'faces_nn/'

    for f in os.listdir(images_path):
        matchObj = re.match("([0-9]+)\.(.*)", f)
        if matchObj:
            num = matchObj.group(1)
            if not os.path.isdir(folder):
                os.makedirs(folder)
            detecter = FaceCropper()
            detecter.generate(images_path, f, num)