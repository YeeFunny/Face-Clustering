import cv2
import os
import re

class FaceCropper(object):
    CASCADE_PATH = "/usr/local/opt/opencv@3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)

    def generate(self, image_path, file, num):
        img = cv2.imread(image_path+file)
        if (img is None):
            print("Can't open image file %s" % file)
            return 0

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 3)
        if (faces is None):
            print('Failed to detect face')
            return 0

        facecnt = len(faces)
        print("Detected faces: %d" % facecnt)
        i = 0
        height, width = img.shape[:2]

        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

            faceimg = img[ny:ny + nr, nx:nx + nr]
            i += 1
            cv2.imwrite(image_path +"faces/%s-image%d.jpg" % (num, i), faceimg)

if __name__ == '__main__':

    images_path = "./downloads/Walid Phares/"
    folder = images_path + 'faces'

    for f in os.listdir(images_path):
        matchObj = re.match("([0-9]+)\.(.*)", f)
        if matchObj:
            num = matchObj.group(1)
            if not os.path.isdir(folder):
                os.makedirs(folder)
            detecter = FaceCropper()
            detecter.generate(images_path, f, num)