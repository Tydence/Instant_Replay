import cv2


# Global variable to switch between Record mode and Playback mode
global recordmode
recordmode = True

# number of frames to record
maxframes = 300


# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)
i = 0

while(cap.isOpened()):
	ret, frame = cap.read()
	# This condition prevents from infinite looping
	# incase video ends.
	if ret == False:
	    break
		
	# Save Frame by Frame into disk using imwrite method
	cv2.imwrite('frames/Frame'+str(i)+'.jpg', frame)
	i += 1
		
	if i >= maxframes:
		i = 0

	# Something should go here to stop the loop (without stopping this from looping)
	# and switch to Playback Mode 



# Close the window / Release webcam
cap.release()

# After we release our webcam, we also release the output
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
