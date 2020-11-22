import cv2
from random import randrange
# loading some pre trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choosing an image to detect faces in
webcam = cv2.VideoCapture(0)
#iterate for all frames
while True:
    successful_frame_read,frame = webcam.read()
    # Converting it into greyscale
    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detecting faces by putting our grey scale image in the above trained data
    face_coordinates = trained_face_data.detectMultiScale(grey_img)

    # Draw rectangle around face
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray = grey_img[y:y+h,x:x+w]
        img_item = "my_image.png"
        cv2.imwrite(img_item,roi_gray)

    cv2.imshow("This sis Fahads Photo",frame)
    key = cv2.waitKey(10)
    
    #quits the if you press Q
    if key==81 or key==113:
        break


print("Code Finished")