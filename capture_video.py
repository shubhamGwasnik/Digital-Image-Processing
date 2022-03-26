import cv2


# TO START VIDEO STREAMING
def video_capture():
    #  livestream from camera
    cap = cv2.VideoCapture(0);  # semicolon to caprure video indefinitely, 0 for using camera at zero index
                                # to read other video ,just write the name of that video file.
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))
    # to caputre farame continously

    print('To stop live stream press Q')
    while True:
        ret, frame = cap.read()  # if frame is available ret will be true,frame will capture the frame
        if ret==True:
            out.write(frame)
        # to capture black and white frames
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Black and white Stream', gray)
            cv2.imshow('Live Stream', frame)
            if cv2.waitKey(1) == ord('Q'):
                break
        else :
            break


    cap.release()
    out.release()
    cv2.destroyWindow()


video_capture()


# TO START RECORDING THE LIVE STREAM