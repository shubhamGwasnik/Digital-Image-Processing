import cv2
import time


# TO START VIDEO STREAMING
def video_capture():
    ptime = 0
    #  livestream from camera
    cap = cv2.VideoCapture(0);  # semicolon to caprure video indefinitely, 0 for using camera at zero index
                                # to read other video ,just write the name of that video file.
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))
    # to caputre farame continously

    print('To stop live stream press Q')
    while True:
        ret, img = cap.read()  # if frame is available ret will be true,frame will capture the frame
        if ret==True:
            out.write(img)
        # to capture black and white frames
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Black and white Stream', gray)
            ## face detection
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            haar_cascade = cv2.CascadeClassifier('face.xml')

            faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

            print(f'Number of faces found = {len(faces_rect)}')

            for (x, y, w, h) in faces_rect:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

            # cv2.imshow('Detected Faces', img)
            #
            # cv2.waitKey(0)
            ctime = time.time()
            fps = 1/(ctime-ptime)
            ptime = ctime
            print(fps)

            cv2.imshow('Live Stream', img)
            if cv2.waitKey(1) == ord('Q'):
                break
        else :
            break


    cap.release()
    out.release()
    # cv2.destroyWindow()


video_capture()

# it will also detect face if we show any photo to the camera
