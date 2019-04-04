import pyrebase
import time
import numpy as np
config = {
  "apiKey": "AIzaSyDzUK8CJ4ADaTEnLYotDmBbe5Y6fUfRgaQ",
  "authDomain": "knots-ai.firebaseapp.com",
  "databaseURL": "https://knots-ai.firebaseio.com",
  "storageBucket": "knots-ai.appspot.com"
}

unique_id = 1000000

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
storage.child(str(unique_id)+"/audio/sound.wav").put("sound.wav")
data = {
    "services": {
        "camera":1,
        "NLP":1,
        "move":1
    },
    "data": {
    "image": str(unique_id)+"/images/example.jpg",
    "audio": str(unique_id)+"/audio/sound.wav",
    "movement":{
      "category":"d_drive",
      "errors":{
        "error": 3,
        "e_old": 0,
        "e_sum": 0
      } 
    }
    },
    "status": 2, # -1 for not possible, 0 for unoccupied, 1 for occupied and 2 for done 
    "time":str(time.time())
}
results = db.child("queries").push(data)
#storage.child("images/example.jpg").put("sample.jpg")
