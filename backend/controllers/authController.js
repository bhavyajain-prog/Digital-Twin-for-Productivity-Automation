const {
  auth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} = require("../config/firebase");

const { admin } = require("../config/firebase");

const signup = async (req, res) => {
  const { name, email, password } = req.body;

  try {
      const userCredential = await createUserWithEmailAndPassword(
      auth,
      email,
      password
    );
    const user = userCredential.user;

    res.status(201).json({
      message: "User created successfully",
      uid: user.uid,
      email: user.email,
    });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

const login = async (req, res) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) {
      return res.status(400).json({ message: "Email and password required." });
    }
    const userCredential = await signInWithEmailAndPassword(
      auth,
      email,
      password
    );
    const user = userCredential.user;
    const token = await admin.auth().createCustomToken(user.uid);

    res.status(200).json({ message: "Login successful", token });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const verifyToken = async (req, res) => {
  try {
    const { token } = req.body;
    if (!token) {
      return res.status(400).json({ message: "Token required" });
    }

    const decodedToken = await admin.auth().verifyIdToken(token);
    res
      .status(200)
      .json({ message: "Token is valid", userId: decodedToken.uid });
  } catch (error) {
    res.status(401).json({ error: "Invalid or expired token" });
  }
};

module.exports = { signup, login, verifyToken };
