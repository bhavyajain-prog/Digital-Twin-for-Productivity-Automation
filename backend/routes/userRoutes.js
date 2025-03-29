const express = require("express");
const router = express.Router();
const { getUsers, createUser } = require("../controllers/userController");

router.get("/", getUsers);
router.post("/", createUser);

module.exports = router;
