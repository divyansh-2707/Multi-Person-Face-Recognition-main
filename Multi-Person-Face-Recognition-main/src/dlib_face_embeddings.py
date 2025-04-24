'''
Create face embeddings for all the faces in the dataset directory
'''

import pickle
from imutils import paths
import cv2
import face_recognition
import os
from parameters import (
    DLIB_FACE_ENCODING_PATH,
    DATASET_PATH,
    FACE_RECOGNITION_MODEL,
    NUMBER_OF_TIMES_TO_UPSAMPLE,
)

def create_face_embeddings():
    '''
    This function creates face encodings for all the faces in the dataset directory
    '''
    imagePaths = list(paths.list_images(DATASET_PATH))
    print("[INFO] Found {} images in dataset.".format(len(imagePaths)))

    knownEncodings = []
    knownNames = []

    for (i, imagePath) in enumerate(imagePaths):
        print(f"[INFO] Processing image {i + 1}/{len(imagePaths)}")
        name = os.path.basename(os.path.dirname(imagePath))
        print(f"[INFO] Person: {name}")

        image = cv2.imread(imagePath)
        if image is None:
            print(f"[WARNING] Unable to read image: {imagePath}")
            continue

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect face locations
        boxes = face_recognition.face_locations(
            rgb, number_of_times_to_upsample=NUMBER_OF_TIMES_TO_UPSAMPLE, model=FACE_RECOGNITION_MODEL
        )

        if len(boxes) == 0:
            print(f"[WARNING] No face found in: {imagePath}")
            continue

        encodings = face_recognition.face_encodings(
            rgb, boxes, num_jitters=10, model='large'
        )

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    print("[INFO] Serializing encodings to file...")
    data = {"encodings": knownEncodings, "names": knownNames}
    with open(DLIB_FACE_ENCODING_PATH, "wb") as f:
        pickle.dump(data, f)

    print("[INFO] Embeddings creation completed successfully.")

if __name__ == '__main__':
    create_face_embeddings()
