const { db } = require("./firebase");

async function testFirestore() {
  try {
    const docRef = db.collection("testCollection").doc("testDoc");
    await docRef.set({ message: "Hello from Firestore!" });
    console.log("Data written successfully!");

    const doc = await docRef.get();
    console.log("Read from Firestore:", doc.data());
  } catch (error) {
    console.error("Error:", error);
  }
}

testFirestore();
