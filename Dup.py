import cv2
import pickle
import os
import face_recognition

# Importing student images

folderPath = 'Images'
StudentIds = []
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
# print(ModePath)
for path in PathList:
    imgList.append((cv2.imread(os.path.join(folderPath, path))))
    print(os.path.splitext(path)[0])  # Getting ids from the image name#
    StudentIds.append(os.path.splitext(path)[0])
print(StudentIds)
print(len(imgList))
print("Encoding Starting.....")


# find encodings of images#
def findEncoding(imagesList):
    encodelist = []
    for image in imagesList:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        encodelist.append(encode)
    return encodelist


encodeListKnown = findEncoding(imgList)
print("Encoding Complete.....")
