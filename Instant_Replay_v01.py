import cv2
import keyboard
import numpy

# number of frames to record
maxframes = 300

# Opens the camera
cap = cv2.VideoCapture(0)
i = 0

# Global variable to switch between Record mode and Playback mode
global recordmode
recordmode = True



while True:

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            print('Camera Off')
            break

        cv2.imwrite('frames/Frame' + "%04d" % i + '.jpg', frame)
        i += 1

        if i >= maxframes:
            i = 0

        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            # Close the window / Release webcam
            cap.release()
            recordmode = False
            print('Record Mode Off')
            break  # finishing the loop

    while not recordmode:

        imSeq = cv2.VideoCapture('frames/Frame%04d.jpg')
        # assert imSeq.isOpened()

        cv2.namedWindow("window", cv2.WINDOW_AUTOSIZE)
        counter = 0

        while True:
            ret, frames = imSeq.read()
            if not ret: break

            counter += 1
            print("count:", counter)

            cv2.imshow("window", frames)

            if cv2.waitKey(10) != -1:  # (-1 means no key)
                break

            if keyboard.is_pressed('a'):  # if key 'a' is pressed
                # Close the window / Release playback
                recordmode = True
                imSeq.release()
                print('Playback Mode Off')
                cap = cv2.VideoCapture(0)
                i = 0
                print('Camera engaged')
                break

imSeq.release()


# After we release our webcam, we also release the output
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
