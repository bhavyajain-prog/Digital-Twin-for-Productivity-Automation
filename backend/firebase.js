const admin = require("firebase-admin");

// Load the service account key (Download it from Firebase Console)
const serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://lnm-intelitwin.firebaseio.com",
});

const db = admin.firestore();

module.exports = { db };
