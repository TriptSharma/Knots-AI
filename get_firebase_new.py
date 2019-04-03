import pyrebase

config = {
  "apiKey": "AIzaSyDzUK8CJ4ADaTEnLYotDmBbe5Y6fUfRgaQ",
  "authDomain": "knots-ai.firebaseapp.com",
  "databaseURL": "https://knots-ai.firebaseio.com",
  "storageBucket": "gs://knots-ai.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

data = {
    "name": "Mortimer 'Morty' Smith"
}
results = db.child("users").push(data)


