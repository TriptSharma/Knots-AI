import pyrebase
import numpy as np
import  pandas as pd
from collections import OrderedDict
config = {
  "apiKey": "AIzaSyDzUK8CJ4ADaTEnLYotDmBbe5Y6fUfRgaQ",
  "authDomain": "knots-ai.firebaseapp.com",
  "databaseURL": "https://knots-ai.firebaseio.com",
  "storageBucket": "knots-ai.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

#set user info
users = db.child("queries").get(get_dict=True)
# print(users)

# for i in users.items():
# 	print(i,  i[1]['time'])
	# exit()

sorted_users = sorted(users.items(), key=lambda x: x[1]['time'])
print(sorted_users)

sorted_users = list(sorted_users)

datapath = sorted_users[0][1]['data']
audiopath = datapath['audio']

storage.child(str(audiopath)).download("sample.wav")

