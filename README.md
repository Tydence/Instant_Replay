# Instant_Replay
An instant reply from a webcam using OpenCV and Python
OpenCV will need to be installed.
It requires numpy and Matplotlib

Also, openCV can be installed via pip with "pip install opencv-python"
Its just really poorly documented

This is the basic framework for a super simple instant replay system

The basic outline:

Footage from a webcam is recorded as frames
When the button is pushed it goes into playback mode

In playback mode, it plays the recorded frames
When the button is pushed it goes back into recording mode


Currently, there are 2 files.
WebCam_Record_v5.py - records from a webcam to a .jpg sequence. It works great.
Except I cant get it to stop. It has to be forced to quit.

ImageSeqLoader.py plays back frames.
It currrently just does realtime playback.

Once these work, we can add functions!
But, it's a start.



