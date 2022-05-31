import cv2
CapturePath = "Webcam Capture/webcam_capture.jpg"
def WebcamCapture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Computer Network Capture")


    ret,frame = cam.read()
    if not ret:
        print("failed to grab frame")
        return
    img_name = CapturePath
    cv2.imwrite(img_name,frame)
    print("Capture successfully")
    cv2.imshow("test",frame)

    cam.release()
