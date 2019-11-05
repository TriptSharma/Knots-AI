# import the necessary packages
import numpy as np
import cv2


# define the list of boundaries
#red, green, blue, gray
boundaries = [
	([0, 0, 0], [45,45,45])
#	([17, 15, 100], [50, 56, 200])#,
#	([86, 31, 4], [220, 88, 50]),
#	([25, 146, 190], [62, 174, 250]),q
#	([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries

cap = cv2.VideoCapture(1) 

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
		#mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

		_, contours, _ = cv2.findContours(mask,  
				cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
		  
		#cv2.imshow('Canny Edges After Contouring', edged) 
		req=[]
		maxArea=0
		max_index=0
		if len(contours)==0:
			print("No object detected")
			continue
		for i, cnt in enumerate(contours):
			if cv2.contourArea(cnt)>maxArea:
				maxArea=cv2.contourArea(cnt)
				max_index=i
				
		req.append(contours[max_index])

		if(len(req)!=0):
			cnt=req[0]
			M = cv2.moments(cnt)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			print(cx, cy)

		else:
			print("no contour")
		  
		# Draw all contours 
		# -1 signifies drawing all contours 
		cv2.drawContours(image, req, -1, (0, 255, 0), 3) 
		  
		#output = cv2.bitwise_and(image, image, mask = mask)
	 
	# show the images
		cv2.imshow("images", image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
