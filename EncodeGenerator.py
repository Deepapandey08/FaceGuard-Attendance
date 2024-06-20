import cv2
import pickle
import os
import face_recognition_models
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://faceattendancerealtime-3c8bc-default-rtdb.firebaseio.com/',
    'storageBucket': 'faceattendancerealtime-3c8bc.appspot.com'
})
from  firebase_admin import storage
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
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
print(StudentIds)
print(len(imgList))
print("Encoding Starting.....")


# find encodings of images#
def findEncoding(imagesList):
    encodelist = []
    for image in imagesList:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(image)[0]
            encodelist.append(encode)

            #Uploading to database
        except IndexError as e:
            print(f"Error encoding face: {e}")
    return encodelist


encodeListKnown = findEncoding(imgList)
encodeListKnownWithIds = [encodeListKnown, StudentIds]
print(encodeListKnown)
print("Encoding Complete.....")
file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Encoded Successfully")

