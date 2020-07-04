import cv2

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    #print(check)
    #print(frame)

    cv2.imshow("capturing",frame)

    key=cv2.waitKey(1) # capture picture in 1ms

    #PRESS Q TO EXIT
    if key==ord("q"):
        break

video.release()
cv2.destroyWindow()