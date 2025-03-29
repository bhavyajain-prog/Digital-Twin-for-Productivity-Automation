const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Routes will be added here later
app.get("/", (req, res) => {
  res.send("Backend is running...");
});

const userRoutes = require("./routes/userRoutes");
app.use("/users", userRoutes);
const authRoutes = require("./routes/authRoutes");
app.use("/auth", authRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
