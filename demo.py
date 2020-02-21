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
query_key = None
run = 0
data_path = None

def stream_handler(message):
	global run
	global query_key
	data = message["data"]
	keys = data.keys()
	if run == 0:
		for [num,i] in enumerate(data.values()):
			if i['pStatus']==0 and available == 1:
				data_path = i['data']
				query_key = keys[num]
				print(query_key)
				# available == 0
				# break
		run = 1
	elif run ==1:
		if data['pStatus']==0 and available == 1:
				data_path = data['data']
				available == 0
				query_key = message["path"][1:]
				perform_task()

def perform_task():
	update_status(2)

def update_status(status):
	global query_key
	db.child("CVP").child(query_key).update({"pStatus": status})
	print status


my_stream = db.child("CVP").stream(stream_handler)
