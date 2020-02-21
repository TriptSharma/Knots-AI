const functions = require('firebase-functions');
// const admin = require('firebase-admin');

// admin.initializeApp();


// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });


exports.checkQuery = functions.database.ref('/queries/{pushid}')
	.onCreate((snapshot, context) => {
		// Grab the current value of what was written to the Realtime Database.
		const original = snapshot.val();
		console.log('Received query', context.params.pushId, original);
		// You must return a Promise when performing asynchronous tasks inside a Functions such as
		// writing to the Firebase Realtime Database.
		// Setting an "uppercase" sibling in the Realtime Database returns a Promise.
		const status = 1;
		let cv;
		if (original.services.camera === 1){
			cv = {data: original.data.image,
				qStatus: original.status,
				time : original.time,
				result : null,
				pStatus : 0
			}
		}
		let nlp;
		if (original.services.NLP === 1){
			nlp = {data: original.data.audio,
				qStatus: original.status,
				time : original.time,
				result : null,
				pStatus : 0
			}
		}

		return snapshot.ref.parent.parent.child(`/CVP/${context.params.pushid}`).set(cv), snapshot.ref.parent.parent.child(`/NLP/${context.params.pushid}`).set(nlp);
	});