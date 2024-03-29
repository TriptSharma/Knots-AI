# import the necessary packages
import numpy as np
import cv2
from get_data import download_file

#download_file
if download_file('data', 'image') == False:
	print("Exiting with error")
	exit()

print("file downloaded successfully")


# load the image
image = cv2.imread('example.jpg')

# define the list of boundaries
#red, green, blue, gray
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
	print("Camera not accessed")
	exit()

while True:
	ret, image = cap.read()	
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
	 
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
	 
	# show the images
		cv2.imshow("images", np.hstack([image, output]))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()