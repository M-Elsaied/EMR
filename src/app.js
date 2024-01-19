const express = require('express');
const app = express();
const port = process.env.PORT || 3000; // Ensure you're not using port 5000

app.get('/ping', (req, res) => {
    res.status(200).send('pong');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

module.exports = app;
