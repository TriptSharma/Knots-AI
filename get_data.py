import pyrebase
import numpy as np
import  pandas as pd

config = {
  "apiKey": "AIzaSyDzUK8CJ4ADaTEnLYotDmBbe5Y6fUfRgaQ",
  "authDomain": "knots-ai.firebaseapp.com",
  "databaseURL": "https://knots-ai.firebaseio.com",
  "storageBucket": "knots-ai.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

def get_sorted_data():
	#set user info
	# print(users)

	users = db.child("queries").get(get_dict=True)
	# for i in users.items():
	# 	print(i,  i[1]['time'])
		# exit()

	sorted_users = sorted(users.items(), key=lambda x: x[1]['time'])
	# print(sorted_users)

	sorted_users = list(sorted_users)

	return sorted_users

def download_file(folder):
	sorted_users = get_sorted_data()
	datapath = sorted_users[0][1]['data']
	# print(datapath)
	path = datapath[folder]
	filename = folder
	try:
		if folder == 'audio':
			filename+='.wav'
			
		elif folder == 'image':
			filename+='.jpg'
		storage.child(str(path)).download(filename)
		return filename
	except:
		print("File not accessible!")
		return None
