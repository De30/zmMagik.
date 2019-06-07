import cv2
import numpy as np

MIN_ACCURACY = 0.7

set_frames = {}
mon_list = []
args = []
template = None
logger = None  # loggin handler
remove_downloaded = False # true, if the input was a remote url
out_file = None # video file frames will be written to
json_out = []
kernel_clean = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
kernel_fill = np.ones((10,10),np.uint8)

# read https://docs.opencv.org/3.3.0/d2/d55/group__bgsegm.html#gae561c9701970d0e6b35ec12bae149814

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=20, nmixtures=5, backgroundRatio=0.9, noiseSigma=1) 
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG(decisionThreshold=0.98, initializationFrames=10)
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False, history=20) 
#fgbg=cv2.bgsegm.createBackgroundSubtractorGSOC(detectShadows=False)
#fgbg=cv2.bgsegm.createBackgroundSubtractorCNT(minPixelStability = 5, useHistory = True, maxPixelStability = 5 *60,isParallel = True)
#fgbg=cv2.createBackgroundSubtractorKNN(detectShadows=False)
#fgbg=cv2.bgsegm.createBackgroundSubtractorLSBP()


poly_mask = None
