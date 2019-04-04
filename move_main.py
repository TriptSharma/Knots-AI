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

users = db.child("queries").get(get_dict=True)
sorted_users = sorted(users.items(), key=lambda x: x[1]['time'])

sorted_users = list(sorted_users)
#print(sorted_users)


i = 0
while 1:
    if sorted_users[i][1]['services']['move'] == 1:   
        key = sorted_users[i][0] 
        vehicle_category = sorted_users[i][1]['data']['movement']
        print(vehicle_category)
        if vehicle_category['category'] == 'd_drive':
            error = vehicle_category['erros']['error']
            e_sum = vehicle_category['erros']['e_sum']
            e_old = vehicle_category['erros']['e_old']
            print(key)
            Kp = 10
            Ki = 0.1
            Kd = 0.0
            movement = Kp*error + Ki*(error + e_sum) + Kd*(error-e_old) ;

            db.child("queries").child(key).update({"response":{"movement": movement}})
            break
    if i== len(sorted_users)-1:
        break
    i = i + 1


#storage.child("images/example.jpg").put("sample.jpg")
