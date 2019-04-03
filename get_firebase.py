from firebase import Firebase
f = Firebase('https://knots-ai.firebaseio.com/')
f = Firebase('https://knots-ai.firebaseio.com//message_list')
r = f.push({'user_id': 'tripti', 'text': [1, 2, 3]})



