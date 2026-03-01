const express = require('express');
const multer = require('multer');
const aiController = require('../controllers/ai.controller');

const router = express.Router();

// Setup multer memory storage to keep file in buffer
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// POST /api/ai/upload-csv
router.post('/upload-csv', upload.single('file'), aiController.uploadAndPredict);

module.exports = router;
