import cv2

imSeq = cv2.VideoCapture(r"C:\Users\tydence.davis\Desktop\Python\ImageSeqLoader\Resources\Image_sequence\Cars%03d.jpg")
assert imSeq.isOpened()

cv2.namedWindow("window", cv2.WINDOW_AUTOSIZE)

counter = 0
while True:
	ret, frame = imSeq.read()
	if not ret: break

	counter += 1
	print("count:", counter)

	cv2.imshow("window", frame)

	if cv2.waitKey(10) != -1: # (-1 means no key)
		break

imSeq.release()
cv2.destroyAllWindows()