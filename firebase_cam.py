import pyrebase
import numpy as np
import cv2

config = {
  "apiKey": "AIzaSyDzUK8CJ4ADaTEnLYotDmBbe5Y6fUfRgaQ",
  "authDomain": "knots-ai.firebaseapp.com",
  "databaseURL": "https://knots-ai.firebaseio.com",
  "storageBucket": "knots-ai.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
unique_id = 1000000
if ret==True:
#while(True):
	# Capture framerame-by-frame
	#cv2.imwrite('sample.jpg', frame)	
	# as admin
	data = {"opencv": 1, "nlp": 1, "move":1,"id": unique_id }
	db.child("users").set(data)
	# storage.child(str(unique_id) + "/images/example.jpg").download("sample.jpg")
	#storage.child(str(unique_id) + "/images/example.jpg").put("sample.jpg")
	storage.child(str(unique_id) + "/audio/sound.wmv").put("sound.wav")
	
	# Our operations on the frame come here
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#str = base64.b64encode(frame)
	#r = f.put({'user_id': str, 'text': 'Hello'})
	# Display the resulting frame
	#cv2.imshow('frame','sample.jpg')

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64\ ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}