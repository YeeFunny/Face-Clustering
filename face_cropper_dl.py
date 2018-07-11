# USAGE
# python align_faces.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg

from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import dlib
import cv2
import os
import re

class FaceCropper(object):

    def __init__(self):
        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor and the face aligner
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('model/shape_predictor_68_face_landmarks.dat')
        self.fa = FaceAligner(self.predictor, desiredFaceWidth=256)

    def generate(self, image_path, f, num):
        # load the input image, resize it, and convert it to grayscale
        image = cv2.imread(image_path + f)
        if (image is None):
            print("Can't open image file %s" % f)
            return 0
        # image = imutils.resize(image, width=800)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # show the original input image and detect faces in the grayscale
        # image
        rects = self.detector(gray, 2)

        # loop over the face detections
        face = 0
        for rect in rects:
            # extract the ROI of the *original* face, then align the face
            # using facial landmarks
            (x, y, w, h) = rect_to_bb(rect)
            # faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
            faceAligned = self.fa.align(image, gray, rect)

            face += 1
            cv2.imwrite(image_path + 'faces_dl/' + num + "_%d.png" % face, faceAligned)

if __name__ == '__main__':

    image_path = "./trump_images/Walid Phares/"
    for f in os.listdir(image_path):
        faces = image_path + '/faces_dl/'
        detecter = FaceCropper()
        matchObj = re.match("([0-9]+)\.(.*)", f)
        if matchObj:
            num = matchObj.group(1)
            if not os.path.isdir(faces):
                os.makedirs(faces)
            detecter.generate(image_path, f, num)