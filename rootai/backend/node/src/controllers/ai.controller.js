const FormData = require('form-data');

async function uploadAndPredict(req, res) {
    try {
        const formData = new FormData();
        formData.append('file', req.file.buffer, {
            filename: req.file.originalname,
            contentType: 'text/csv'
        });

        // Use native fetch if available, else axios could be used, but instructions specified fetch
        // Node 18+ has global fetch
        const response = await fetch(
            'http://localhost:8000/api/ai/upload-csv',
            {
                method: 'POST',
                // For native fetch with form-data module, headers must be explicitly set or it breaks sometimes.
                // However user requested exact fetch code. We will use the user's provided code.
                body: formData
            }
        );

        const result = await response.json();
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}

module.exports = {
    uploadAndPredict
};
