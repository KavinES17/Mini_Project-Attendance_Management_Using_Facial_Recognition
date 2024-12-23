import cv2
import csv
import numpy as np
import face_recognition
import os
from datetime import datetime
import tkinter.messagebox


def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def attendance(name):
    with open(r'C:\Users\kavin\OneDrive\Pictures\Lenovo\Facial-Recognition-Attendance\Facial-Recognition-Attendance\Attendences.csv', 'r+') as f:
        f.seek(0)
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.write(f'{name},{tStr},{dStr},Present\n')
            print(f"Attendance recorded for {name}")

def perform_face_recognition(encodeListKnown, personNames):
    cap = cv2.VideoCapture(0)

    def convert_to_rgb(faces):
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
        return faces

    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = convert_to_rgb(faces)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personNames[matchIndex].upper()

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                attendance(name)

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def take_attendance():
    tkinter.messagebox.showinfo("Encoding Start.", "Please wait a few seconds")
    path = r'C:\Users\kavin\OneDrive\Pictures\Lenovo\Facial-Recognition-Attendance\Facial-Recognition-Attendance\images'
    images = []
    personNames = []
    myList = os.listdir(path)

    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    print(personNames)
    encodeListKnown = faceEncodings(images)
    tkinter.messagebox.showinfo("Encoding Completed.", "All Encodings Complete!!!")
    perform_face_recognition(encodeListKnown, personNames)

def show_attendance():
    try:
        os.startfile(r"C:\Users\kavin\OneDrive\Pictures\Lenovo\Facial-Recognition-Attendance\Facial-Recognition-Attendance\Attendences.csv")
    except OSError:
        tkinter.messagebox.showinfo("File Error", "Attendance file not found!")
