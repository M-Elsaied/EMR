const express = require('express');
const patientRoutes = require('./routes/patientRoutes');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json()); // for parsing application/json

app.use('/api/patients', patientRoutes); // Register patient routes

app.get('/ping', (req, res) => {
    res.status(200).send('pong');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

module.exports = app;
