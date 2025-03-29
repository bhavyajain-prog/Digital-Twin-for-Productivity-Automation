const admin = require("firebase-admin");
const {initializeApp} = require("firebase/app");
const { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } = require("firebase/auth");


const serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://lnm-intelitwin.firebaseio.com",
});

const firebaseConfig = {
  apiKey: "AIzaSyAVcWQYmAejvYqi8dn75BMRCGLqE4uiSHA",
  authDomain: "lnm-intellitwin.firebaseapp.com",
  projectId: "lnm-intellitwin",
  storageBucket: "lnm-intellitwin.firebasestorage.app",
  messagingSenderId: "487010020847",
  appId: "1:487010020847:web:d0bd479658552257181a1a",
};

const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth(firebaseApp); // This is the correct way to get Auth in newer Firebase versions

// Export modules
const db = admin.firestore();

module.exports = { admin, db, auth, createUserWithEmailAndPassword, signInWithEmailAndPassword };
