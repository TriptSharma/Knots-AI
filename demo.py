import pyrebase
import numpy as np

config = {
  "apiKey": "AIzaSyDzUK8CJ4ADaTEnLYotDmBbe5Y6fUfRgaQ",
  "authDomain": "knots-ai.firebaseapp.com",
  "databaseURL": "https://knots-ai.firebaseio.com",
  "storageBucket": "knots-ai.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
available = 1

print 1
run = 0
data_path = None
def stream_handler(message):
	global run
	global available
	data = message["data"]
	if run == 0:
		for i in data.values():
			if i['pStatus']==0 and available == 1:
				data_path = i['data']
				print(data_path)
				available == 0
				break
		run = 1
	elif run ==1:
		if data['pStatus']==0 and available == 1:
				data_path = data['data']
				print(data_path)
				available == 0
my_stream = db.child("CVP").stream(stream_handler)