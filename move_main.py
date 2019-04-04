import pyrebase
import json
from collections import namedtuple
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

Kp = 10 
Ki = 0.1
Kd = 0.0 
my_list = []
users_by_name = db.child("queries").get()
for user in users_by_name.each():
  x = json.loads(str(user.val()), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
  my_list.append(x)

print(my_list)

movement = Kp*e + Ki*(e + e_sum) + Kd*(e-e_old) ;


#storage.child("images/example.jpg").put("sample.jpg")
