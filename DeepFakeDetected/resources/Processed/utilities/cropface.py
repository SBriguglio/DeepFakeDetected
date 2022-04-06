# Uses OpenCV to crop the background out of each image

import math
import os
import cv2
from tqdm import tqdm


def crop(resize_x=200, resize_y=200, sample_rate=1):
    # inner function detects face and crops image
    def inner(uncropped_image):
        gray = cv2.cvtColor(uncropped_image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
        cropped_faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in cropped_faces:
            cropped_faces = uncropped_image[y:y + h, x:x + w]
            cropped_faces = cv2.resize(cropped_faces, (resize_x, resize_y))
        return cropped_faces

    # create directories if they do not already exist
    try:
        os.makedirs('../cropped/deepfakes')
    except OSError:
        print("Note: ../cropped/deepfakes already exists")
    try:
        os.makedirs('../cropped/originals')
    except OSError:
        print("Note: ../cropped/originals already exists")

    # if you think this is messy, I agree. I did it just so I save some time not constantly checking sample_rate
    # when it is redundant (i.e. when sample_rate = 1). Over 64000ish iterations, I like to believe it saves time. :P
    # I also didn't want to put this into its own method to reduce repeated code because I'm not sure if I want to
    # change something.
    if sample_rate == 1:
        # process deepfake images
        for i in tqdm(os.listdir('../deepfakes'), desc="Cropping Deepfakes (this can take a while)..."):
            filename = str(i)
            try:
                img = cv2.imread('../deepfakes/' + filename, cv2.IMREAD_UNCHANGED)
                faces = inner(img)
                cv2.imwrite('../cropped/deepfakes/' + filename, faces)
            except:
                print("File couldn't be cropped: {}".format(filename))

        # process original images
        for i in tqdm(os.listdir('../originals'), desc="Cropping Originals (this can take a while)..."):
            filename = str(i)
            try:
                img = cv2.imread('../originals/' + filename, cv2.IMREAD_UNCHANGED)
                faces = inner(img)
                cv2.imwrite('../cropped/originals/' + filename, faces)
            except:
                print("File couldn't be cropped: {}".format(filename))
    else:
        # process deepfake images
        count = 0
        for i in tqdm(os.listdir('../deepfakes'), desc="Cropping Deepfakes (this can take a while)..."):
            count += 1
            if count % sample_rate == 0:
                filename = str(i)
                try:
                    img = cv2.imread('../deepfakes/' + filename, cv2.IMREAD_UNCHANGED)
                    faces = inner(img)
                    cv2.imwrite('../cropped/deepfakes/' + filename, faces)
                except:
                    print("File couldn't be cropped: {}".format(filename))

        # process original images
        count = 0
        for i in tqdm(os.listdir('../originals'), desc="Cropping Originals (this can take a while)..."):
            count += 1
            if count % sample_rate == 0:
                filename = str(i)
                try:
                    img = cv2.imread('../originals/' + filename, cv2.IMREAD_UNCHANGED)
                    faces = inner(img)
                    cv2.imwrite('../cropped/originals/' + filename, faces)
                except:
                    print("File couldn't be cropped: {}".format(filename))

    # friendly message letting the user know it's a good time to finish their coffee break
    print("Cropping completed.")


if __name__ == '__main__':
    crop(200, 200, 1)

